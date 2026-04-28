# Tech_Winter_Analysis_DSA210_Nolan_Efe
DSA210 Term Project / Fall 2025-2026

# Tech Winter Analysis: Layoffs vs. Open-Source Commits (2020 - 2023)

## Motivation

I have always been interested in how macroeconomic instability impacts human productivity and professional behavior. We can see this in how industries shift and how people adapt their skill sets during economic downturns. 

I intend to explore this topic through the lens of software engineering and open-source contributions. 

Additionally, I follow stock market trends and macroeconomic indicators closely. The recent "Tech Winter" (2020-2023) provided a unique historical period where massive industry layoffs coincided with a highly volatile stock market. This project combines both interests. My goal is to see if mass tech layoffs and market crashes have a measurable effect on developer output. For example, do developers code more in open-source repositories when they face job insecurity, or does a market crash cause a drop in overall programming activity?

---

## Overview

This project investigates the correlation between macroeconomic instability and open-source software development. Specifically, it analyzes the "Tech Winter" to determine if mass industry layoffs actually lead to more people working on open-source coding projects across 50 major GitHub repositories. The analysis also incorporates NASDAQ-100 stock market data to provide context on how the overall tech economy was doing at the same time.

---

## Data to be Utilized

### 1. Industry Instability (Layoffs)
* **Source:** Layoffs.fyi (downloaded as a CSV file).
* **Data:** Daily firing numbers and total headcount reductions across the tech sector.

### 2. Open-Source Developer Activity (GitHub)
* **Source:** GitHub REST API.
* **Data:** Daily counts of commits and pull requests from 50 of the most popular public repositories.
* **Method:** I utilized a GitHub Personal Access Token and a custom Python pacing script to systematically extract this data without hitting the API's severe rate limits.

### 3. Macroeconomic Context (Stock Market)
* **Source:** Historical financial data accessed via a Python library (e.g., yfinance).
* **Data:** Daily closing prices for the NASDAQ-100 index to measure the overall health and sentiment of the tech economy on those exact same days.

---

## Methodology

### Data Cleaning & Integration
* I needed to standardize the 4-year timeline across three entirely different data sources (GitHub, Stocks, and Layoffs).
* I used forward-filling methods to handle missing values for the NASDAQ data (since markets are closed on weekends and holidays) to maintain daily continuity.
* Merging: I successfully merged the datasets on the date index, resulting in a final master dataset of 1,461 continuous days with complete commit, stock, and layoff information.

### Visualization
* I first created baseline distribution plots to understand the spread and scale of GitHub commits and layoff events.
* Then, I created scatter plots and line charts over time to visually identify potential relationships between NASDAQ drops, layoff spikes, and GitHub commit volume.

### Hypothesis Tests
I performed statistical tests to validate two specific hypotheses before moving to machine learning.

**1) The "Market Sentiment" Effect**
* **Null 1:** The NASDAQ closing price has no significant correlation with daily open-source commit volume.
* **Alternative 1:** There is a significant negative correlation between the NASDAQ price and commits.
* **Result:** Reject H0. A declining tech market strongly correlates with increased overall open-source activity. As the economy cools, developer output rises.

**2) The "Layoff Panic" Response**
* **Null 2:** There is no significant difference in the average number of commits on days with massive layoffs versus normal days.
* **Alternative 2:** Days with high layoffs see a significantly higher average number of commits.
* **Result:** Failed To Reject H0. Statistical testing showed no significant immediate spike in commits on the exact days layoffs were announced, proving developers react to broader trends rather than daily news.

---

## Machine Learning (ML)

In the final phase of the project, I applied machine learning techniques to test if market events are predictive of developer behavior, moving beyond simple correlation.

### 1. Random Forest Regression (Supervised Learning)
* **Goal:** Predict the exact volume of daily GitHub commits based on the NASDAQ closing price and Layoff counts.
* **Result:** The model produced a negative R-squared score.
* **Interpretation:** The regression model failed to predict daily behavior. More importantly, the Feature Importance analysis revealed the model put nearly 100% of its weight on the NASDAQ and ignored the layoff data. This proves daily layoffs are too noisy to be a reliable numerical predictor for daily commits.

### 2. k-Nearest Neighbors Classification (Supervised Learning)
* **Goal:** To classify days as "Panic Days" (layoffs > 0) or "Normal Days" based on commit and stock data.
* **Result:** The model achieved an 83% accuracy, but a Recall of 0.00 for Panic Days.
* **Interpretation:** This is a textbook example of the "Accuracy Paradox." Because layoff days are relatively rare, the algorithm simply guessed "Normal Day" for every single test case. This proves that a layoff event is a "Black Swan" occurrence that lacks a consistent daily precursor in the data.

### 3. K-Means Clustering (Unsupervised Learning)
* **Goal:** To see if the data naturally groups into distinct economic "Eras" rather than focusing on daily predictions.
* **Method:** Used the Elbow Method to determine that k=3 was the optimal number of clusters.
* **Findings:** The algorithm successfully bypassed the daily noise and isolated the "Tech Winter" into its own distinct cluster.
* **Conclusion:** The unsupervised model proved that the tech economy acts like the "climate" rather than the "weather." Developers do not react to single, daily layoff announcements. Instead, they shift their long-term behavior in response to the broader market sentiment over several months.

---

## Future Work & Limitations
* **Class Sparsity:** The dataset contains extreme sparsity regarding layoff days. Future iterations would require specific anomaly detection models (like Isolation Forests) rather than standard classifiers to handle these "Black Swan" events.
* **Lack of Qualitative Data:** Commits are counted purely by volume. A single typo fix counts the same as a massive architectural code change. Future work should analyze the size or complexity of the commits (lines of code changed) to measure the true depth of developer contribution.
* **Confounding Variables:** Other global events during 2020-2023 (such as pandemic lockdowns and the shift to remote work) heavily influenced screen time and coding habits. A more rigorous causal study is needed to isolate economic factors from lifestyle changes.

---

## Structure of Project

* `get_github_data.py`: Script to pull historical daily commit data from 50 target open-source repositories via the GitHub API.
* `get_stocks.py`: Script to gather historical macroeconomic NASDAQ data.
* `clean_data.ipynb` / `clean_data.py`: The data engineering scripts used for cleaning, handling NaN values, and merging all three pillars.
* `Tech_Winter_Analysis.ipynb`: The primary analysis notebook containing Exploratory Data Analysis (EDA), baseline statistics, visual distributions, hypothesis testing, and the complete Machine Learning pipeline.
* `FINAL_MASTER_DATASET.csv`: The fully cleaned, merged, and ready-to-analyze dataset (1,461 daily rows).
* `github_commits_raw.csv`, `nasdaq_data.csv`, `layoffs_data.csv`: Intermediate raw data files collected by the scripts.
* `requirements.txt`: List of Python dependencies required to run the pipeline and notebooks.
* `README.md`: The main project documentation.

---

## How to Run

### 1. Set Up the Environment
Ensure you have Python installed, then install the required dependencies by running the following command in your terminal:

pip install -r requirements.txt

### 2. Configure API Access (GitHub)

To reproduce the GitHub data collection without hitting severe rate limits, you must use a GitHub Personal Access Token.

Open get_github_data.py.

Locate the variable GITHUB_TOKEN.

Replace the placeholder string with your own valid GitHub token.

### 3. Run the Pipeline

To build the dataset and view the analysis from scratch, execute the files in the following order:

Run python get_github_data.py to pull the raw commit data. (Note: This process takes time due to API rate-limit pacing).

Run python get_stocks.py to pull the macroeconomic context.

Open and run all cells in clean_data.ipynb to format and merge the datasets.

Open and run all cells in Tech_Winter_Analysis.ipynb to view the master timeline, baseline statistics, EDA visualizations, hypothesis tests, and the final Machine Learning models.

---

## AI Usage Disclaimer
In this project, I utilized AI tools (Gemini) to assist with:

Code Refactoring: Optimizing pandas merge operations and data cleaning logic.

Data Visualization: Assisting with matplotlib and seaborn syntax for clear, professional plot formatting.

