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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        city = input('Which city would you like to analyze (chicago, new york city, washington)  ')
        if city not in CITY_DATA.keys():
            print("Sorry, your ansewer is invalid.")
            continue
        else:
            break
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Which month to filter the data by? (all, january, february, ... , june)  ')
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which day of week to filter by? (all, monday, tuesday, ... sunday)  ')
    
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
    df = pd.read_csv(f'./data/{CITY_DATA[city]}')
    df.drop('Unnamed: 0',axis=1,inplace=True)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day'] = df['Start Time'].dt.day_name().str.lower()
    
    if month != 'all' and day != 'all':
        df = df[ (df['month'] == month) & (df['day'] == day)]
        return df
    elif month != 'all' and day == 'all':
        df = df[ (df['month'] == month)]
        return df
    elif day != 'all' and month == 'all':
        df = df[ (df['day'] == day)]
        return df
    else:
        return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].value_counts().index[0]
    print(f'the most common month is {common_month}')
    # TO DO: display the most common day of week
    common_day = df['day'].value_counts().index[0]
    print(f'the most common day is {common_day}')
    # TO DO: display the most common start hour
    common_hour = df['Start Time'].dt.hour.value_counts().index[0]
    print(f'the most common hour (24hr format) is {common_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_StartStation = df['Start Station'].value_counts().index[0]
    print(f'the most common start station is {common_StartStation}')
    
    # TO DO: display most commonly used end station
    common_EndStation = df['End Station'].value_counts().index[0]
    print(f'the most common start station is {common_EndStation}')

    # TO DO: display most frequent combination of start station and end station trip
    common_combined = pd.melt(df[['Start Station','End Station']])['value'].value_counts().index[0]
    print(f'most frequent combination of start station and end station trip is {common_EndStation}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print(f'total Travel time = {total_travel} seconds')

    # TO DO: display mean travel time
    mean = df['Trip Duration'].mean()
    print(f'Travel time average = {mean} seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts().to_dict()
    print('Type\t\tCounts')
    print('-'*40)
    for user,count in user_types.items():
        print(f'{user}\t{count}')
        
    print()
    print()
    
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        user_gender = df['Gender'].value_counts().to_dict()
        print('Gender\t\tCounts')
        print('-'*40)
        for gender,count in user_gender.items():
            print(f'{gender}\t\t{count}')
    else:
        print('There is no gender feature in the dataframe')
    
    
    print()
    print()
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = int(df['Birth Year'].nsmallest(1).values[0])
        recent = int(df['Birth Year'].nlargest(1).values[0])
        common = int(df['Birth Year'].value_counts().index[0])

        print(f'Earliest year of birth is {earliest}')
        print(f'Most recent year of birth is {recent}')
        print(f'Most common year of birth is {common}')
    
    else:
        print('There is no Birth Year feature in the dataframe')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()