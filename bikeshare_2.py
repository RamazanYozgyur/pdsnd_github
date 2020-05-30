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
    city=input("Hello which city among Chicago, New York City and Washington do you want to choose to explore \n").lower()
    while city.lower() not in ("chicago" ,"new york city","washington") :
                   
         city=input("You make mistakes please write again city  among chicago, new york city and washington  \n").lower()


             

    # TO DO: get user input for month (all, january, february, ... , june)
    month=input("Which month do you  want to check amoung January, February, ...., June \n").title()
    while month not in ("January","February","March","April","May","June"):
        month=input("You make mistakes please write month again among January, February, ...., June \n").title()
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("Which weekdays do you  want to check among monday, tuesday, ... sunday \n").title()
    while day not in ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"):
        day=input("You make mistakes please write your day again amoung monday, tuesday, ... sunday \n").title()      
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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] =pd.to_datetime(df['Start Time']) 

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour']= df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df =  df.loc[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df =  df.loc[df['day_of_week']==day.title()]
    
    return df
    



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is {}".format(df["month"].mode()[0]))

    # TO DO: display the most common day of week
    print("The most common day of week is " + df["day_of_week"].mode()[0])

    # TO DO: display the most common start hour
    print("The most common start hour {}".format(df["hour"].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most commonly used start station is {}".format(df["Start Station"].mode()[0]))

    # TO DO: display most commonly used end station
    print("Most commonly used end station is {}".format(df["End Station"].mode()[0]))


    # TO DO: display most frequent combination of start station and end station trip
    print("most frequent combination of start station and end station trip is {} ".format(df.groupby(["Start Station","End Station"]).size().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("total travel time  is " + str(df["Trip Duration"].sum(skipna=True)) + " minutes" )

    # TO DO: display mean travel time
    print("mean travel time is " + str(int(df["Trip Duration"].mean(skipna=True))) + " minutes" )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("In total we have {} users".format(str(df["User Type"].count())))
    print("These are different user types and numbers of them in total \n " + str(df.groupby("User Type")["User Type"].count()))         

    # TO DO: Display counts of gender
    try:
        
       print("We have genders and you can see  their numbers below \n {}".format(str(df.groupby("Gender")["Gender"].count())))
    except:
        print("There is no Gender column in Washington.csv")
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        
    
       print("Earliest year of birth among user is {} and most recent date is {}. We can also see that most common year of birth is {} ".format(int(df["Birth Year"].min(skipna= True)),int(df["Birth Year"].max(skipna= True)),int(df["Birth Year"].mode()[0])))
    except:
        print("There is no Birth Year column in Washington.csv")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_data_function(df):
    answer=input("Do you want to see raw data? Yes or No ").lower()
    if answer not in ("yes","no"):
        print("Please answer correctly. Yes or No. ") 
    
    k=5          
    while answer == "yes":
        print(df.head(k))
        answer=input("Do you want to see more raw data? Yes or No ").lower()
        k+=5     
    print('-'*40)
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data_function(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

