from selenium import webdriver
from pages.quotes_page import QuotesPage

chrome = webdriver.Chrome('P:\\chromedriver.exe')
chrome.get('http://quotes.toscrape.com/search.aspx')
page = QuotesPage(chrome)

author = page.ask_for_author()
page.select_author(author_name=author)

tags = page.get_available_tags()
tag = page.ask_for_tag(tags)

page.select_tag(tag_name=tag)

page.search_button.click()

print(page.quotes)