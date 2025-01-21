import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Asks the user to specify a city, month, and day to analyze.

    Returns:
        (str) city - the city to analyze
        (str) month - the month to filter by, or "all" for no filter
        (str) day - the day of the week to filter by, or "all" for no filter
    """
    print("Hello! Let's explore some US bikeshare data!")

     # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input("Choose a city (Chicago, New York City, Washington): ").strip().lower()
        if city in cities:
            break
        print("Invalid input. Please select from Chicago, New York City, or Washington.")

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("Choose a month (January to June) or 'all' for no filter: ").strip().lower()
        if month in months:
            break
        print("Invalid input. Please select a valid month or 'all'.")

     # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input("Choose a day of the week or 'all' for no filter: ").strip().lower()
        if day in days:
            break
        print("Invalid input. Please select a valid day or 'all'.")

    print('-' * 50)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and applies filters for month and day if applicable.

    Args:
        city (str): Name of the city
        month (str): Month to filter by, or "all" for no filter
        day (str): Day of the week to filter by, or "all" for no filter

    Returns:
        DataFrame: Filtered bikeshare data
    """
    df = pd.read_csv(CITY_DATA[city])

    # Convert Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()

    # Filter by month
    if month != 'all':
        month_idx = ['january', 'february', 'march', 'april', 'may', 'june'].index(month) + 1
        df = df[df['month'] == month_idx]

    # Filter by day
    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """Displays the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

     # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print(f"Most Common Month: {common_month}")

     # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(f"Most Common Day: {common_day.title()}")

     # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(f"Most Common Hour: {common_hour}")

    print(f"\nThis took {time.time() - start_time:.2f} seconds.")
    print('-' * 50)

def station_stats(df):
    """Displays the most popular stations and trips."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f"Most Common Start Station: {common_start_station}")

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"Most Common End Station: {common_end_station}")

     # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + " to " + df['End Station']
    common_trip = df['trip'].mode()[0]
    print(f"Most Common Trip: {common_trip}")

    print(f"\nThis took {time.time() - start_time:.2f} seconds.")
    print('-' * 50)

def trip_duration_stats(df):
    """Displays statistics on total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

     # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    print(f"Total Travel Time: {total_duration} seconds")

    # TO DO: display mean travel time
    mean_duration = df['Trip Duration'].mean()
    print(f"Mean Travel Time: {mean_duration:.2f} seconds")

    print(f"\nThis took {time.time() - start_time:.2f} seconds.")
    print('-' * 50)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

     # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User Types:")
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("\nGender Counts:")
        print(gender_counts)
    else:
        print("\nNo gender data available.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"\nEarliest Birth Year: {earliest_year}")
        print(f"Most Recent Birth Year: {most_recent_year}")
        print(f"Most Common Birth Year: {common_year}")
    else:
        print("\nNo birth year data available.")

    print(f"\nThis took {time.time() - start_time:.2f} seconds.")
    print('-' * 50)

def display_raw_data(df):
    """Displays raw data upon user request."""
    print('\nDisplaying raw data...\n')
    start_idx = 0
    while True:
        raw_data = input("Would you like to see 5 rows of raw data? Enter yes or no: ").strip().lower()
        if raw_data != 'yes':
            break
        print(df.iloc[start_idx:start_idx + 5])
        start_idx += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input("\nWould you like to restart? Enter yes or no: ").strip().lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
    main()
