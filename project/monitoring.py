import requests
import pandas
import datetime


list_of_species= ['NO', 'NO2', 'O3', 'CO', 'SO2', 'PM10', 'PM25']
list_of_sites = ['MY1', 'BG1', 'BG2', 'CT2', 'CT3']

def average_all_values(site_code,species_code,start_date=None,end_date=None):
    """
    This function uses requests to gather data for the current date and find the average
    The data is gathered from the specific Species and Site the user has chosen
    Uses Current Date so will most likely not contain 24 values
    
    Parameters:
        Site_code/Species_code: input from user for certain code they want
        start/end_date: current date from 00:00 until 00:00 the next day
    Variables:    
        endpoint: uses requests to gather data from API
        url: uses inputs to find url with specific codes
        CheckRequests: check if request can be found or not and stops function if not found
        result: uses res and df to find all items found
        AllValues: finds all data values that I can use for these functions(List)
        NumOfValues/CountingSum: used to find total count and number of variables to find average
    Returns: 
        Average: Number found as average from list
    """
    
    # start date finds current date
    # end date finds current date + 1 day to find next day
    start_date = datetime.date.today() if start_date is None else start_date
    end_date = start_date + datetime.timedelta(days=1) if end_date is None else end_date
    
    
    # find url of API with codes to be used by user
    endpoint = "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json"
   
    # url uses user input to put into the endpoint
    url = endpoint.format(
        site_code = site_code,
        species_code = species_code,
        start_date = start_date,
        end_date = end_date
    )

    # try the check request to find status
    try:
        CheckRequest = requests.get(url,timeout=1)
        CheckRequest.raise_for_status()
    except:
        pass
    # if the check is not found, or the website link doesnt work then return null
    if CheckRequest.status_code != 200:
        print("Website Error: ", url, CheckRequest)
        return "Please try different Site/Species Code"


    # find request as json, transform into dataframe using pandas 
    res = requests.get(url).json()
    df = pandas.DataFrame(res)
    df  = (df.iloc[2]) # only need 3rd key and values
    result = df.item() # dataframe of only values and time 
    
    
    AllValues = []
    for element in result:
        if element['@Value'] != '': # make sure there are no empty elements
            AllValues.append((element['@Value'])) # add elements to list

    #print(AllValues)
    CountingSum = 0 # total of all values
    NumOfValues = 0 # num of values in list
    for i in AllValues:
        NumOfValues += 1
        CountingSum += float(i)

    if NumOfValues != 0: # if the total isnt 0, so if list is not empty
        Average = CountingSum/NumOfValues
    
        return Average

    else:
        return "No Result Found" # return this if no values found

#print(average_all_values("MY1", "NO"))


def median_of_values(site_code,species_code,start_date=None,end_date=None):
    """
    This function uses requests to gather data for the current date and find the median
    The data is gathered from the specific Species and Site the user has chosen
    Uses Current Date so will most likely not contain 24 values
    
    Parameters:
        Site_code/Species_code: input from user for certain code they want
        start/end_date: current date from 00:00 until 00:00 the next day
    Variables:    
        endpoint: uses requests to gather data from API
        url: uses inputs to find url with specific codes
        CheckRequests: check if request can be found or not and stops function if not found
        result: uses res and df to find all items found
        AllValues: finds all data values that I can use for these functions(List)
        SortedList: List of all values sorted from least to most
        MedianIndex: Index of median value found in sorted list
    Returns: 
        Median: Number found as median from list
    """
    
    # start date finds current date
    # end date finds current date + 1 day to find next day
    start_date = datetime.date.today() if start_date is None else start_date
    end_date = start_date + datetime.timedelta(days=1) if end_date is None else end_date
    
    
    # find url of API with codes to be used by user
    endpoint = "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json"
   
    # url uses user input to put into the endpoint
    url = endpoint.format(
        site_code = site_code,
        species_code = species_code,
        start_date = start_date,
        end_date = end_date
    )

    # try the check request to find status
    try:
        CheckRequest = requests.get(url,timeout=1)
        CheckRequest.raise_for_status()
    except:
        pass
    # if the check is not found, or the website link doesnt work then return null
    if CheckRequest.status_code != 200:
        print("Website Error: ", url, CheckRequest)
        return "Please try different Site/Species Code"


    # find request as json, transform into dataframe using pandas 
    res = requests.get(url).json()
    df = pandas.DataFrame(res)
    df  = (df.iloc[2]) # only need 3rd key and values
    result = df.item() # dataframe of only values and time 
    
    
    AllValues = []
    for element in result:
        if element['@Value'] != '': # make sure there are no empty elements
            AllValues.append((element['@Value'])) # add elements to list

    print(AllValues)
    # List is made to be returned at the end
    
    Median = 0
    # Simple insertion sort to sort array to find median
    for i in range(1, len(AllValues)):
        test = AllValues[i]
        # test value looks at each value
        i2 = i-1
        # i2 value is value before test value
        while test < AllValues[i2] and i2 >= 0:
            # check if value should be ahead (greater) of current test value
                AllValues[i2+1] = AllValues[i2]
                i2 = i2 - 1
        #check next value           
        AllValues[i2+1] = test    



    # if count MOD 2 = 1 then length of list is uneven
    if len(AllValues) % 2 == 1:
        MedianIndex = int(len(AllValues) / 2)
        # list is uneven, middle value is median
        Median = AllValues[MedianIndex]

    # if not uneven then list is even
    else:
        # need to find 2 values as list is even
        # find index of middle value and middle value - 1 
        MedianIndex1 = int(len(AllValues) / 2) - 1
        MedianIndex2 = int(len(AllValues) / 2) 
        # for even list, add 2 values and /2 to find median
        Median = (float(AllValues[MedianIndex1]) + float(AllValues[MedianIndex2]))/2
        # round to 4 dp
        Median = round(Median,4)
        

    return Median



#print(median_of_values("MY1", "NO"))

def bar_chart_of_values(site_code,species_code,start_date=None,end_date=None):
    """
    This function uses requests to gather data for the current date and use data to plot a bar graph
    The data is gathered from the specific Species and Site the user has chosen
    Uses Current Date so will most likely not contain 24 values
    Uses TURTLE - found in python standard library
    Parameters:
        Site_code/Species_code: input from user for certain code they want
        start/end_date: current date from 00:00 until 00:00 the next day
    Variables:    
        endpoint: uses requests to gather data from API
        url: uses inputs to find url with specific codes
        CheckRequests: check if request can be found or not and stops function if not found
        result: uses res and df to find all items found
        AllValues: finds all data values that I can use for these functions(List)
        ListOfFloats: List containing all values needed
        wn: the window needed to show the graph
    Returns: 
        wn: window showing the barchart
    
    
    """

    import turtle # turtle will be needed to represent the data
    # start/end date is current date from 00:00 to 24:00
    start_date = datetime.date.today() if start_date is None else start_date
    end_date = start_date + datetime.timedelta(days=1) if end_date is None else end_date
    
    # url of website needed for API
    endpoint = "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json"
    # url uses code input from user to find data
    url = endpoint.format(
        site_code = site_code,
        species_code = species_code,
        start_date = start_date,
        end_date = end_date
    )


    # check if the request works 
    try:
        r = requests.get(url,timeout=1)
        r.raise_for_status()
    except:
        pass
    if r.status_code != 200: # if it doesnt work then function is ended
        print ("Website Error: ", url, r)
        return "Please try different Site/Species Code"
    
    # use json to get request of data, turn to dataframe to find 3rd key and value(list)
    res = requests.get(url).json()
    df = pandas.DataFrame(res)
    df  = (df.iloc[2])
    result = df.item()
    
    # add values to list unless value is empty
    AllValues = []
    for element in result:
        if element['@Value'] != '':
            AllValues.append((element['@Value']))

    
    
    


    ListOfFloats = []
    for i in AllValues:
        i = float(i)
        ListOfFloats.append(i)
        # add float values to list

    maxheight = max(ListOfFloats) # find max height of list
    numbers = len(ListOfFloats) # find len of list to see how many bars to make
    border = 10 # atleast 10 pixels inbetween the barchart and border of window
    wn = turtle.Screen() # create window  
    wn.setworldcoordinates(0 - border, 0 - border, 45 * numbers + border, maxheight + border) # set up border, 45*numbers to make the bars big

    def drawBar(t, height, color):
        # draw height using turtle 
        t.fillcolor(color)
        t.speed(10)
        t.begin_fill() 
        t.down()            
        t.left(90)
        t.forward(height)
        t.write(str(height)) # write height of bar on top of bar
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(height)
        t.left(90)
        t.end_fill()
        t.up()

    pen = turtle.Turtle()  
    wn. bgcolor("grey")  # grey background      
    pen.pensize(3) # size 3 pen to make size slightly big
    

    for i in range(len(ListOfFloats)):
        drawBar(pen, ListOfFloats[i], "cyan") # for each bar, draw it and colour it cyan

    # this is to add in information of barchart
    xpos = (45*numbers/3) # x position of text
    pen.setpos(xpos,-5) # set xpos -5 to make it fit in
    style = ('Arial', 15, 'italic') # font and size of text
    
    pen.write(("Site is", site_code, "Species is: ", species_code ), font=style )

    
    wn.exitonclick()

ListOfSpecies= ['NO', 'NO2', 'O3', 'CO', 'SO2', 'PM10', 'PM25']
#print(bar_chart_of_values("MY1", "NO"))


def range_of_values_week(site_code,species_code,start_date=None,end_date=None):
    """
    This function uses requests to gather data for the current date and find the range of values
    The data is gathered from the specific Species and Site the user has chosen
    Range is calculated from finding max and min value per day
    Uses Current Date so will most likely not contain 24 values for first day
    Will return 7 ranges for ranges per day for the past week
    
    Parameters:
        Site_code/Species_code: input from user for certain code they want
        start/end_date: current date from 00:00 until 00:00 the next day
    Variables:    
        endpoint: uses requests to gather data from API
        url: uses inputs to find url with specific codes
        CheckRequests: check if request can be found or not and stops function if not found
        result: uses res and df to find all items found
        AllValues: finds all data values that I can use for these functions(List)
        Min/Max value: used to find max/min value from list
        DayRange: used to find range per day
    Returns: 
        WeekRange: List of range per day for the whole week
    
    """

    # find all days for the past week
    ListOfDays = []
    WeekRangeList = [] # use list to find the week range
    for currentdate in range(8): # range of 8 (7 days)
        if currentdate == 0: # find current date
            start_date = datetime.date.today() if start_date is None else start_date
            end_date = start_date + datetime.timedelta(days=1) if end_date is None else end_date
            print(start_date)
            ListOfDays.append(start_date) # add current date to listofdays
            currentdate += 1
            

        else: # find the past 6 days from today
            start_date = datetime.date.today() - datetime.timedelta(days=currentdate) # start at 00:00 from previous day
            end_date = start_date + datetime.timedelta(days=1) # end at 00:00 next day
            print(start_date)
            ListOfDays.append(start_date)
            currentdate += 1
    
        # find url of API
        endpoint = "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json"
        # codes are used from user input to find data
        url = endpoint.format(
            site_code = site_code,
            species_code = species_code,
            start_date = start_date,
            end_date = end_date
        )

        # check if request works and outputs data
        try:
            r = requests.get(url,timeout=1)
            r.raise_for_status()
        except:
            pass
        if r.status_code != 200:
            print ("Website Error: ", url, r) # if not then there is a problem as not every site takes data for every species
            return "Please try different Site/Species Code"


        # use json to find request data
        res = requests.get(url).json()
        df = pandas.DataFrame(res)
        df  = (df.iloc[2])
        result = df.item()
        # make dataframe and only find 3rd key and value
        
        AllValues = []
        for element in result:
            if element['@Value'] != '':
                AllValues.append((element['@Value']))

        ListOfFloat = []
        for i in AllValues:
            i = float(i)
            ListOfFloat.append(i)
        # make list of all data as float
        
        # find max and min value using simple for loops and comparisons
        MaxValue = 0
        MinValue = 9999999
        for i in ListOfFloat:
            if i > MaxValue:
                MaxValue = i
            if i < MinValue:
                MinValue = i

        # find the max/min in data to find time corrosponding to max/min
        for element in result:
            if element['@Value'] == str(MaxValue):
                MaxDate = (element['@MeasurementDateGMT']) 
        for element in result:
            if element['@Value'] == str(MinValue):
                MinDate = (element['@MeasurementDateGMT']) 
        
        print ("Min value: ", MinValue, "Min date: ", MinDate)
        print ("Max value: ", MaxValue, "Max date: ", MaxDate)
        DayRange = MaxValue-MinValue
        # find range by max - min
        print("DAY RANGE: ", DayRange)
        WeekRangeList.append(DayRange)
        # add daily range to week range
    

    return (WeekRangeList)   

#print(range_of_values_week("MY1", "NO"))


def selected_days(site_code,species_code,start_date,end_date):
    """
    This function uses requests to gather data for the current date
    This will output a calculation, but the user can specify the output
    The output can be either Range/MaxValue/MinValue/AverageValue
    The data is gathered from the specific Species and Site the user has chosen
    Range is calculated from finding max and min value per day
    Uses Current Date so will most likely not contain 24 values for current date
    Will return multiple ranges for ranges per day for given range of days
    
    Parameters:
        Site_code/Species_code: input from user for certain code they want
        start/end_date: gets date from user and finds date from 00:00 until 00:00 using end date
    Variables:    
        endpoint: uses requests to gather data from API
        url: uses inputs to find url with specific codes
        CheckRequests: check if request can be found or not and stops function if not found
        result: uses res and df to find all items found
        AllValues: finds all data values that I can use for these functions(List)
        Picked: find which option the user has picked
        Max/Min value: used for calculation for first 3 outputs
        NumOfValues/CountingSum: used to find average by counting num of data and total
    Returns: 
        Option of Returning: Range/MaxValue/MinValue/AverageValue from data given
    """
    

    
    YearPicked = (start_date[:4]) # find year by first 4 characters of data
    MonthPicked = (start_date[5:7]) # month is next 2 int characters, after the "-"
    DayPicked = (start_date[8:10]) # day is next 2 characters, after the "-"
    # DATA IS GIVEN BY: year - month - day
    start_date = datetime.datetime(int(YearPicked), int(MonthPicked), int(DayPicked)) if start_date is None else start_date
    end_date = datetime.datetime(int(YearPicked), int(MonthPicked), int(DayPicked)+1) if end_date is None else end_date
    #print(start_date)
    #print(end_date)
    
    
    # find url of API
    endpoint = "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json"
    # use user inputs to use codes for API
    url = endpoint.format(
        site_code = site_code,
        species_code = species_code,
        start_date = start_date,
        end_date = end_date
    )

    # check if requests works
    try:
        r = requests.get(url,timeout=1)
        r.raise_for_status()
    except:
        pass
    if r.status_code != 200: # if doesnt work then function is ended
        print ("Website Error: ", url, r)
        return "Please try different Site/Species Code"


    # use json to find data and add to dataframe
    res = requests.get(url).json()
    df = pandas.DataFrame(res)
    df  = (df.iloc[2]) # only need 3rd key and value from dataframe
    result = df.item()
    
    # make list of all values from dataframe that are not empty
    AllValues = []
    for element in result:
        if element['@Value'] != '':
            AllValues.append((element['@Value']))
    #print(AllValues)


    # 4 options, boolean used to see which option is picked
    MaxPicked = False
    MinPicked=False
    RangePicked=False
    AveragePicked=False
    CalcsList = ("MaxPicked", "MinPicked", "RangePicked","AveragePicked")
    
    for i in range(len(CalcsList)):
        print(i, CalcsList[i]) # present the user which option they want

    PickedBoolean = False # make sure user hasnt enter wrong value
    while PickedBoolean == False:
        Picked = int(input("Which calculation do you want?")) # ask user what option they want
        if Picked < 5 and Picked > -1: # make sure the user enters corrent value
            #print(CalcsList[Picked])
            if Picked == 0:
                MaxPicked=True
                PickedBoolean = True
            elif Picked == 1:
                MinPicked=True
                PickedBoolean = True
            elif Picked == 2:
                RangePicked=True
                PickedBoolean = True
            else:
                AveragePicked=True
                PickedBoolean = True
        
    
    MaxNumber = 0
    MinNumber = 999999999999 # used to find max and min
    for i in AllValues:
        if float(i) > MaxNumber:
            MaxNumber = float(i)
        elif float(i) < MinNumber:
            MinNumber = float(i)
    # if user has picked 3 options then calculations are already done
    if MaxPicked == True:
        return MaxNumber
    if MinPicked == True:
        return MinNumber
    if RangePicked == True:
        RangeNumber = MaxNumber-MinNumber
        return RangeNumber
    # if user picked average, simple calculation to find total of list and divide by num of values
    if AveragePicked == True:
        CountingSum = 0
        NumOfValues = 0
        for i in AllValues:
            NumOfValues += 1
            CountingSum += float(i)

        if NumOfValues != 0: # make sure list isnt empty
            Average = CountingSum/NumOfValues
            
            return Average


#print(selected_days("MY1", "NO", "2022-12-05", "2022-12-08"))
