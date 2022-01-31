import requests as req
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"
last_page = 20


def extract_indeed_pages():
  result = req.get(URL)
  soup = BeautifulSoup(URL, 'lxml')
  
  return last_page


#https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit=50&radius=25&start=0
# start 인자에 0 = 1gage, 50 = 2page
def extract_indeed_jobs(last_page):
  for page in range(last_page):

    result = req.get(f"{URL}&start={page*LIMIT}")
    print(result.status_code)
  
