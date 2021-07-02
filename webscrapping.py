# To make the web scrapping programme first you need t0
# 1) Install the requests and bs4 library
import requests
from bs4 import BeautifulSoup as bs

github_user = input("Enter the github user name :")
url='https://github.com/'+github_user
r=requests.get(url)
soup=bs(r.content,'html.parser')
profile_image=soup.find('img',{'class':' avatar avatar-user'})['src']
print(profile_image)