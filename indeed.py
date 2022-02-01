import requests as req
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"
last_page = 20


# def extract_indeed_pages():
#   result = req.get(URL)
#   soup = BeautifulSoup(URL, 'lxml')
  
#   return last_page


#https://kr.indeed.com/jobs?q=python&limit=50&start=0
# start 인자에 0 = 1gage, 50 = 2page
def extract_indeed_jobs(last_page=last_page):
  jobs = list()
  # for page in range(last_page):
  #   result = req.get(f"{URL}&start={page*LIMIT}")
  #   soup = BeautifulSoup(result.text, "lxml")
  #   results = soup("div", {"class": "mosaic-provider-jobcards"})
  #   print(results)
  #   return jobs
  # Test code
  result = req.get(f"{URL}&start={0*LIMIT}")
  soup = BeautifulSoup(result.text, "lxml")
  results = soup.find_all("a", {"class": "tapItem"})
  
  for result in results:
    temp = result.find('h2')
    title = temp.find("span")['title']
    print(title)
    break
    

  
  # for result in results:
  #   #print(result.find("span", {"class": "title"}))
  #   #print(result.find("span").find('title'))
  #   #len(results) => 50
  #   tab = result.find("h2")["jobTitle"]
  #   print(tab)
    
  return jobs
#div class: mosaic-provider-jobcards