import requests as req
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"
redirect_job_id = f"https://kr.indeed.com/viewjob?jk="


def extract_indeed_jobs(page_num=20):
  
  jobs = list()
  count_page = 0
  for page in range(20):
    print(f"Scrapping page {page}")
    result = req.get(f"{URL}&start={count_page*LIMIT}")
    count_page += 1
    soup = BeautifulSoup(result.text, "lxml")
    results = soup.find_all("a", {"class": "tapItem"})
    for result in results:
      title = result.find("h2", {"class": "jobTitle"}).find("span", title=True).text
      company = result.find("span", {"class": "companyName"})
      if(company is not None):
        company_anchor = company.find("a")
      if(company_anchor is not None):
          company = company_anchor.text
      elif company_anchor is None and company is None:
        company = "No company name"
      else:
        company = company.text
      location = result.find("div", {"class": "companyLocation"}).text
      job_id = result['data-jk']
      job_url = redirect_job_id+job_id
      job = {'title': title, 'company': company, 'location': location, 'link': job_url}
      jobs.append(job)
  return jobs

