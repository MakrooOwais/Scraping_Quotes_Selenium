from selenium import webdriver
from pages.quotes_page import QuotesPage

firefox = webdriver.Firefox(executable_path = 'C:\\Users\\Owais Mohammad\\PythonProjects\\geckodriver.exe')
firefox.get('http://quotes.toscrape.com/search.aspx')
page = QuotesPage(firefox)

author = page.ask_for_author()
page.select_author(author_name=author)

tags = page.get_available_tags()
tag = page.ask_for_tag(tags)

page.select_tag(tag_name=tag)

page.search_button.click()

print(page.quotes)