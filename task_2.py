import pprint
from task_1 import scrape_top_list
import json
details=scrape_top_list() 
# pprint.pprint(details)
def  group_by_year(movies): 
    unic_year=[]
    for i in details: 
        year=i["year"]
        if year not in unic_year: 
            unic_year.append(year)
            unic_year.sort()
    dic_of_movies={i:[] for i in unic_year}
    for i in movies:
        year=i["year"]
        for j in dic_of_movies: 
            if str(j)==str(year):
                dic_of_movies[j].append(i)
    with open("task_2.json","w+") as file: 
        json.dump(dic_of_movies,file,indent=4)
        return(dic_of_movies)
import pprint
pprint.pprint(group_by_year(details)) 