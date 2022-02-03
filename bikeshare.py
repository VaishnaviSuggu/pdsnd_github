import datetime as dt
import time
import pandas as pd
import numpy as np

CITY_DATA = { '1': 'chicago.csv',
              '2': 'new_york_city.csv',
              '3': 'washington.csv' }

def get_filters():
    global city, month, day,filters,days
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    days = ["days","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    city = input("Select the city you want the data for: \n Enter - \n 1 for chicago \n 2 for new york city \n 3 for washington : ")
    while city not in CITY_DATA.keys():
        city = input("OOPS! Wrong Input...- Enter - \n 1 for chicago \n 2 for new york city \n 3 for washington : ")
    
    filters = input(" Would you like to filter by 'month','day','both' or 'none' ?")
    while filters.lower() not in ['month','day','both','none']:
        filters = input("OOPS! Wrong Input..Select either 'month','day','both' or 'none' ")
    # TO DO: get user input for month (all, january, february, ... , june)
    filters = filters.lower()
    if filters == "month":
        month = input("Choose a month between January and June as an integer. (eg. Jan = 1) :")
        while month.lower() not in ['1','2','3','4','5','6']:
            month = input("OOPS! Wrong Input..\n Choose a month between January and June as an integer. (eg. Jan = 1) :")
            
    elif filters == "day": 
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = input("Select a day as an integer (eg. sunday = 1) : ")
        while int(day) not in range(1,8):
            day = input("OOPS! Wrong Input..\n Select a day as an integer (eg. sunday = 1) : ")
        
    elif filters == "both":
        month = input("Choose a month between January and June as an integer. (eg. Jan = 1) :")
        while month.lower() not in ['1','2','3','4','5','6','all']:
            month = input("OOPS! Wrong Input..\n Choose a month between January and June as an integer (eg. Jan = 1)  :")
        day = input("Select a day as an integer (eg. sunday = 1) : ")
        while int(day) not in range(1,8):
            day = input("OOPS! Wrong Input..\n Select a day as an integer (eg. sunday = 1) : ")

    print('-'*40)
    


def load_data():
    global df_raw
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
    df_raw = df
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df['Month'] = df["Start Time"].dt.month
    df["Week day"] = df["Start Time"].dt.weekday_name
    df['Hour'] = df['Start Time'].dt.hour
    df['Trip']= [(df['Start Station'][i], df['End Station'][i]) for i in range(len(df))]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    if filters=="none":
        start_time = time.time()
        # TO DO: display the most common month
        print("Most common month is ",df['Month'].value_counts().index[0])

        # TO DO: display the most common day of week
        print("Most commom day of week is ", df["Week day"].value_counts().index[0])
        # TO DO: display the most common start hour
        
        print("Most commom start hour is ", df["Hour"].value_counts().index[0])
        
    elif filters=="month": 
        start_time = time.time()
        df1 = df[df['Month']==int(month)] 
        print("Most commom day of week is ", df1["Week day"].value_counts().index[0])
        # TO DO: display the most common start hour
        print("Most commom start hour is ", df1["Hour"].value_counts().index[0])
    
    elif filters == "day": 
        start_time = time.time()
        df1 = df[df['Week day']==days[int(day)]]
        print("Most commom start hour is ", df1["Hour"].value_counts().index[0])
        
    elif filters == 'both':
        start_time = time.time()
        df1 = df[(df['Month'] == int(month)) & (df['Week day']== days[int(day)])]
        print("Most commom start hour is ", df1["Hour"].value_counts().index[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most commonly used start station is ",df['Start Station'].value_counts().index[0])

    # TO DO: display most commonly used end station
    print("Most commonly used end station is ",df['End Station'].value_counts().index[0])

    # TO DO: display most frequent combination of start station and end station trip
    
    print("Most frequent combination of start and end station is ",df['Trip'].value_counts().index[0])
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time = ", df["Trip Duration"].sum(), "seconds")

    # TO DO: display mean travel time
    print("Mean travel time = ", (df["Trip Duration"].sum())/(len(df["Trip Duration"])), "seconds")
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types :\n","Subscribers = ",(df['User Type']=="Subscriber").sum(),"\n Customers =", (df['User Type']=="Customer").sum()) 
    
    if city == '1' or city == '2':
    # TO DO: Display counts of gender
        print("Counts of gender :\n","Male = ", (df["Gender"]=="Male").sum(),"\n Female = ",(df["Gender"]=="Female").sum())

        # TO DO: Display earliest, most recent, and most common year of birth
        print("Earliest year of birth =", df['Birth Year'].min())
        print("Most recent year of birth =", df['Birth Year'].max())
        print("Most common year of birth =", df['Birth Year'].value_counts().index[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    global city,month,day
    while True:
        get_filters()
        print("Preparing statistics....")
        df = load_data()

        time_stats(df)
        
        if filters == "none":
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
        elif filters == "month":
            df1 = df[df['Month'] == int(month)]
            station_stats(df1)
            trip_duration_stats(df1)
            user_stats(df1)
        elif filters == "day":
            df1 = df[df['Week day']==days[int(day)]]
            station_stats(df1)
            trip_duration_stats(df1)
            user_stats(df1)
        elif filters == "both":
            df1 = df[(df['Month'] == int(month)) & (df['Week day']== days[int(day)])]
            station_stats(df1)
            trip_duration_stats(df1)
            user_stats(df1)

        restart = input("\n Would you like to restart? Enter 'yes' or 'no'.\n")
        while restart.lower() not in ["yes","no"]:
            restart = input("\n Invalid Input!! Would you like to restart? Enter 'yes' or 'no'.")
        
        row=0
        if restart.lower() != 'yes':
            while True :
                if row == 0:
                    raw_data = input("\n Would you like to view the raw data? Enter yes or no : ")
                    while raw_data.lower() not in ["yes","no"]:
                        raw_data = input("\n Invalid Input !! Would you like to view the raw data? Enter yes or no : ")
                    
                else:
                    raw_data = input("\n Would you like to view the next 5 rows in the raw data? Enter yes or no :")
                    while raw_data.lower() not in ["yes","no"]:
                        raw_data = input("\n Invalid Input!! Would you like to view the raw data? Enter yes or no : ")
                    
                if raw_data.lower() != 'yes':
                    break
                else:
                    print(df_raw[row:row+5])
                    row+=5
                    if row == len(df_raw)-1:
                        print("End of Data")
                        break
            break
            
            
# Run this for the output

if __name__ == "__main__":
	main()

