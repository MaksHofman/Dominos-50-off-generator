import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
"""
mail = "https://www.youtube.com/"
"""
mail = "https://10minutemail.net/"

dominos = "https://dominospizza.pl/"

def open_10minutmail():
    driver = webdriver.Chrome()
    driver.get(mail)
    input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "fe_text")))
    value = input_element.get_attribute("value")
    ten_minut_mail_gen = value
    print(ten_minut_mail_gen)
    driver.execute_script("window.open('', '_blank');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(dominos)
    svg_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="aside"]/aside[3]/div/button')))
    svg_button.click()
    email_input = driver.find_element(By.ID, "Email")
    email_input.send_keys(ten_minut_mail_gen)
    checkbox = driver.find_element(By.XPATH, '//*[@id="main"]/div[4]/div[2]/div/form/div[2]/label/span')
    checkbox.click()
    button = driver.find_element(By.XPATH, '//*[@id="main"]/div[4]/div[2]/div/form/button')
    button.click()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(120)
    refresh_page_mail = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="left"]/ul/li[1]/a')))
    #refresh_page_mail.click()
    link_element = WebDriverWait(driver, 180).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="maillist"]/tbody/tr[2]/td[1]/a')))
    link_element.click()
    add_element = link_element = WebDriverWait(driver, 180).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="dismiss-button"]')))
    add_element.click()
    linkz_element = driver.find_element_by_xpath('//a[@href="http://infinity.emaillabs.info.pl/click/?lt=aHR0cHM6Ly93d3cuZG9taW5vc3BpenphLnBsL25ld3NsZXR0ZXIvY29uZmlybT9zdWJzY3JpcHRpb25oYXNoPTE4NzgxZjQ3NTBlNTdkNWJiNDliMTM0MTAwMThjZDc5MmEwNzU3ZWIyMjk5YTk5Zjc4ZmNmOTBiMWEyOTg5MTQmzgfOTMwODIwMjMwMTA0NDh8TUh4VWFIVXNJREF6SUVGMVp5QXlNREl6SURBeE9qQTFPakExSUNzd01qQXdmRzF4YnprMk5qQTNRRzl0WldsbExtTnZiWHd4TG1sdVptbHVhWFI1TG5OdGRIQjhjbVZrWjNKcFpEUTFmREI4TVM1bE0yRTBNalptTTJSbE5ERXhOV1prTkdaaFptWTBaV1ZrTWpGaE5UUXdNZz09"]')
    linkz_element.click()
    """
    first_link_to_dominos = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tab1"]/div[2]/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr/td[2]/table/tbody/tr/td/div[2]/table/tbody/tr[6]/td/table/tbody/tr/td/a')))
    first_link_to_dominos.click()
    """
    driver.switch_to.window(driver.window_handles[0])
    #refresh_page_mail.click()
    link_element.click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p[style="font-size:16px;font-weight:bold;text-align:center;"]')))
    text_to_save = element.text
    with open("dominos_cody.txt", "a") as file:
            file.write(text_to_save + "\n")

    time.sleep(400)
    driver.close()
    #//*[@id="dismiss-button"]/div/span
    #//*[@id="tab1"]/div[2]/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr/td[2]/table/tbody/tr/td/div[2]/table/tbody/tr[6]/td/p

open_10minutmail()