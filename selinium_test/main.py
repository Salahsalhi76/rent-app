from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=chrome_options)
browser.get("http://localhost:3000/login")
loginBtn = browser.find_element(By.CSS_SELECTOR, "#signInDiv")
loginBtn.click()
browser.switch_to.window(browser.window_handles[1])
WebDriverWait(browser, 15).until(EC.url_changes("http://localhost:3000/"))

url = browser.current_url
email = browser.find_element(By.CSS_SELECTOR, "#identifierId")
email.send_keys("tpigltest@gmail.com")
browser.find_element(By.CSS_SELECTOR, "#identifierNext > div > button").click()
WebDriverWait(browser, 1500).until(EC.url_changes(url))
browser.implicitly_wait(124)
password = browser.find_element(By.CSS_SELECTOR, "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
password.send_keys("Bilelsef")
url = browser.current_url
browser.find_element(By.CSS_SELECTOR, "#passwordNext > div > button").click()

WebDriverWait(browser, 150).until(EC.url_changes(url))
browser.switch_to.window(browser.window_handles[0])

browser.find_element(By.CSS_SELECTOR, "#root > div > div.body > div.body_content > div.body_right_space > button").click()
url = browser.current_url

#browser.find_element(By.CSS_SELECTOR,"body > div.MuiDialog-root.MuiModal-root.css-zw3mfo-MuiModal-root-MuiDialog-root > div.MuiDialog-container.MuiDialog-scrollPaper.css-hz1bth-MuiDialog-container > div > div > div.add_home_content > input:nth-child(3)").click()
browser.implicitly_wait(124)
browser.find_element(By.CSS_SELECTOR, "body > div.MuiDialog-root.MuiModal-root.css-zw3mfo-MuiModal-root-MuiDialog-root > div.MuiDialog-container.MuiDialog-scrollPaper.css-hz1bth-MuiDialog-container > div > div > div.add_home_content > input:nth-child(3)").send_keys("title test")
browser.find_element(By.CSS_SELECTOR, "body > div.MuiDialog-root.MuiModal-root.css-zw3mfo-MuiModal-root-MuiDialog-root > div.MuiDialog-container.MuiDialog-scrollPaper.css-hz1bth-MuiDialog-container > div > div > div.add_home_content > textarea:nth-child(5)").send_keys("description test")
browser.find_element(By.CSS_SELECTOR, "body > div.MuiDialog-root.MuiModal-root.css-zw3mfo-MuiModal-root-MuiDialog-root > div.MuiDialog-container.MuiDialog-scrollPaper.css-hz1bth-MuiDialog-container > div > div > div.add_home_content > input[type=number]:nth-child(8)").send_keys("555")
browser.find_element(By.CSS_SELECTOR, "body > div.MuiDialog-root.MuiModal-root.css-zw3mfo-MuiModal-root-MuiDialog-root > div.MuiDialog-container.MuiDialog-scrollPaper.css-hz1bth-MuiDialog-container > div > div > div.add_home_content > div:nth-child(6) > div:nth-child(4) > input[type=number]").send_keys("100")

browser.find_element(By.CSS_SELECTOR, "body > div.MuiDialog-root.MuiModal-root.css-zw3mfo-MuiModal-root-MuiDialog-root > div.MuiDialog-container.MuiDialog-scrollPaper.css-hz1bth-MuiDialog-container > div > div > div.add_home_content > div:nth-child(10) > div:nth-child(1) > select").send_keys("Alger")
browser.find_element(By.CSS_SELECTOR, "body > div.MuiDialog-root.MuiModal-root.css-zw3mfo-MuiModal-root-MuiDialog-root > div.MuiDialog-container.MuiDialog-scrollPaper.css-hz1bth-MuiDialog-container > div > div > div.add_home_content > div:nth-child(10) > div:nth-child(2) > select").send_keys("Baraki")
browser.find_element(By.CSS_SELECTOR, "body > div.MuiDialog-root.MuiModal-root.css-zw3mfo-MuiModal-root-MuiDialog-root > div.MuiDialog-container.MuiDialog-scrollPaper.css-hz1bth-MuiDialog-container > div > div > div.add_home_content > input:nth-child(13)").send_keys("salhi salah eddine")
browser.find_element(By.CSS_SELECTOR, "body > div.MuiDialog-root.MuiModal-root.css-zw3mfo-MuiModal-root-MuiDialog-root > div.MuiDialog-container.MuiDialog-scrollPaper.css-hz1bth-MuiDialog-container > div > div > div.add_home_content > textarea:nth-child(15)").send_keys("Baraki alger")
browser.find_element(By.CSS_SELECTOR, "body > div.MuiDialog-root.MuiModal-root.css-zw3mfo-MuiModal-root-MuiDialog-root > div.MuiDialog-container.MuiDialog-scrollPaper.css-hz1bth-MuiDialog-container > div > div > div.add_home_content > div:nth-child(16) > div:nth-child(1) > input[type=email]").send_keys("ks_salhi@esi.dz")
browser.find_element(By.CSS_SELECTOR, "body > div.MuiDialog-root.MuiModal-root.css-zw3mfo-MuiModal-root-MuiDialog-root > div.MuiDialog-container.MuiDialog-scrollPaper.css-hz1bth-MuiDialog-container > div > div > div.add_home_content > div:nth-child(16) > div:nth-child(2) > input[type=phone]").send_keys("0555555555")
browser.find_element(By.CSS_SELECTOR, "body > div.MuiDialog-root.MuiModal-root.css-zw3mfo-MuiModal-root-MuiDialog-root > div.MuiDialog-container.MuiDialog-scrollPaper.css-hz1bth-MuiDialog-container > div > div > div.add_home_content > div:nth-child(6) > div:nth-child(3) > input[type=number]").send_keys("5")
browser.find_element(By.CSS_SELECTOR, "body > div.MuiDialog-root.MuiModal-root.css-zw3mfo-MuiModal-root-MuiDialog-root > div.MuiDialog-container.MuiDialog-scrollPaper.css-hz1bth-MuiDialog-container > div > div > div.add_home_content > div:nth-child(6) > div:nth-child(3) > input[type=number]").send_keys("5")

browser.implicitly_wait(100)

shareBtn = browser.find_element(By.CSS_SELECTOR, "body > div.MuiDialog-root.MuiModal-root.css-zw3mfo-MuiModal-root-MuiDialog-root > div.MuiDialog-container.MuiDialog-scrollPaper.css-hz1bth-MuiDialog-container > div > div > div.addhome_appbar > button")
shareBtn.click()

