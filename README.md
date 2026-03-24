# TermProject_DSA210

Motivation and Objective
The tech industry has recently seen a huge wave of layoffs, often called the "Tech
Winter". My project looks at whether these layoffs actually lead to more people working
on open-source coding projects. The idea is that when skilled developers lose their jobs,
they might use their free time to contribute to public projects on GitHub to keep their
skills sharp and stay visible to recruiters. I want to see if there is a measurable link
between when these layoffs happen and when we see spikes in global coding activity.

Data Source and Collection
I will combine three different datasets for this analysis. First, I will get layoff data from
"Layoffs.fyi," which tracks daily firing numbers in a CSV file. To enrich this, I will use the
GitHub APl to get daily counts of commits and pull requests from 50 popular public
repositories. Finally, I will add daily stock market data for the NASDAQ-100 using a
Python library to see how the overall tech economy was doing at the same time.

Data Characteristics
The final dataset will be a table where each row is a single day. I expect to have around
1,000 to 1,500 days of data covering the last few years. The main columns will be the
number of layoffs, the amount of GitHub activity, and the stock market price for that day.
I will need to clean the data to handle missing values and make sure the dates from all
three sources line up correctly before I start my analysis.
