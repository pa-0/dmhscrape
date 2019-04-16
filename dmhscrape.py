# import libraries
from urllib.request import urlopen
import os
import csv
from bs4 import BeautifulSoup


dirPath = os.getcwd() #Get the Current working directory
filePath = "CommerceC/Members -.html" #Specify the File to Scrape
absFilePath = os.path.join(dirPath, filePath) #Join directory and file to create URL
#print(absFilePath)

#Open HTML File to scrape
page = urlopen("file:///" + absFilePath)
soup = BeautifulSoup(page, 'html.parser')

with open('commercec.csv', 'w') as myfile:
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	wr.writerow(["Company Name", "Company Website", "Address", "Phone"])
	if page:
		spans = soup.find_all('span')
		for span in spans:
			companyName = span.find('p', {'class': 'ccaMemName'})
			companyWeb = [tag['href'] for tag in span.select('p a[href]')]
			companyAddr = span.find('p', {'class': 'ccaAddr'})
			cInfo = span.find('p', class_='ccaContactInfo')
			cAddr = str([companyAddr.text[:-3]])
			if companyName:
				wr.writerow([companyName.text] + [companyWeb[1]] + [companyAddr.text[:-3]] + [cInfo.text[:11]])
