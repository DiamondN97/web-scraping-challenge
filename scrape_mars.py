	#!/usr/bin/env python
	# coding: utf-8

	# # Part One: Scrape NASA
	# Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. 
	# Assign the text to variables to reference later.



	#Import dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
import time





def scrape():


	conn = 'mongodb://localhost:27017'
	client = pymongo.MongoClient(conn)




	db = client.mars_db
	collection = db.news
	mars_news = db.news.find()





	url = 'https://mars.nasa.gov/news/'

	# Retrieve page with the requests module
	response = requests.get(url)
	# Create BeautifulSoup object; parse with 'lxml'
	soup = bs(response.text, 'lxml')




	headlines = soup.find_all('div', class_='content_title')
	latest_headline = headlines[0].text
	latest_headline = latest_headline.strip()
	latest_headline





	article = soup.find_all('div', class_='image_and_description_container')
	# paragraph

	latest_paragraph = article[0]
	latest_paragraph = latest_paragraph.find('div', class_='rollover_description_inner')
	latest_paragraph = latest_paragraph.text.strip()
	latest_paragraph




	mars_news_dict = {
	    "latest_headline": latest_headline,
	    "latest_paragraph": latest_paragraph
	}

	db.news.insert_one(mars_news_dict)


	# # Part Two: Scrape JPL for featured image
	# Visit the url for JPL Featured Space Image here. 
	# Use splinter to navigate the site and 
	# Find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.



	executable_path = {'executable_path': r'C:\Users\diamo\Bootcamp\chromedriver.exe'}
	browser = Browser('chrome', **executable_path, headless=False)




	url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
	browser.visit(url)
	browser.click_link_by_partial_text('FULL IMAGE')
	time.sleep(5)
	browser.click_link_by_partial_text('more info')




	html = browser.html
	soup = bs(html, 'html.parser')
	image_url = soup.find('figure', class_='lede').a['href']
	image_url




	base_url = 'https://www.jpl.nasa.gov'
	full_image_url = base_url + image_url
	full_image_url




	image = {
	    "full_image_url": full_image_url
	}
	#Put into db w/its own collection? 
	db.image.insert_one(image)


	# # Mars Facts
	# Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
	# Use Pandas to convert the data to a HTML table string.



	mars_url = 'https://space-facts.com/mars/'
	mars_facts = pd.read_html(mars_url)[0]
	# mars_facts
	mars_facts_html = mars_facts.to_html()
	mars_facts_html


	# # Part 4: Mars Hemispheres
	# 
	# Visit the USGS Astrogeology site here to obtain high resolution images for each of Mars' hemispheres.
	# 
	# Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere
	# 
	# * Cerberus
	# * Valles Marineris
	# * Schiaparelli 
	# * Syrtis Major
	# 



	hemisphere_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
	response = requests.get(hemisphere_url)
	soup = bs(response.text, 'lxml')




	cerberus_title = soup.find('title').text
	cerberus_title = cerberus_title.split('|')
	cerberus_title = cerberus_title[0]
	cerberus_title




	cerberus_hemisphere = soup.find_all('div', class_= 'wide-image-wrapper')
	cerberus_hemisphere = cerberus_hemisphere[0]
	cerberus_hemisphere = cerberus_hemisphere.find_all('img', class_='wide-image')
	cerberus_hemisphere = cerberus_hemisphere[0]
	cerberus_hemisphere = cerberus_hemisphere['src']
	# cerberus_hemisphere




	base_url = 'https://astrogeology.usgs.gov/'
	cerberus_full_url = base_url + cerberus_hemisphere
	# cerberus_full_url
	hemisphere_image_urls = [
	    {"title": cerberus_title, "img_url": cerberus_full_url}
	]




	url2 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
	response = requests.get(url2)
	soup = bs(response.text, 'lxml')




	valles_title = soup.find('title').text
	valles_title = valles_title.split('|')
	valles_title = valles_title[0]




	valles_hemisphere = soup.find_all('div', class_= 'wide-image-wrapper')
	valles_hemisphere = valles_hemisphere[0]
	valles_hemisphere = valles_hemisphere.find_all('img', class_='wide-image')
	valles_hemisphere = valles_hemisphere[0]
	valles_hemisphere = valles_hemisphere['src']
	# valles_hemisphere




	valles_full_url = base_url + valles_hemisphere
	# valles_full_url
	hemisphere_image_urls.append({"title": valles_title, "img_url": valles_full_url})




	hemisphere_image_urls




	url3 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
	response = requests.get(url3)
	soup = bs(response.text, 'lxml')




	schiaparelli_title = soup.find('title').text
	schiaparelli_title = schiaparelli_title.split('|')
	schiaparelli_title = schiaparelli_title[0]
	# schiaparelli_title




	schiaparelli_hemisphere = soup.find_all('div', class_= 'wide-image-wrapper')
	schiaparelli_hemisphere = schiaparelli_hemisphere[0]
	schiaparelli_hemisphere = schiaparelli_hemisphere.find_all('img', class_='wide-image')
	schiaparelli_hemisphere = schiaparelli_hemisphere[0]
	schiaparelli_hemisphere = schiaparelli_hemisphere['src']
	# schiaparelli_hemisphere




	schiaparelli_full_url = base_url + schiaparelli_hemisphere
	# schiaparelli_full_url
	hemisphere_image_urls.append({"title": schiaparelli_title, "img_url": schiaparelli_full_url})




	hemisphere_image_urls




	url4 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
	response = requests.get(url4)
	soup = bs(response.text, 'lxml')




	syrtis_title = soup.find('title').text
	syrtis_title = syrtis_title.split('|')
	syrtis_title = syrtis_title[0]
	# syrtis_title




	syrtis_hemisphere = soup.find_all('div', class_= 'wide-image-wrapper')
	syrtis_hemisphere = syrtis_hemisphere[0]
	syrtis_hemisphere = syrtis_hemisphere.find_all('img', class_='wide-image')
	syrtis_hemisphere = syrtis_hemisphere[0]
	syrtis_hemisphere = syrtis_hemisphere['src']
	# syrtis_hemisphere




	syrtis_full_url = base_url + syrtis_hemisphere
	syrtis_full_url
	hemisphere_image_urls.append({"title": syrtis_title, "img_url": syrtis_full_url})



	# hemisphere_image_urls
	mars_info_dict = {
	    "latest_headline": latest_headline,
	    "latest_paragraph": latest_paragraph,
	    "full_image_url": full_image_url,
	    "mars_facts_html": mars_facts_html,
	    # "hemisphere_images": hemisphere_image_urls

	    }
	mars_info_dict
	db.mars_info_dict.insert_one(mars_info_dict)



	# def scrape_2(): 
	# executable_path = {'executable_path': r'C:\Program Files\Chromedriver\chromedriver.exe'}
	# browser = Browser('chrome', **executable_path, headless=False)
	# nasa_news_url = 'https://mars.nasa.gov/news/'
	# # Retrieve page with the requests module
	# news_response = requests.get(nasa_news_url)
	# time.sleep(5)
	# browser.quit()

	# Retrieve page with the requests module


	# hemisphere_image_urls = hemisphere_image_urls


