# scrape-online-malls

This is a very simple Python mini-program for scraping online malls based on BeautifulSoup. When the program is executed, the Python code reads the queries and the page ranges from the txt file in the current working directory, and automatically download the images of the products returned as query results.

The program is currently only for experimentation and can only scrape an online shop website: [Round The Clock Mall.com](https://www.roundtheclockmall.com/). The website is chosen simply because it can be scraped easily with BeautifulSoup. Some websites are a lot harder because they obviously took the measure to avoid webscraping. For the future, I will try to extend the program for it to scrape more different websites, as long as the scraping based on BeautifulSoup is possible. 

Dependencies: `bs4`, `uuid`. 
