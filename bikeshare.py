import time
import pandas as pd
import numpy as np


# Adding some comments
# More comments
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def print_head():
    # This function simply prints the head of each dataset
    for key, value in CITY_DATA.items():
        print("First five values of {}'s dataset".format(key))
        print(pd.read_csv(value).head())


# A comment here
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    # Check for valid input
    cities = ['chicago', 'new york city', 'washington']
    months = ['january','february','march','april','may','june','all']
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
       
    city = input("\nWhat city would you like to filter by? Please enter a string with the full city name. \n").lower()
    if city in cities:
        pass
    else:
        city = 'new york city'
        print("\nYou entered an invalid city! Defaulting to 'new york city'")
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("\nWhat month would you like to filter by? Type 'all' for all months. Please enter a string with the full month name. \n").lower()
    if month in months:
        pass
    else:
        month = 'all'
        print("\nYou entered an invalid month! Defaulting to 'all'")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("\nWhat day of the week would you like to filter by? Type 'all' for all days.  Please enter a string with the full day name. \n").lower()
    if day in days:
        pass
    else:
        day = 'all'
        print("\nYou entered an invalid day! Defaulting to 'all'")
    
    print("\nYour choices for filtering are \ncity: {} \nmonth: {} \nday: {}".format(city, month, day))
    
    choice = input("Would you like to change these choices? Y/N \n")
    if choice == 'Y' or choice == 'y':
        print()
        get_filters()
    
    return city, month, day

# A comment there


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("\nThe most common month is: \n",df['month'].mode()[0])

    # TO DO: display the most common day of week
    print("\nThe most common day of the week is: \n",df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print("\nThe most common day of the week is: \n",df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is: \n", df['Start Station'].mode()[0])
    
    # TO DO: display most commonly used end station
    print("The most commonly used end station is: \n", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    # This technique was aided by code found on the link https://stackoverflow.com/questions/35268817/unique-combinations-of-values-in-selected-columns-in-pandas-data-frame-and-count
    pairs_df = pd.DataFrame(df.groupby(['Start Station','End Station']).size().reset_index().rename(columns={0:'count'}).sort_values('count', ascending=False)).reset_index()
    print("The most commonly used combination of start station and end station is: \n", pairs_df[['Start Station','End Station']].iloc[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("\nThe total travel time was: \n", df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("\nThe mean travel time was: \n", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# This is a comment.
# This is another comment.
def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    print("\nThe count of user types is: \n" ,df.groupby('User Type').size())
    
    # Failsafe for washington: no birth year or gender column.
    if city == 'washington':
        pass
    else:
        # TO DO: Display counts of gender
        print("\nThe count of genders is: \n", df.groupby('Gender').size())

        # TO DO: Display earliest, most recent, and most common year of birth
        print("\nThe earliest birth year is: \n",df['Birth Year'].min())
        print("\nThe most recent birth year is: \n",df['Birth Year'].max())
        print("\nThe most common birth year is: \n",df['Birth Year'].mode()[0])   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_raw_data(df):
    choice = input('\nWould you like to see raw data? Enter yes or no.\n').lower()
    i = 0
    while choice == 'yes':
        print(df[i:i+5])
        i += 5
        choice = input('\nWould you like to see raw more data? Enter yes or no.\n').lower()
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        user_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            
if __name__ == "__main__":
	main()
