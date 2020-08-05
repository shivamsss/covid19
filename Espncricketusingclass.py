import requests
from bs4 import BeautifulSoup

class team:
    def __init__(self,year,name,matches,won,lost,tied,abonded,points,runrate):
        self.year=year
        self.name=name
        self.matches=matches
        self.won=won
        self.lost=lost
        self.tied=tied
        self.abonded=abonded
        self.points=points
        self.runrate=runrate

    def __str__(self):
        return "{},{},{},{},{},{},{},{},{}\t".format(self.year,self.name,self.matches,self.won,self.lost,self.tied,self.abonded,self.points,self.runrate)

class fetchdata:
    def fetchdata(self,year,save_data):
        url="https://www.espncricinfo.com/table/series/8048/season/{}/ipl".format(year)
        response=requests.get(url)
        soup=BeautifulSoup(response.text,"html.parser")
        name_tags = soup.find_all("h5", class_="header-title label")
        data_tags = soup.find_all("td", class_="")
        point_tags = soup.find_all("td", class_="border-right label")
        namelist = []
        datalist = []
        pointlist = []
        for tag in name_tags:
            namelist.append(tag.text.strip())
            datalist.append([])
        del namelist[0]
        del datalist[0]
        i = 0
        j = 0

        for data in data_tags:
            datalist[i].append(float(data.text.strip()))
            j += 1
            if j % 6 == 0:
                i += 1

        for point in point_tags:
            pointlist.append(float(point.text.strip()))

        teams=[]

        for i in range(len(namelist)):
            team=team(year,namelist[i],datalist[i][0],datalist[i][1],datalist[i][2],datalist[i][3],datalist[i][4],
                       pointlist[i],datalist[i][5])
            teams.appends(team)

        if save_data:
            file = open("IPL-TEAMS-DATA-{}.csv".format(year), 'a')

            for team in teams:
                print(team)
                file.write(str(team))

            print("DATA-SAVED-IN-FILE")

        else:
            for team in teams:
                print(team)


def main():

    data = fetchdata()
    data.fetchData(2019, True)

if __name__ == '__main__':
    main()