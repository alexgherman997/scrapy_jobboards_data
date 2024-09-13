# Project status 
Web scraping using Python and Scrapy. More documentation here: https://docs.scrapy.org/en/latest/

## Instalation 
pip3 install scrapy

## Execution 
## Scrape the class name = 'qoutes' and output console
scrapy crawl quotes 

## Scrape the class name = 'qoutes' and output result in jsonl
scrapy crawl quotes -O ex.jsonl 

## Debugging, searching selectors on page
scrapy shell 'https://quotes.toscrape.com/page/1/'