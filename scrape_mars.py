# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape():

    ############# Mars News #############
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL of page to be scraped
    url = 'https://www.redplanetscience.com'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    titles = soup.find_all('div', class_='content_title')

    title_list = []

    for title in titles:
        headline = title.text.strip()
    #     print(headline)
        title_list.append(headline)

    browser.quit()


    ############# JPL Mars Space Images #############
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL of page to be scraped
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    featured_image = soup.find('div', class_='floating_text_area')
    featured_image_url = url + featured_image.find("a")["href"]

    browser.quit()


    ############# Mars Facts #############
 
    # URL of page to be scraped
    url = 'https://galaxyfacts-mars.com/'

    tables_data = pd.read_html(url)
    table_df = tables_data[0]


    ############# Mars Hemispheres #############
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL of page to be scraped
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    hemisphere = soup.find_all('div', class_="description")

    url_list = []
    title_list = []

    # Creating a list of the hemisphere names/titles and their respective urls
    for hemi in hemisphere:
        a_href = hemi.find("a")
        ref = a_href["href"]
        link = url + ref
        url_list.append(link)
        
        h3 = hemi.find("h3")
        title = h3.text.split(" Hemisphere")[0]
        title_list.append(title)
    browser.quit()

    hoto_url_list = []

    # Creating a list of the images located on their respective pages.
    for link in url_list:
        executable_path = {'executable_path': ChromeDriverManager().install()}
        browser = Browser('chrome', **executable_path, headless=False)
        browser.visit(link)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        photo = soup.find('div', class_="downloads")
        photo_link = photo.find("a")["href"]
        photo_url = url + photo_link
        photo_url_list.append(photo_url)
        
        browser.quit()

    # Creating a dictionary of hemisphere names and urls to their respective photos
    hemisphere_image_urls = [    
        {"title":title_list[0], "img_url":photo_url_list[0]},
        {"title":title_list[1], "img_url":photo_url_list[1]},
        {"title":title_list[2], "img_url":photo_url_list[2]},
        {"title":title_list[3], "img_url":photo_url_list[3]}
    ]

    return hemisphere_image_urls