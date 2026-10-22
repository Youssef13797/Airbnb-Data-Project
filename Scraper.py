import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--headless") 
options.add_argument("--window-size=1920,1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

cities = ["Amsterdam", "Athens", "Barcelona", "Berlin", "Budapest", "Lisbon", "London", "Paris", "Rome", "Vienna"]
all_data = []

for city in cities:
    print(f"Scraping data for {city}...")

    url = f"https://www.airbnb.com/s/{city}--Netherlands/homes?room_types%5B%5D=Entire+home%2Fapt&min_bedrooms=2"
    driver.get(url)
    time.sleep(4) 
    
    try:
        cards = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="card-container"]')
        
        for card in cards[:50]:
            try:
                
                name = card.find_element(By.CSS_SELECTOR, '[data-testid="listing-card-title"]').text
                
                price_text = card.find_element(By.CSS_SELECTOR, '[data-testid="price-availability-row"]').text
                price = float(price_text.replace('€', '').replace(',', '').split()[0])
                
                
                link = card.find_element(By.TAG_NAME, 'a').get_attribute('href')
                
                
                try:
                    rating = card.find_element(By.CSS_SELECTOR, 'span[aria-label*="rating"]').text.split()[0]
                except:
                    rating = None
                
                all_data.append({
                    "city": city,
                    "property_name": name,
                    "price": price,
                    "rating": rating,
                    "url": link
                })
            except Exception as e:
                continue
                
    except Exception as e:
        print(f"Couldn't load cards for {city}, skipping...")

df = pd.DataFrame(all_data)
df.to_csv("airbnb_listings.csv", index=False, encoding="utf-8-sig")
print("Scraping done! Data saved to airbnb_listings.csv")
driver.quit()