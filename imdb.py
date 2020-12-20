import requests
from bs4 import BeautifulSoup
url="https://www.imdb.com/india/top-rated-indian-movies/"
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
def scrap_by_list():
    contents=soup.find('tbody',{'class':'lister-list'})
    years=contents.find_all('span',class_="secondaryInfo")

    relyear=[]
    for year in years:
        relyear.append((year).get_text())
    
        

    movname=[]
    title1=contents.find_all('a')
    for title in title1:
        a=title.get_text()
        if  a == ' \n':
            continue
        else:
            movname.append(a)

    movlink=[]
    links=contents.find_all("a")
    for link in links:
        l=link.get("href")
        li="https://www.imdb.com" + l
        movlink.append(li)


    movTitle=[]
    titles=contents.find_all("a")
    for title in titles:
        t=title.get("title")
        if type(t)==str:
            movTitle.append(t)
        else:
            continue

    movRate=[]
    rates=contents.find_all('strong')
    for rate in rates:
        rate.get("title")
        movRate.append(rate.text)


    movie_list=[ ]
    dicte={"movie ranking":" " , "movie_name":" ","movie_title":"" , "movie_Rating":"" , "movlink":" "}
    for i in range(0,250):
        dicte["movie ranking"]=i+1
        dicte["movie_name"]=movname[i]
        dicte["movie_title"]=movTitle[i]
        relyear[i] = relyear[i][1:5]
        dicte["release_year"]=int((relyear[i]))
        dicte["movie_Rating"]=float(movRate[i])

        dicte["movlink"]=movlink[i]
        movie_list.append(dicte.copy())
    return movie_list
scraped=scrap_by_list()

import json 
file=open("year.json","w")
json.dump(scraped,file,indent="")































































# for i in range(0,len(movname)):
#     e={ }
#     pos+=1
#     for movName in movname:
#         e["position"]=pos
#         e["Movie Name"]=movname[i]
#         for movetitle in movTitle:
#             e["title"]= movTitle[i]
#             for relYear in relyear:
#                 e["Releasing Year"] = relyear[i]
#                 for rating in movRate:
#                     e[" Movies Rating"] = movRate[i]
#                     for Links in movlink:
#                         e["Movie Link"]= movlink[i]
#                         break
#                     break
#                 break
#             break            
#     dicte["MOVIE"]=e
#     v.append(dicte)
# print(v)
# import json

# pot=open("imdb.json","w")
# json.dump(v,pot,indent="")














    









