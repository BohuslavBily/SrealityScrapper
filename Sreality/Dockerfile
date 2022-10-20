FROM python:latest
WORKDIR /scraper
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["./wait-for-postgres.sh", "db", "scrapy", "crawl", "Sreality"]
