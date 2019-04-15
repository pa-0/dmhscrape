# import libraries
from urllib.request import urlopen
import os
from bs4 import BeautifulSoup


dirPath = os.getcwd() #Get the Current working directory
filePath = "CommerceC\Members -.html" #Specify the File to Scrape
absFilePath = os.path.join(dirPath, filePath) #Join directory and file to create URL
print(absFilePath)

#Open HTML File to scrape
page = urlopen("file:///" + absFilePath)
soup = BeautifulSoup(page, 'html.parser')

def soupFinder(className):
	if page:
		dataText = soup.find('p', attrs={'class': className}).text.strip()
	return dataText
	
def soupFinderTag(className, liClass):
	for ultag in soup.find_all('ul', {'class': className}):
		for litag in ultag.find_all('li', {'class': liClass}):
			foundTag = litag.text
			return foundTag

#Function to scrape desired Data
def scrapeData():
	cName = soupFinder('ccaMemName')
	wAddr = soupFinder('ccaWebAddrLk')
	cAddr = soupFinder('ccaAddr')
	cContact = soupFinder('ccaAddrPhone')

	print(companyName)
	
# repName = soup.find('span', {'class': 'WebRupee'})
# for rep in repName:
    # print(rep.string)
	
badges = soup.body.find('div', attrs={'class': 'ccaMemListingContainer'})
for span in badges.span.find_all('span'):
    print(span.)
