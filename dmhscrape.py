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
			companyName = span.find('p', {'class': 'ccaMemName'})
			companyWeb = [tag['href'] for tag in span.select('p a[href]')]
			companyAddr = span.find('p', {'class': 'ccaAddr'})
			if companyName:
				company = [[companyName.text] + [companyWeb[1]] + [companyAddr.text[:-3]]]
				print(company)
#				return companyName.texts, companyWeb[1], companyAddr.text


#cName, cWeb, cAddr = spanScan()
spanScan()


