from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=True)


def scrape_scan_image():
    browser.visit("https://spaceimages-mars.com/")
    browser.find_by_tag('button')[1].click()
    soup = bs(browser.html, 'html.parser')
    soup.find('img', class_='fancybox-image').get('src')
    img_url_rel = soup.find('img', class_='fancybox-image').get('src')
    img_url_abs = f'https://spaceimages-mars.com/{img_url_rel}'
    return img_url_abs

def scrape_mars_title():
    browser.visit("https://redplanetscience.com/")
    soup = bs(browser.html, 'html.parser')
    result = soup.find('div', class_='content_title')
    title = result.text
    return title

def scrape_mars_para():
    browser.visit("https://redplanetscience.com/")
    soup = bs(browser.html, 'html.parser')
    result = soup.find('div', class_='article_teaser_body')
    para = result.text
    return para

