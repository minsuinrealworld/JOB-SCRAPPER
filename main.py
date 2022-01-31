import requests
from bs4 import BeautifulSoup


indeed_result = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85as_and=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, 'lxml')



#https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit=50&radius=25&start=0
# start 인자에 0 = 1gage, 50 = 2page
