Bikeshare Data Analysis

This project is part of the Udacity Programming for Bigdata and Hadoop Nanodegree program. The objective is to explore data related to bike-sharing systems in three major U.S. cities: Chicago, New York City, and Washington, D.C. The program provides insights into bike-sharing usage by answering key questions and presenting statistics interactively.

Overview

Bikeshare systems allow users to rent bicycles for short-term use, either for one-way or round trips. This project analyzes data from these systems to uncover usage patterns, popular stations, trip durations, and user demographics. The datasets span the first six months of 2017 and include data on:

Start Time

End Time

Trip Duration

Start Station

End Station

User Type

Additional columns, such as Gender and Birth Year, are available for Chicago and New York City.

Features

Interactive Filtering:

Users can filter data by city, month, and day of the week.

Offers an interactive experience in the terminal to explore filtered statistics.

Key Insights:

Popular times of travel:

Most common month, day of the week, and hour of the day.

Popular stations and trips:

Most commonly used start and end stations.

Most frequent trip (combination of start and end stations).

Trip durations:

Total travel time.

Average travel time.

User information:

Counts of user types (Subscriber vs. Customer).

Counts of gender (available for NYC and Chicago).

Earliest, most recent, and most common year of birth (available for NYC and Chicago).

Raw Data Display:

Users can view raw data in chunks of 5 rows upon request.

Datasets

The datasets used in this project are provided by Motivate, a bike share system provider in the United States. They include data for the first six months of 2017 for Chicago, New York City, and Washington.

Columns in the Datasets:

Core Columns:

Start Time

End Time

Trip Duration

Start Station

End Station

User Type (Subscriber or Customer)

Additional Columns for NYC and Chicago:

Gender

Birth Year


Project Files

bikeshare.py: The main Python script that performs the analysis.

Dataset Files:

chicago.csv

new_york_city.csv

washington.csv

Technologies Used

Python 3.7+

pandas

NumPy

Text Editors: VSCode, Sublime, or PyCharm

Terminal Applications: Terminal (Mac/Linux) or Command Prompt (Windows)

How to Run

Clone the repository:

git clone <repository-url>

Navigate to the project directory:

cd bikeshare-analysis

Install required libraries if not already installed:

pip install pandas numpy

Run the program:

python bikeshare.py

Usage Instructions

Start the program:

You will be prompted to select:

A city (Chicago, New York City, or Washington).

A month (January to June, or all).

A day of the week (Monday to Sunday, or all).

View calculated statistics:

Most frequent travel times.

Popular stations and trips.

Total and average trip durations.

User demographics (if available).

View raw data:

After seeing statistics, you can request to view the raw data in 5-row increments.
