import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str)  - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("please choose one of these city names chicago, new york city or washington: ").lower() 
    while True:
        if city == 'chicago' or city == 'new york city' or city == 'washington':
            break
        else:
            city = input("Sorry, the name you entered is not right. Please enter again:").lower() 
    #ask user if they want to filter date by date or not    
    x = input("do you want to filter data by month, day, both, or not at all: ").lower()
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    weekDays = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday",'all']
    while True:
        if x == 'both':
            # get user input for month (all, january, february, ... , june)
            month = input("please enter the name of the month:january, february, ... , june or all: ").lower()
            while True:
                if month in months:
                    break
                else:
                    month = input("Sorry, the month name you entered is not right. Please enter again:").lower()
            # get user input for day of week (all, monday, tuesday, ... sunday)
            day = input("please enter the name of the day: sunday, monday, ... , saturday or all: ").lower()
            while True: 
                if day in weekDays:
                    break
                else:
                    day = input("Sorry, the day name you entered is not right. Please enter again: ").lower()
            break            
        # get user input for month only(all, january, february, ... , june)
        elif x=='month':
            day = 'all'
            month = input("please enter the name of the month:january, february, ... , june or all: ").lower()
            while True:
               if month in months:
                   break
               else:
                   month = input("Sorry, the month name you entered is not right. Please enter again:").lower()
            break
        #get user input for day of week only(all, monday, tuesday, ... sunday)
        elif x=='day':
            month = 'all'
            day = input("please enter the name of the day: sunday, monday, ... , satarday or all: ").lower()
            while True: 
                if day in weekDays:
                    break
                else:
                    day = input("Sorry, the day name you entered is not right. Please enter again: ").lower()
            break
        elif x=='not at all':
            month = 'all'
            day = 'all'
            break
        else:
            x=input("Sorry, the option you entered is not right. Please enter again: ").lower()
            
            
    print('-'*40,'\n')
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] =  pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday

    #filter by month if applicable
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_name = months.index(month)+1
        df = df[df['month'] == month_name]


    #filter by day if applicable:
    
    if day != 'all':
        weekDays = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
        weekday= weekDays.index(day)
        df = df[df['day'] == weekday]

  
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    months=df['month'].unique().tolist()
    days=df['day'].unique().tolist()
    
    # display the most common month  
    if len(months)>1:
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        popular_month_num = df['month'].mode()[0]
        popular_month= months[popular_month_num - 1]
        print('{} is the most common month during the year'.format(popular_month))
        
        
        # display the most common day of week
    if len(days)>1:
        weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        popular_day_number = df['day'].mode()[0]
        popular_day = weekDays[popular_day_number]
        print('{} is the most common day during the week'.format(popular_day))
    

    # display the most common start hour
    df['hour'] =df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('{} is the most common houre during the day'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40,'\n')


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_startstation =df['Start Station'].mode()[0]
    print('the most popular start station here is: ', popular_startstation)

    # display most commonly used end station
    popular_endstation =df['End Station'].mode()[0]
    print('the most popular end station here is: ', popular_endstation)


    # display most frequent combination of start station and end station trip
    
    df['combination_station'] = df['Start Station']+' - '+ df['End Station']
    popular_startendstation =df['combination_station'].mode()[0]
    print('the most popular frequent combination between start and end station here is: ', popular_startendstation)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print(f'the total of travel time for all users: {df["Trip Duration"].sum()}seconds\n')

    # display mean travel time
    print(f'the mean of travel time for all users: {df["Trip Duration"].mean()}seconds\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40,'\n')


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('the number of user based on thier type is: \n',df.groupby(['User Type'])['User Type'].count(),'\n')

    # Display counts of gender
    if 'Gender' in df.columns:
        print('the number of user based on thier gender is: \n',df.groupby(['Gender'])['Gender'].count(),'\n')
    
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        recent_year = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print('the earliest year of birth for user is: ',earliest_year)
        print('the most recent of birth for user is: ',recent_year)
        print('the most recent of birth for user is: ',common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40,'\n')

def display_user_data(df):
        
            df_lengh = len(df)
            for i in range(0,df_lengh,5):
                y =  input("Do you want to check more 5 users data? if yes please print yes else print no: ").lower()
                if y == 'yes':
                    usersdata = df.iloc[i:i+5]
                    print(usersdata)
                else:
                    break
            
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_user_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
