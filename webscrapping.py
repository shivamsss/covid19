import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
url="https://www.imdb.com/india/top-rated-indian-movies/"
response=requests.get(url)
#print(response.text)

soup=BeautifulSoup(response.text,"html.parser")
movienametags=soup.find_all("td",class_="titleColumn")
movieratingtags=soup.find_all("td",class_="ratingColumn imdbRating")

movietitle=[]
movieyear=[]
movierating=[]
for tag in movienametags:
    # print(tag)
    # print(tag.text.strip())
    title=tag.text.strip()
    year = int(title[-5:-1])
    movietitle.append(title)
    movieyear.append(year)

print(movietitle)
print(movieyear)

for tag in movieratingtags:
    rating=tag.text.strip()
    movierating.append(rating)
print(movierating)

plt.scatter(movieyear,movierating)
plt.show()