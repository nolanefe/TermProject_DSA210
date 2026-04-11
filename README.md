# Tech Winter Analysis: Layoffs vs. Open-Source Commits (2020 - 2023)

## Project Overview
This project investigates the correlation between macroeconomic instability and open-source software development. Specifically, it analyzes the "Tech Winter" to determine if mass industry layoffs actually lead to more people working on open-source coding projects across 50 major GitHub repositories. The analysis also incorporates NASDAQ-100 stock market data to provide context on how the overall tech economy was doing at the same time.

## Repository Structure
* **`get_github_data.py`**: Script to pull historical daily commit data from 50 target open-source repositories via the GitHub Commits API.
* **`get_stocks.py`**: Script to gather historical macroeconomic NASDAQ data.
* **`clean_data.ipynb`**: The data engineering pipeline. This notebook cleans the raw data, handles duplicates, standardizes the 4-year timeline, and merges all three pillars into the final master dataset.
* **`Tech_Winter_Analysis.ipynb`**: The primary analysis notebook containing Exploratory Data Analysis (EDA), baseline statistics, visual distributions, and hypothesis testing. *(Machine Learning modeling is currently in progress).*
* **`FINAL_MASTER_DATASET.csv`**: The fully cleaned, merged, and ready-to-analyze dataset (1,461 daily rows).

## Instructions to Reproduce the Analysis

### 1. Set Up the Environment
Ensure you have Python installed, then install the required dependencies by running the following command in your terminal:
`pip install -r requirements.txt`

### 2. Configure API Access (GitHub)
To reproduce the GitHub data collection without hitting severe rate limits, you must use a GitHub Personal Access Token.
1. Open `get_github_data.py`.
2. Locate the variable `GITHUB_TOKEN`.
3. Replace the placeholder string with your own valid GitHub token.

### 3. Run the Pipeline
To build the dataset and view the analysis from scratch, execute the files in the following order:
1. Run `get_github_data.py` to pull the raw commit data. (Note: This process takes time due to API rate-limit pacing).
2. Run `get_stocks.py` to pull the macroeconomic context.
3. Open and run all cells in `clean_data.ipynb` to format and merge the datasets.
4. Open and run all cells in `Tech_Winter_Analysis.ipynb` to view the master timeline, baseline statistics, EDA visualizations, and hypothesis tests.

Note: This repository is actively being updated. Machine Learning methods on the dataset and final conclusions will be added in the next milestones.
