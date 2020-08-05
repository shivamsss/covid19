import pandas as pd
teams=[ "Rajasthan Royals",
    "Delhi Capitals",
    "Chennai Super Kings",    "Mumbai Indians",
    "Delhi Capitals",
    "Kolkata Knight Riders",
    "Chennai Super Kings",
    "Deccan Chargers",
    "Kings XI Punjab",
    "Mumbai Indias"
    ]
ranks = [2, 3, 4, 1, 3, 4, 1, 2, 5, 4]
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
data_set={
    "teams":teams,
    "ranks":ranks,
    "years":years
}
#print(data_set)
pd_data_set=pd.DataFrame(data_set)
print(pd_data_set)
print()
group_pd_data_set=pd_data_set.groupby('ranks')
print(group_pd_data_set.groups)
print()
grouped_data_set = pd_data_set.groupby(['teams', 'ranks'])
print(grouped_data_set.groups)

print("Iterating In Group Items")

for teams,grp in grouped_data_set:
    print(teams)
    print(grp)
    print("Another iTERABLE+++++++++++++++++++++++")
    print(grouped_data_set.get_group(teams))