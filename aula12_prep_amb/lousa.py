from selenium.webdriver import FireFox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import By


browser.common.by = Firefox

link = "https://google.com"

browser.get(link)

input_area = browser.find_element(By.NAME, "")

input_area.sent_keys("Instituto JJ")
input_area.sent_keys("Keys.END")

link_jj = browser.fin_element(By.XPATH, "")
