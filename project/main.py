import sys
from os import system
import pandas as pd
from reporting import *
from monitoring import *
from intelligence import *



def main_menu():
    """
    This function will be executed at the start of the program, it will show the main menu of the program allowing the user to navigate through the different options
    Variables:
        choice -> helps to choose the fucntoin
    Returns:
        Function Chosen by user"""

    while True:
        print("R - Access the PR module")
        print("I - Access the MI module")
        print("M - Access the RM module")
        print("A - Print the About text")
        print("Q - Quit the application")

        
        choice = input('Enter Your Choice\n : ')
        if choice.upper() == 'Q':
            quit()
        elif choice.upper() == 'R':
            reporting_menu()
        elif choice.upper() == 'I':
            intelligence_menu()
        elif choice.upper() == 'M':
            monitoring_menu()
        elif choice.upper() == 'A':
            about()
        else:
            return "error try again"


def reporting_menu():
    """
    This function will be executed when the user chooses the 'R' option in the main menu.
    The user can choose between different options to perform tasks for the PR module.
        Variables:
            choice -> helps to choose the fucntoin
        Returns:
            an array as per the analyses chosen by the user
    """

    while True:
        print("1 - Get Daily Average")
        print("2 - Get Daily Median")
        print("3 - Get Hourly Average")
        print("4 - Get Monthly Average")
        print("5 - Get the Hour with the Higihest Pollutant Level on a Particular Day")
        print("6 - Count the Missing Data")
        print("7 - Replace the Missing Data")
        print("0 - Go Back")
        print()
        
        choice = int(input('Enter Your Choice: '))
        if choice == 0:
            main_menu()
        elif choice == 1:
            data = pd.DataFrame()
            monitoring_station = input("enter 'h' for Harlington \nenter 'm' for Marylebone Road \nenter 'k' for Kensington: ")
            pollutant = input("enter any one pollutant given below\nNO or PM10 or PM25\n: ")
            print(daily_average(data, monitoring_station, pollutant))
        elif choice == 2:
            data = pd.DataFrame()
            monitoring_station = input("enter 'h' for Harlington \nenter 'm' for Marylebone Road \nenter 'k' for Kensington: ")
            pollutant = input("enter any one pollutant given below\nNO or PM10 or PM25\n: ")
            print(daily_median(data, monitoring_station, pollutant))
        elif choice == 3:
            data = pd.DataFrame()
            monitoring_station = input("enter 'h' for Harlington \nenter 'm' for Marylebone Road \nenter 'k' for Kensington: ")
            pollutant = input("enter any one pollutant given below\nNO or PM10 or PM25\n: ")
            print(hourly_average(data, monitoring_station, pollutant))
        elif choice == 4:
            data = pd.DataFrame()
            monitoring_station = input("enter 'h' for Harlington \nenter 'm' for Marylebone Road \nenter 'k' for Kensington: ")
            pollutant = input("enter any one pollutant given below\nNO or PM10 or PM25\n: ")
            print(monthly_average(data, monitoring_station, pollutant))
        elif choice == 5:
            data = pd.DataFrame()
            date = input("Enter the Date in the YYYY-MM-DD format: ")
            monitoring_station = input("enter 'h' for Harlington \nenter 'm' for Marylebone Road \nenter 'k' for Kensington: ")
            pollutant = input("enter any one pollutant given below\nNO or PM10 or PM25\n: ")
            print(peak_hour_date(data, date, monitoring_station, pollutant))
        elif choice == 6:
            data = pd.DataFrame()
            monitoring_station = input("enter 'h' for Harlington \nenter 'm' for Marylebone Road \nenter 'k' for Kensington: ")
            pollutant = input("Choose the Pollutant\nNO or PM10 or PM25\nEnter: ")
            print(count_missing_data(data,  monitoring_station, pollutant))
        elif choice == 7:
            data = pd.DataFrame()
            new_value = input("Enter the value you want to replace 'No data' with: ")
            monitoring_station = input("enter 'h' for Harlington \nenter 'm' for Marylebone Road \nenter 'k' for Kensington: ")
            pollutant = input("Choose the Pollutant\nNO or PM10 or PM25\nEnter: ")
            print(fill_missing_data(data, new_value,  monitoring_station, pollutant))
        else:
            return "Invalid Input"

        input("\nPress Enter To Continue....")







def monitoring_menu():
    """
    This function will be executed when the user chooses the 'R' option in the main menu.
    The user can choose between different options to perform tasks for the RM module.

   Variables:
        SpeciesNeeded/SiteNeeded/FunctionNeeded: all values in RM module to find chosen variables from user

    Returns:
        Functions Chosen by user
    """
    
    
    Options = [average_all_values, median_of_values,
               bar_chart_of_values, range_of_values_week, selected_days]
    # lists all options of functions inside RM file
    print("Options: ")  # print options
    for i in range(len(Options)):
        # print each function and number corrosponding to function
        print(i, Options[i].__name__)
    FunctionNeeded = int(input("enter your choice: "))
    print("Sites: \n")
    for i in range(len(list_of_sites)):
        print(i, list_of_sites[i])  # find site user wants
    SiteNeeded = int(input("What Site do you want"))
    print("Species: \n")  # find species user wants
    for i in range(len(list_of_species)):
        print(i, list_of_species[i])
    SpeciesNeeded = int(input("choice your species"))

    # look at each function the user has chosen and print with the specific site and species listed
    if FunctionNeeded == 0:
        print(average_all_values(
            list_of_sites[SiteNeeded], list_of_species[SpeciesNeeded]))
    if FunctionNeeded == 1:
        print(median_of_values(
            list_of_sites[SiteNeeded], list_of_species[SpeciesNeeded]))
    if FunctionNeeded == 2:
        print(bar_chart_of_values(
            list_of_sites[SiteNeeded], list_of_species[SpeciesNeeded]))
    if FunctionNeeded == 3:
        print(range_of_values_week(
            list_of_sites[SiteNeeded], list_of_species[SpeciesNeeded]))

    if FunctionNeeded == 4:  # is the user chosen range of values-week, then they can choose 2 specific days
        StartDate = input("Please enter date of start in format (YYYY-MM-DD)")
        EndDate = input("Please enter date of end in format (YYYY-MM-DD)")
        assert len(StartDate) == 10  # make sure startDate has 10 characters

        print(selected_days(
            list_of_sites[SiteNeeded], list_of_species[SpeciesNeeded], StartDate, EndDate))
    input("Press Enter key to continue...\n")
    
    


def intelligence_menu():
    """
    This function will be executed when the user chooses the 'I' option in the main menu.
    The user can choose between different options to perform tasks for the MI module.

   Variables:
        choice -> helps choose the fucntoin

    Returns:
        creates a new image as per the user's choice    
   """
    
    
    while True:
        print('1: Find red pixels')
        print('2: Find cyan pixels')
        print('0: Go Back')
        choice = input("Enter your choice: ")
        if choice == '0':
            main_menu()
        elif choice == '1':
            find_red_pixels()
        elif choice == '2':
            find_cyan_pixels()
        else:
            return "Invalid Input"
        input("Press Enter key to continue...\n")
        
    
    

def about():
    """
    This function will be executed when the user chooses the 'A' option in the main menu.

    Variables:
        Module -> it stores the module code
        Candidate_No -> it stores the candidate number of the creater of this program

    Returns:
        formated string with the module code and candidate number
    """
    
    Module = "ECM1400"
    Candidate_No = "245524"
    print(f'Module Code:{Module} Candidate Number: ,{Candidate_No}')
    input("Press Enter key to continue...\n")
    

    


def quit():
    """This function will be executed when the user chooses the 'Q' option in the main menu.
    It should terminate the program"""
    sys.exit()
    











print(main_menu())