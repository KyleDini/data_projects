"""
    Task: scrape title, link and date from blog posts on rithmschool.com/blog and store in a csv file

    order: make request, get the response, send the response (html) to beautifulsoup, extract the info we want with beautifulsoup, then write that info to a csv file

    https://wwww.rithmschool.com/blog
"""

import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")

"""
    ^ prints the html from the website, but it's hard to read :(
    go to the website and open the dev tools (right-click -> inspect)
    in this example, each article is wrapped by an article element
    for each article, we want to select the anchor tag that's inside of h4, the href to get the url (inside of h4), and the date (in <div class "card">)

    looking through the site's html is common because scraping is just telling it where to look
"""

soup = BeautifulSoup(response.text, "html.parser")

articles = soup.find_all("article")
print(articles)
with open("blog_data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "link", "date"])

    for article in articles:
        a_tag = article.find("a")
        article_title = a_tag.get_text()
        article_url = a_tag["href"]
        article_date = article.find("time")["datetime"]
        csv_writer.writerow([article_title, article_url, article_date])
    # this is the actual scraping portion of the code
    # this needs to be in the 'with open' because we need the file to be open while we write to it
    # webcrawling is when we go to multiple urls (usually to scrape data)
    # this example will only scrape one url, need to add webcrawling functionality
