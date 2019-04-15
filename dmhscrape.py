# import libraries
from urllib.request import urlopen
import os
from bs4 import BeautifulSoup


dirPath = os.getcwd() #Get the Current working directory
filePath = "CommerceC/Members -.html" #Specify the File to Scrape
absFilePath = os.path.join(dirPath, filePath) #Join directory and file to create URL
#print(absFilePath)

#Open HTML File to scrape
page = urlopen("file:///" + absFilePath)
soup = BeautifulSoup(page, 'html.parser')
	
def spanScan():
	if page:
		spans = soup.find_all('span')
		for span in spans:
			companies = []
			companyName = span.find('p', {'class': 'ccaMemName'})
			companyWeb = span.find('a', href=True)
			companyAddr = span.find('p', {'class': 'ccaAddr'})
			
			if companyName:
				print(companyName.text + companyWeb['href']+ companyAddr.text + "\n")


data = spanScan()
print(data)


