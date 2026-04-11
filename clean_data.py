import pandas as pd

# Loading the raw layoffs data (skipping the broken header row)
df = pd.read_csv('layoffs_data.csv', skiprows=1)

# Converting the date column into a standard datetime format
df['date'] = pd.to_datetime(df['date'])

# Isolating the exact 4-year timeline for my "Tech Winter" analysis
tech_winter_df = df[(df['date'] >= '2020-01-01') & (df['date'] <= '2023-12-31')]

# Saving the cleaned, filtered data to a new file without the index numbers
tech_winter_df.to_csv('tech_winter_2020_to_2023.csv', index=False)