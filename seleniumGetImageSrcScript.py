from termcolor import colored
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

def clean_title(title):
    return (re.sub('_', ' ', title))


def get_image_src(title):

    title = clean_title(title)

    driver = webdriver.Chrome(executable_path = 'D:\\chromedriver.exe')

    driver.get('https://www.google.com/imghp?hl=fr')

    input = driver.find_element_by_name('q')
    input.send_keys(title) 
    input.send_keys(Keys.ENTER)

    x= driver.find_elements_by_class_name("mJxzWe").find_element_by_css_selector('div div div div div div span div div div a div img').get_attribute("src")
    print(colored(x, 'green'))

get_image_src("beIN_SPORTS_1Premium_Low")

# print(clean_title('beIN_SPORTS_1Premium_Low'))