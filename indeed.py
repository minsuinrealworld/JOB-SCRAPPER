import requests as req
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"
last_page = 20

def extract_indeed_jobs(last_page=last_page):
  jobs = list()
  # for page in range(last_page):
  result = req.get(f"{URL}&start={0*LIMIT}")
  soup = BeautifulSoup(result.text, "lxml")
  results = soup.find_all("a", {"class": "tapItem"})
  for result in results:
    title = result.find("h2").text
    company = result.find("span", {"class": "companyName"}).text
    print(f"Title: {title} CompanyName: {company}")
  return jobs
