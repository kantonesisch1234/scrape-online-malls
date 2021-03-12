# scrape-online-malls

This is a very simple Python mini-program for scraping online malls based on BeautifulSoup. When the program is executed, the Python code reads the queries and the page ranges from the txt file in the current working directory, and automatically download the images of the products returned as query results.

The program is currently only for experimentation and can only scrape one single online shop website: [Round The Clock Mall.com](https://www.roundtheclockmall.com/). The website is chosen simply because it can be scraped easily with BeautifulSoup. Some websites are a lot harder because they obviously took the measure to avoid webscraping. In future, I will try to extend the program for it to scrape more different websites, as long as the scraping based on BeautifulSoup is possible. As long as the BeautifulSoup approach is possible, all one needs to do is to modify a bit on the way of reading the HTML tags. 

Dependencies: `bs4`, `uuid`. 

Possible future updates:
* Able to scrape more online shop websites.
* Automatically remove duplicated images.
* (Much, much, much harder - machine learning will be needed) Automatically remove images containing/without humans. 
