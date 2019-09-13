
# Brad Stephenson
# Web Crawling HW6
# 4/10/19


#import urllib3
import urllib.request
import urllib.parse
import urllib.error

from bs4 import BeautifulSoup

def main():

	page = urllib.request.urlopen("https://fantasy.nfl.com/research/projections")
    soup = BeautifulSoup(page, 'html.parser')

    print soup.find_all("tr")




if __name__ == "__main__":
	main()