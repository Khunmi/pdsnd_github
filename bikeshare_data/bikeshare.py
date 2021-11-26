import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input('Kindly specify a city you would like analyse amongst chicago, new york city and washington: ').lower().replace(' ','_')
        if city not in ('chicago','new_york_city','washington'):
            print('Sorry, incorrect input.')
        else:
            break# TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        month = input('Enter your month of choice as integer; with jan = 1, feb = 2 and so on: ').lower()
        if month not in ('1','2','3','4','5','6','all'):
            print('Sorry, incorrect input.')
        else:
            break# TO DO: get user input for month (all, january, february, ... , june)

    while True:
        day = input('Please select your choice of weekday: ').lower()
        if day not in ('monday','tuesday','wednesday','thursday','friday','saturday','sunday','all'):
            print('Sorry, incorrect input.')
        else:
            break# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day


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
    df = pd.read_csv('{}.csv'.format(city))
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        df= df[df['month'] == int(month)]
    if day != 'all':
        df= df[df['day_of_week'] == day.title()]
    


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    most_common_month = df['month'].mode()[0] 

    
    print('Most common month is: ', most_common_month)# TO DO: display the most common month
    
    most_common_day =  df['day_of_week'].mode()[0]


    print('\nMost common day of the week is: ', most_common_day)# TO DO: display the most common day of week


    most_common_hour = df['Start Time'].dt.hour
    most_common_hour = most_common_hour.mode()[0]
    print('\nMost common start hour is: ', most_common_hour)# TO DO: display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    mst_common_start_station = df['Start Station'].mode()[0] 
    
    print('\nMost common start station is: ', mst_common_start_station)# TO DO: display most commonly used start station


    mst_common_end_station = df['End Station'].mode()[0]
        
    print('\nMost common end station is: ', mst_common_end_station)   # TO DO: display most commonly used end station


    mst_common_combo =  df['Start Station'] + ' and ' + df['End Station']
    mst_common_combo = mst_common_combo.mode()[0] 
    
    print('\nMost common station combination is: ', mst_common_combo)# TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    travel_time = df['Trip Duration'].sum()
    print('\nThe total travel time is: {} seconds.'.format(travel_time)) # TO DO: display total travel time


    mean_travel_time = df['Trip Duration'].mean()
    print('\nThe mean travel time is: {} seconds.'.format(mean_travel_time))# TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types_count = df['User Type'].value_counts()
    print('\nUser types counts are : {}.'.format(user_types_count))# TO DO: Display counts of user types
    
    while True:
        try:
            gender_count = df['Gender'].value_counts(dropna=False)
            print('\nVarious gender counts are : {}.'.format(gender_count))# TO DO: Display counts of gender
            most_common_yob = df['Birth Year'].mode()[0]
            earliest_yob = df['Birth Year'].min()
            most_recent_yob = df['Birth Year'].iloc[0]
            print('\n The earliest year of birth is {}, the most recent year of birth is {} and the most common year of birth is {}.'.format(earliest_yob,most_recent_yob,most_common_yob))# TO DO: Display earliest, most recent, and most common year of birth
            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)
            break
        except:
            print('\nNo Gender and Birth year data for this month')
            break
    
def display_data_request(df):
    """Displays user request on bikeshare data statistics."""
    
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while (view_data != 'no'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data_request(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
