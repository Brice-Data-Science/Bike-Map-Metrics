# -*- coding: utf-8 -*-.
"""
Created on Wed Oct  2 00:35:40 2024.

@author: BNELS
"""

import pandas as pd
import matplotlib.pyplot as plt

# Loading or creating a DataFrame and assigning it to 'hour'
hour = pd.read_csv('data/hour.csv')

# ****************** EXPLORATORY DATA ANALYSIS BELOW ***********************

print(hour.head())
print('')
# print(f"The mean of the total users(count) is: {hour['count'].mean()}")
# print(f"The median of the total users(count) is: {hour['count'].median()}")
# print(
#     f"The standard deviation of the total users(count) is:"
#     f"{hour['count'].std()}\n"
# )

# print(
#     f"The minumum usage of the registered users is:"
#     f"{hour['registered'].min()}"
# )
# print(
#     f"The maximum usage of the registered users is:"
#     f"{hour['registered'].max()}"
# )

print(f"The summary statistics for the last two years can be found below:"
      f"{hour.describe()}")

print(
    "Legend for seasons:  \nWinter = 1 \nSpring = 2 \nSummer = 3\n"
    "Fall = 4\n"
)

# This code calculates the mean of the 'count' column for each unique value in
# the 'season' column within the hour DataFrame.
print(hour.groupby(['season'])['count'].mean())
# Here's how it works:

# hour.groupby(['season']): Groups the DataFrame by the 'season' column,
# creating a subset of rows for each unique season.
# ['count']: Selects the 'count' column from each group.
# .mean(): Calculates the mean of the 'count' column within each group.
# ***********************************************************

print("\nThe average ridership statistics for the number of riders in either"
      " high heat or high humidity:\n")
# ******************************************************
# This line of code calculates and prints the mean of the 'count' column from
# the DataFrame hour, but only for rows where either the 'temp' column is
# greater than 0.5 or the 'hum' column is greater than 0.5.
print(hour.loc[(hour['temp'] > 0.5) | (hour['hum'] > 0.5), 'count'].mean())
# Display the filtered DataFrame as a string
print('')
print('Descriptive Stats')
print(hour[['temp', 'hum', 'count']].describe())
summary_stats = hour[['temp', 'hum', 'count']].describe()
print(summary_stats.to_string())


# hour.loc[(hour['temp'] > 0.5) | (hour['hum'] > 0.5), 'count']: This uses .loc
# to filter hour DataFrame rows based on the condition temp > 0.5 or hum > 0.5
# and selects only the 'count' column.
# ***************************************************************

print("\nThe average ridership statistics for the number of riders in each"
      " season and holidays:\n")
print(
    "Legend for seasons:  \nWinter = 1 \nSpring = 2 \nSummer = 3\n"
    "Fall = 4\n"
)
# Prints the mean per season
print(hour.groupby(['season'])['count'].mean())

# prints the mean per season and holiday
print(
    "Legend for holidays:  \nHoliday = 1 \nNon-Holiday = 0")
print(hour.groupby(['season', 'holiday'])['count'].mean())

# ************ VISUALIZING DATA WITH MATPLOTLIB *****************************

# ********** SCATTER PLOT OF ALL DATA ********

fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(x=hour['instant'], y=hour['count'])
ax.set_xlabel('Hour')
ax.set_ylabel('Count')
ax.set_title('Ridership Count By Hour')
plt.show()

# ******** SCATTER PLOT OF FIRST TWO DAYS ***********

hour_first48 = hour.loc[0:48, :]
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(x=hour_first48['instant'], y=hour_first48['count'])
plt.xlabel('Hour')
plt.ylabel('Count')
plt.title('Count by hour - First Two Days')

# ******** SCATTER PLOT OF LAST YEAR ***********

hour_last_year = hour.loc[8750:17500, :]
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(x=hour_last_year['instant'], y=hour_last_year['count'])
plt.xlabel('Hour')
plt.ylabel('Count')
plt.title('Count by hour - Last Year')
