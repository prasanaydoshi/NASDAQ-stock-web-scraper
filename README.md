# NASDAQ-stock-web-scraper
Welcome to my NASDAQ stock scraper project!

This project like most great ones was built out of necessity and for convenience. Having started off young in the investing space, I always wished for an easier way to filter data and ensure that I only get particular results. This small program is my version of a Bloomberg terminal; having only used one at my school, I was inspired by it and created this project. 

This web scraping project uses the popular Python libraries pandas and Beautiful Soup to scrape data from the NASDAQ website and Yahoo Finance. The project first scrapes a list of all NASDAQ-listed stocks and then dynamically creates a list of URLs for each stock. The scraper then extracts data from each of the URLs and converts all the scraped data into a CSV file. 

The original list of stocks was scraped from https://www.advfn.com/nasdaq. This website allowed me to conviently scrape all the possible stocks listed on NASDAQ. Part of scraping this website also included dynamically creating URL's for different sections of this website.

The rest of the data was scraped from Yahoo finance; while scraping it, I also cleaned it. Some stocks may be tradable but are holding companies and have no real value to the retail investor.

This project is designed to be easily scalable, allowing you to scrape as much data as you need. The code is well-organized, with separate functions for each step of the scraping process, making it easy to modify or customize for your specific use case.

To use this project, you will need to have Python 3 installed on your system, along with the following libraries: pandas, Beautiful Soup, and requests. You can install these libraries using pip, the Python package manager. Simply run pip install pandas beautifulsoup4 requests in your command line to install them.

Once you have the required libraries installed, you can run the main.py script to start scraping. The program will create a data folder in the project directory, where the scraped CSV files will be stored.

Thank you for checking out my NASDAQ stock scraper project. I hope you find it useful! If you have any questions or feedback, please feel free to contact me.
