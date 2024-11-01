# -*- coding: utf-8 -*-.
"""
Created on Wed Oct  2 00:35:40 2024.

@author: BNELS
"""

import pandas as pd
hour = pd.read_csv('data/hour.csv')
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
