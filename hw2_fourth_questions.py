### HW2 Fourth Questions

# Use the data in covid.csv for this exercise
#
# 10) In a separate file, write a piece of code that
# loads the covid.csv file and prints the list of countries
#  and the total average of death/confirmed among those countries
# for those countries that have more than 500, 1000 and 5000
# active cases respectively.
# Follow DRY principles in order to complete this exercise.


import pandas as pd


df_covid = pd.read_csv("covid.csv")
df_covid.head(10)


def covid_stats(df):
    
    thresholds = [500, 1000, 5000]
    
    for thres in thresholds:
        threshold_data = df[df["Active"] > thres]
        
        threshold_data["deaths_confirmed_avg"] = threshold_data["Deaths"] / threshold_data["Confirmed"]
        
        print("List of countries with more than " + str(thres) + " active cases.")
        print(threshold_data[["Country", "deaths_confirmed_avg"]].to_string(index=False))
        

print(covid_stats(df_covid))