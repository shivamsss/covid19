import requests

import json
import pandas as pd
import numpy as np


class Covid:
    def __init__(self,daily_data,daily_date):
        self.daily_data=daily_data
        self.daily_date=daily_date

    def __str__(self):
        return "{},{}\n".format(self.daily_data,self.daily_date)

class fetchapidata:

   def fetch(self,save_data):

       url = "https://api.covid19india.org/states_daily.json"
       response = requests.get(url)
       covid_data=json.loads(response.text)
       covid_data_daily=covid_data['states_daily']
       i=0
       covid_data_new=[]
       covid_data_new_date=[]

       for i in range(0, len(covid_data_daily),3):
           covid_data_new.append(covid_data_daily[i]['pb'])


       for i in range(0,len(covid_data_daily),3):
           covid_data_new_date.append(covid_data_daily[i]['date'])

       covid_csv=[]
       for i in range(0,len(covid_data_new)):
           data=Covid(covid_data_new[i],covid_data_new_date[i])
           covid_csv.append(data)
       if save_data:
           file=open('pb_covid_data.csv','a')
           for team in covid_csv:
              # print(team)
               file.write(str(team))


def main():
    data=fetchapidata()
    data.fetch(True)
 
if __name__ == '__main__':
    main()