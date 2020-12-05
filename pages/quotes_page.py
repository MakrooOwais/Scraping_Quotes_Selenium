from typing import List
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions

from locators.quotes_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser


class QuotesPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self) -> List[QuoteParser]:
        return [
            QuoteParser(e) for e in self.browser.find_elements(
                By.CSS_SELECTOR,
                QuotesPageLocators.QUOTE
            )
        ]
            

    @property
    def author_dropdown(self) -> Select:
        element = self.browser.find_element(
            By.CSS_SELECTOR,
            QuotesPageLocators.AUTHOR_DROPDOWN
        )
        return Select(element)

    @property
    def tag_dropdown(self) -> Select:
        tag = self.browser.find_element(
            By.CSS_SELECTOR,
            QuotesPageLocators.TAG_DROPDOWN
        )
        return Select(tag)

    @property
    def search_button(self):
        button = self.browser.find_element(
            By.CSS_SELECTOR,
            QuotesPageLocators.SEARCH_BUTTON
        )
        return button

    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name)
        """WebDriverWait(self.browser, 5).until(
            expected_conditions.presence_of_all_elements_located(
                (By.CSS_SELECTOR, QuotesPageLocators.TAG_DROPDOWN_VALUE_OPTION)
            )
        )
"""
    def select_tag(self, tag_name: str):
        self.tag_dropdown.select_by_visible_text(tag_name)


    def get_available_tags(self):
        tags = [option.text.strip() for option in self.tag_dropdown.options]
        available_tags = [a for a in tags if a != '----------']
        return available_tags

    def ask_for_author(self):
        return input("Enter the name of the author you want quotes from: ")

    def ask_for_tag(self, tags):
        print('Available tags are: [{}]'.format(' | '.join(tags)))
        return input("Enter tag you want quotes from: ")
