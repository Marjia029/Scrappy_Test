FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY scrapingcourse_scraper/ scrapingcourse_scraper/

CMD ["scrapy", "crawl", "products"]
