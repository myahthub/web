
#Student Name:  A'Myah Temple
#Program Name:  Webscraping
#Creation Date:  04/23/25
#Last Modified Date:  11/20/25
#CSCI Course:  301
#Grade Received:  100
#Design Comments: This project grabs job info from a website. It looks at the page, finds each job, and gets the title, 
#company, location, and link. The code is easy to read and easy to change if the website updates.

import requests
from bs4 import BeautifulSoup

#website wanted to scrape
URL = "https://pythonjobs.github.io/"
#send a request to website and store the page content
page = requests.get(URL)
#parsers the HTML content using BeatifulSoup
soup = BeautifulSoup(page.content, "html.parser")
#find all job listing
job_listings = soup.find_all("div", class_="job")
#loop thorugh each job listing to extract and print the title, company, location, and link
for job in job_listings:
	title = job.find("h1").text.strip() if job.find("h1") else "N/A"
	company = job.find("span", class_="info").text.strip() if job.find("span", class_="info") else "N/A"
	location = job.find("span", class_="location").text.strip() if job.find("span", class_="location") else "N/A"
	link = job.find("a")["href"] if job.find("a") else "N/A"
	print(f"Job Title: {title}")
	print(f"Company: {company}")
	print(f"Location: {location}")
	print(f"Apply Here: {link}\n")
