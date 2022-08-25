# ***
# Discord Test Task
# Used Selenium in order to fill registration form. Unfortunately didn't manage to solve issue with captcha.
# After captcha phase, there is landing page that requires phone number confirmation.

import requests
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from password_gen import generate_random_password


print('*' * 100)
print('Enter email:')
type_email = input()
print('Enter username:')
type_username = input()

gen_password = generate_random_password()

driver = webdriver.Chrome(ChromeDriverManager().install())
browser = webdriver.Chrome()
browser.get(('https://discord.com/register'))

mail = browser.find_element(By.NAME, 'email')
mail.send_keys(type_email)
username = browser.find_element(By.NAME, 'username')
username.send_keys(type_username)
password = browser.find_element(By.NAME, 'password')
password.send_keys(gen_password)

birthdate_month = browser.find_element(By.ID, 'react-select-2-input')
birthdate_month.send_keys("january")

birthdate_day = browser.find_element(By.ID, 'react-select-3-input')
birthdate_day.send_keys("1")

birthdate_year = browser.find_element(By.ID, 'react-select-4-input')
birthdate_year.send_keys("1990")

nextButton = browser.find_element(
    By.XPATH,
    '//button[@type="submit"]'
)
nextButton.click()

# Time to solve captcha manually
time.sleep(30)


# Tested on my own discord account following code. Successfully obtained token.
# [captcha_required] error occurs

payload = {
    'login': type_email,
    'password': gen_password
}

headers = {
    'Content-type': 'application/json'
}

r = requests.post('https://discord.com/api/v9/auth/login', headers=headers, json=payload)
print(r.text.split()[1].replace(',', '').replace("\"", ''))
