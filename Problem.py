import sys
import requests
from bs4 import BeautifulSoup

class Problem:

  def __init__(self, URL):
    
    try : 
      r = requests.get(URL)
      soup = BeautifulSoup(r.content, 'html5lib') 
    except Exception as e : 
      sys.exit("!! Can't fetch webpage, try rechecking the link !!")
    
    x =  soup.find('div', attrs = {'class':'title'}) 
    self.name = x.text;    
    
    x =  soup.find('th', attrs = {'class':"left", 'style':"width:100%;"})
    self.contest = x.text

    x =  soup.findAll('span', attrs = {'class':"tag-box"})
    self.tags = []
    for z in x: 
        self.tags.append(z.text.strip())
    

