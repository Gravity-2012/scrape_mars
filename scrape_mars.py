# Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import requests
import pandas as pd

def scrape():

    executable_path = {'executable_path': 'C:/Users/chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


    # URL of Mars Exploration Program page to be scraped
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    # Retrieve page with the requests module
    response = requests.get(url)
    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response.text, 'html.parser')
    # use the container 'div' and the class 'side' to prepare for printing statement of title and paragraph
    results = soup.find_all('div', class_="slide")
    # print cleaned titles and print cleaned pargraphs
    for result in results:

        news_title = result.find('div', class_="content_title")
        title = news_title.find('a').text.strip()
        paragraph = result.find('div', class_="rollover_description_inner").text.strip()


    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    # Retrieve page with the requests module
    response = requests.get(url)
    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response.text, 'html.parser')
    # use inspect to find the hyperlink tag 'a' and the class 'button fancybox'
    results = soup.find_all('a', class_="button fancybox")
    # run loop for featured image
    # this will be the list we're appending to
    # main url + picture hrl will get you the featured_image_url
    image_reference = []
    main_url = 'https://www.jpl.nasa.gov'

    for x in results:
        pic = x['data-fancybox-href']
        image_reference.append(pic)
    
    # combine the main website with the feature data-fancybox-href to get the full image
    featured_image_url = main_url + pic


    # set URL path
    # let browser visit the site
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    # use BeautifulSoup to pull in the weather tweet on Mars
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')
    mars_weather = soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text.strip()


    # URL path
    url = 'https://space-facts.com/mars/'
    # Use pandas to read any tables on the URL
    tables = pd.read_html(url)
    # slice dataframe and use normal indexing
    df = tables[1]
    df. columns = ['Index', 'Measurement']
    # Use df.to_html() to convert to html for later use
    df.to_html('Mars_Facts')


    #mars_data dictionary
    mars_data = {'title': title, 'paragraph': paragraph, 'featured_image_url': featured_image_url,\
         'mars_weather': mars_weather}

    return mars_data
    
print(scrape())
