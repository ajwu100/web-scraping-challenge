import os
from bs4 import BeautifulSoup
from splinter import Browser
import requests
import pandas as pd


def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()
    # Scrape from NASA Mars News Site for latest News Title and Paragraph Text.
    url1 = 'https://mars.nasa.gov/news/'
    browser.visit(url1)
    html1 = browser.html
    soup = BeautifulSoup(html1, 'html.parser')
    news_titles = []
    news_ps = []
    mars_news = soup.find_all('li', class_="slide")
    for news in mars_news:
        title = news.find(class_="content_title").text
        p = news.find(class_="article_teaser_body").text
        news_titles.append(title)
        news_ps.append(p)
    news_title = news_titles[0]
    news_p = news_ps[0]
    # print(news_title)
    # print(news_p)
    browser.quit()

    browser = init_browser()
    # Scrape from JPL Featured Space Image for current featured Mars image.
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)
    html2 = browser.html
    soup = BeautifulSoup(html2, 'html.parser')
    mars_image = soup.find_all(class_="img")[0]
    image_url = mars_image.img["src"]
    featured_image_url = ["http://www.jpl.nasa.gov/"+image_url]
    # print(featured_image_url)
    browser.quit()

    browser = init_browser()
    # Scrape table from Mars Facts Webpage.
    url3 = "https://space-facts.com/mars/"
    facts_table = pd.read_html(url3)
    # facts_table
    # type(facts_table)
    mars_facts_df = facts_table[0]
    mars_facts_df.columns = ["Description", "Mars"]
    # mars_facts_df
    mars_html_table = mars_facts_df.to_html()
    browser.quit()

    browser = init_browser()
    # Scrape titles and images of Mars hemispheres from USGS Webpage.
    url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url4)
    html4 = browser.html
    soup = BeautifulSoup(html4, 'html.parser')
    # Scrape titles of Mars hemispheres
    titles = soup.find_all('h3')
    new_titles = []
    for title in titles:
        new = str(title).replace("<h3>", "")
        new = str(new).replace("</h3>", "")
        new_titles.append(new)
    # new_titles

    # for hemisphere in mars_hemispheres:
    new_img_urls = []
    links = browser.find_by_tag('h3')
    links[0].click()

    for i in range(0, 4):
        browser.find_by_tag('h3')[i].click()
        sample = browser.links.find_by_text('Sample').first
        img_url = sample['href']
        new_img_urls.append(img_url)
        browser.back()
    browser.quit()
    # new_img_urls

    hemisphere_image_urls = []

    for i in range(len(new_titles)):
        hemisphere_image_url = {"title": new_titles[i],
                                "img_url": new_img_urls[i]}
        hemisphere_image_urls.append(hemisphere_image_url)

    mars_update = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_html_table": mars_html_table,
        "hemisphere_image_urls": hemisphere_image_urls
    }
    return mars_update
