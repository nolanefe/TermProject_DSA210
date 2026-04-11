import requests
import pandas as pd
import time
import os

# My token
# I'm using this token to authenticate my requests so GitHub allows me to 
# pull data more frequently than a guest user would be allowed
GITHUB_TOKEN = "MY_TOKEN_HERE"
headers = {"Authorization": f"token {GITHUB_TOKEN}"}

# This list contains 50 high-impact open-source repositories analyzed 
# to measure general developer activity levels across different tech sectors
repos = [
    # --- Backend & Languages ---
    "golang/go", "rust-lang/rust", "nodejs/node", "python/cpython", 
    "microsoft/TypeScript", "denoland/deno", "spring-projects/spring-boot", 
    "laravel/laravel", "django/django", "pallets/flask",
    
    # --- Data Science & Machine Learning ---
    "tensorflow/tensorflow", "keras-team/keras", "pytorch/pytorch", 
    "scikit-learn/scikit-learn", "pandas-dev/pandas", "numpy/numpy", 
    "huggingface/transformers", "apache/spark", "elastic/elasticsearch", "opencv/opencv",
    
    # --- Infrastructure, DevOps & Tools ---
    "kubernetes/kubernetes", "docker/compose", "moby/moby", "prometheus/prometheus", 
    "hashicorp/terraform", "ansible/ansible", "git/git", "torvalds/linux", 
    "microsoft/vscode", "github/gitignore",
    
    # --- Databases & Systems ---
    "postgres/postgres", "redis/redis", "mongodb/mongo", "cockroachdb/cockroach", "pingcap/tidb",
    
    # --- Utilities & Community Favorites ---
    "ohmyzsh/ohmyzsh", "facebook/jest", "prettier/prettier", "webpack/webpack", "d3/d3"
]

csv_filename = "github_commits_raw.csv"

print("Starting Final Data Collection (webpack and d3)...")

for repo in repos:
    print(f"Scanning {repo}...")
    # This URL is the specific endpoint for the GitHub Commits API
    url = f"https://api.github.com/repos/{repo}/commits"
    
    # I'm setting a 4-year window here to capture the entire 'Tech Winter' timeline
    # I'm also asking for 100 commits per page to reduce the total number of API calls I have to make
    params = {
        "since": "2020-01-01T00:00:00Z",
        "until": "2023-12-31T23:59:59Z",
        "per_page": 100
    }
    
    repo_commits = []
    page = 1
    
    # Since I don't know exactly how many pages of commits exist
    # I'm using a 'while True' loop to keep fetching until GitHub tells me there's nothing left
    while True:
        params['page'] = page
        try:
            response = requests.get(url, headers=headers, params=params, timeout=10)
            
            # 403 usually means I've hit the rate limit for the hour
            if response.status_code == 403:
                print(f"  -> Rate limit hit at {repo}. Stopping this repo.")
                break
            elif response.status_code != 200:
                print(f"  -> Error {response.status_code} at {repo}. Moving to next.")
                break
                
            commits = response.json()
            # If the response is an empty list, it means I've reached the last page of data
            if not commits: 
                break
                
            for commit in commits:
                # GitHub provides dates in ISO 8601 format (e.g., YYYY-MM-DDTHH:MM:SSZ)
                # I am splitting the string at the 'T' and selecting index [0] 
                # to extract only the date part, as my analysis is conducted on a daily basis
                date_str = commit['commit']['author']['date']
                repo_commits.append({
                    "repo": repo,
                    "date": date_str.split('T')[0]
                })
                
            page += 1
            # I'm adding a small pause here to be respectful of GitHub's servers 
            # and to stay under the rate limit 'radar.'
            time.sleep(0.6) 
            
        except requests.exceptions.Timeout:
            print(f"  -> Connection timed out on {repo} page {page}. Saving what we have and moving on.")
            break
        except Exception as e:
            print(f"  -> Unexpected error: {e}. Moving on.")
            break

    # Append directly to my existing giant CSV
    if repo_commits:
        # Converting my list of dictionaries into a DataFrame for easy CSV export
        df = pd.DataFrame(repo_commits)
        
        # I'm using mode='a' (append) so I don't overwrite the data I've already collected
        # for previous repositories in this session
        # header=False ensures I don't put "repo,date" in the middle of my data
        df.to_csv(csv_filename, mode='a', header=False, index=False)
        print(f"  [SAVED] {len(df)} commits appended to disk.")

print("Process completely finished. Congratulations!")