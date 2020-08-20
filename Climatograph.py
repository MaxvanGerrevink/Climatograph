## Libaries...
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

## Loading Precipitation data...
## The KNMI precipitation data can be retrived from https://www.knmi.nl/nederland-nu/klimatologie/monv/reeksen
data = pd.read_csv("C:/VU_Amsterdam/HYDRO_Thesis/Data/Precipitation_data_1951_2020.csv",';') ## precipitation file
data.head()

## Loading Temperature data...
## The KNMI precipitation data can be retrived from https://www.knmi.nl/nederland-nu/klimatologie/daggegevens
Temp = pd.read_csv("C:/VU_Amsterdam/HYDRO_Thesis/Data/Temp_data_volkol_1962_2020.csv",';') ## Temperature and other climatological data
Temp.head()

## Setting up the data frame for precipitation
## Splitting the dates...
data['Date'] = data['YYYYMMDD']
data['Date'] = pd.to_datetime(data['Date'])

data['Day'] = data['Date'].dt.day
data['Month'] = data['Date'].dt.month
data['Year'] = data['Date'].dt.year

## Converting the precipitation data into mm.
data = data[data['RD'].str[0:3] != 'Nan'] ## removing no data fields
data['Rain_mm'] = data['RD'].str[0:3] ## add a RAIN column
data['Rain_mm'] = data['Rain_mm'].astype('int') ## convert the rainvalues into interger
data['Rain_mm'] = data['Rain_mm']/10 ## convert precipitation to mm (KNMI measures precipitation in 0.1 mm)
data.head()

## Setting up the data frame for Temperature
## splitting the dates...
Temp['Date'] = Temp['YYYYMMDD']
Temp['Date'] = pd.to_datetime(Temp['Date'])

Temp['Day'] = Temp['Date'].dt.day
Temp['Month'] = Temp['Date'].dt.month
Temp['Year'] = Temp['Date'].dt.year

## Converting temperature
Temp['Temp'] = Temp['TG'].astype('int') ## convert the rainvalues into interger
Temp['Temp'] = Temp['Temp']/10 ## convert rain to Graden Celsius (KNMI measures temperature in 0.1 degrees celsius)

## Getting labels for plots..
Months = [Month for Month, df in data.groupby('Month')]
Years = [Year for Year, df in data.groupby('Year')]

## Monthly grouping of precipittation data
Jan = data.loc[data['Month'] == 1]
Jan = Jan['Rain_mm'].mean()*31

Feb = data.loc[data['Month'] == 2]
Feb = Feb['Rain_mm'].mean()*28

Mar = data.loc[data['Month'] == 3]
Mar = Mar['Rain_mm'].mean()*31

Apr = data.loc[data['Month'] == 4]
Apr = Apr['Rain_mm'].mean()*30

May = data.loc[data['Month'] == 5]
May = May['Rain_mm'].mean()*31

Jun = data.loc[data['Month'] == 6]
Jun = Jun['Rain_mm'].mean()*30

Jul = data.loc[data['Month'] == 7]
Jul = Jul['Rain_mm'].mean()*31

Aug = data.loc[data['Month'] == 8]
Aug = Aug['Rain_mm'].mean()*31

Sep = data.loc[data['Month'] == 9]
Sep = Sep['Rain_mm'].mean()*30

Oct = data.loc[data['Month'] == 10]
Oct = Oct['Rain_mm'].mean()*31

Nov = data.loc[data['Month'] == 11]
Nov = Nov['Rain_mm'].mean()*30

Dec = data.loc[data['Month'] == 12]
Dec = Dec['Rain_mm'].mean()*31

Rain_monthly = [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec]

## Monthly grouping temperature data
Jan_temp = Temp.loc[Temp['Month'] == 1]
Jan_temp = Jan_temp['Temp'].mean()

Feb_temp = Temp.loc[Temp['Month'] == 2]
Feb_temp = Feb_temp['Temp'].mean()

Mar_temp = Temp.loc[Temp['Month'] == 3]
Mar_temp = Mar_temp['Temp'].mean()

Apr_temp = Temp.loc[Temp['Month'] == 4]
Apr_temp = Apr_temp['Temp'].mean()

May_temp = Temp.loc[Temp['Month'] == 5]
May_temp = May_temp['Temp'].mean()

Jun_temp = Temp.loc[Temp['Month'] == 6]
Jun_temp = Jun_temp['Temp'].mean()

Jul_temp = Temp.loc[Temp['Month'] == 7]
Jul_temp = Jul_temp['Temp'].mean()

Aug_temp = Temp.loc[Temp['Month'] == 8]
Aug_temp = Aug_temp['Temp'].mean()

Sep_temp = Temp.loc[Temp['Month'] == 9]
Sep_temp = Sep_temp['Temp'].mean()

Oct_temp = Temp.loc[Temp['Month'] == 10]
Oct_temp = Oct_temp['Temp'].mean()

Nov_temp = Temp.loc[Temp['Month'] == 11]
Nov_temp = Nov_temp['Temp'].mean()

Dec_temp = Temp.loc[Temp['Month'] == 12]
Dec_temp = Dec_temp['Temp'].mean()

Temp_monthly = [Jan_temp, Feb_temp, Mar_temp, Apr_temp, May_temp,\
                Jun_temp, Jul_temp, Aug_temp, Sep_temp, Oct_temp,\
                Nov_temp, Dec_temp]

## Plotting charts
sns.set_style('darkgrid')
fig, ax1 = plt.subplots()
ax1.bar(Months, Rain_monthly, color = 'b')
ax2 = ax1.twinx() 
ax2.plot(Months, Temp_monthly, color = 'r')
ax1.set_xticks(Months)
ax1.set_ylim(30,75)
ax1.set_xlabel('Month')
ax1.set_ylabel('Precipitation (mm)')
ax2.set_ylabel('Temperature (C)')
ax1.set_title('Climatograph of the Deurnsche Peel', fontweight='bold')
plt.show()
