import requests
from bs4 import BeautifulSoup

url="https://www.espncricinfo.com/table/series/8048/season/2019/ipl"
response=requests.get(url)
#print(response.text.strip())
soup = BeautifulSoup(response.text, "html.parser")

name_tags=soup.find_all("h5",class_="header-title label")
data_tags=soup.find_all("td",class_="")
point_tags=soup.find_all("td",class_="border-right label")
namelist=[]
datalist=[]
pointlist=[]
for tag in name_tags:

    namelist.append(tag.text.strip())
    datalist.append([])
del namelist[0]
del datalist[0]
i = 0
j = 0

for data in data_tags:
    datalist[i].append(float(data.text.strip()))
    j+=1
    if j % 6 == 0:
        i += 1


for point in point_tags:
    pointlist.append(float(point.text.strip()))

print(namelist)
print(datalist)
print(pointlist)

