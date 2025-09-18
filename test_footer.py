from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://only.digital/")

footer = driver.find_element(By.TAG_NAME, "footer")
assert footer.is_displayed()

driver.find_element(By.CSS_SELECTOR, "footer a[href*='behance.net']").is_displayed()
driver.find_element(By.XPATH, "//footer//*[text()='Начать проект']").is_displayed()

print("✅ Тест успешно пройден")
driver.quit()
