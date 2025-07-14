from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

# Set up Chrome options (headless mode)
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

# Start Chrome and open the page
driver = webdriver.Chrome(options=options)
driver.get("https://www.inmotionhosting.com/vps-hosting")
time.sleep(3)  # Wait for the page to load

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

def get_feature_text(li):
    # Merge all text from <li> element
    return ' '.join(li.stripped_strings)

# Find all plan cards
cards = soup.find_all("div", class_="imh-rostrum-card")

plans = []
for card in cards:
    plan_name = card.find("h3", class_="imh-rostrum-card-title").get_text(strip=True)
    price_tag = card.find("span", class_="rostrum-price")
    price = price_tag.get_text(strip=True) if price_tag else None
    features = [get_feature_text(li) for li in card.select("ul.imh-rostrum-details-list li")]
    vcpu      = next((x for x in features if "vCPU" in x), None)
    ram       = next((x for x in features if "RAM" in x), None)
    ssd       = next((x for x in features if "SSD" in x), None)
    bandwidth = next((x for x in features if "Bandwidth" in x), None)
    ip        = next((x for x in features if "Dedicated IP" in x), None)
    plans.append({
        "Plan Name": plan_name,
        "Price ($/mo)": price,
        "vCPU": vcpu,
        "RAM": ram,
        "SSD": ssd,
        "Bandwidth": bandwidth,
        "Dedicated IP": ip
    })

# Convert to DataFrame
df = pd.DataFrame(plans)
df = df.fillna("")
print(df)