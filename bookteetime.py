from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import time
import pytz
import sys

print("Start!")

# Get today's date
today = datetime.today()
formatted_date = today + timedelta(weeks=1)
print(f"Booking date set to: {formatted_date.date()}")

# Prompt the user for earliest start time
user_start_time = input("Please enter the earliest start time (e.g., 9:00 AM): ")
user_start_time = user_start_time.replace(" ", "").upper()
# Validate the time format
try:
    start_time = datetime.strptime(user_start_time, "%I:%M%p")  # Parses times like '9:00AM'
    print(f"Start time set to: {start_time.strftime('%I:%M %p')}")
except ValueError:
    print(f"{user_start_time} is invalid! Please use the format 'HH:MM AM/PM' (e.g., 9:00 AM)")
    sys.exit()

# Wait until this time to start running the code
TARGET_HOUR = 21
TARGET_MINUTE = 00
est = pytz.timezone('America/New_York')

def format_time_diff(time_diff):
    h, m, s = int(time_diff) // 3600, (int(time_diff) % 3600) // 60, int(time_diff) % 60
    return " and ".join(f"{v} {n}{'s' * (v != 1)}" for v, n in [(h, "hr"), (m, "min"), (s, "sec")] if v)

def wait_until_target_time():
    while True:
        now = datetime.now(est)
        target_time = now.replace(hour=TARGET_HOUR, minute=TARGET_MINUTE, second=0, microsecond=0)

        if now >= target_time:
            print("It's time! Running the script...")
            break  # Exit loop to execute your script

        # Calculate sleep duration
        time_diff = (target_time - now).total_seconds()

        if time_diff > 3600:  # If more than an hour away, sleep for 30 minutes
            sleep_duration = 1800
            print(format_time_diff(time_diff), "until target time.")
        elif time_diff > 600:  # If more than 10 minutes away, sleep for 5 minutes
            sleep_duration = 300
            print(format_time_diff(time_diff), "until target time.")
        elif time_diff > 60:  # If more than 1 minute away, sleep for 30 seconds
            sleep_duration = 30
            print(format_time_diff(time_diff), "until target time.")
        else: # If within 1 minute, don't sleep
            sleep_duration = 0    
        time.sleep(sleep_duration)

print("Waiting until", datetime.strptime(f"{TARGET_HOUR}:{TARGET_MINUTE}", "%H:%M").strftime("%I:%M %p"))
wait_until_target_time()

# Open the page
base_url = "https://somerset-group-v2.book.teeitup.golf/?course=7092,7084,7094&date={}&golfers=4&holes=18&max=9999".format(formatted_date)
chrome_options = webdriver.ChromeOptions()
chrome_options.debugger_address = "localhost:9222"
driver = webdriver.Chrome(options=chrome_options)
driver.get(base_url)

# Wait for the tea time slots to be present on the page (i.e. page load)
WebDriverWait(driver, 30).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "p[data-testid='teetimes-tile-time']"))
)

print("Tea times loaded! Time to search!")

# Find all tea time slots using CSS selector
time_slots = driver.find_elements(By.CSS_SELECTOR, "p[data-testid='teetimes-tile-time']")

# Latest possible time is 2 hours after start time
end_time = start_time + timedelta(hours=2)
print(f"End time set to: {end_time.strftime('%I:%M %p')}")

# Search for a valid tea time
for slot in time_slots:
    time_text = slot.text.strip()
    # Convert string time to a datetime object for comparison
    time_obj = datetime.strptime(time_text, "%I:%M %p")  # Parses times like '9:20 AM'

    # Check if time is in range
    if start_time <= time_obj <= end_time:
        print(f"Valid time found: {time_text}")
        parent_container = slot.find_element(By.XPATH, "./ancestor::div[contains(@class, 'css-1d3bbye')]")
        book_button = parent_container.find_element(By.CSS_SELECTOR, "button[data-testid='teetimes_book_now_button']")
        book_button.click()  # Click the button to book
        print(f"Clicked BOOK NOW for {time_text}!")

        # Wait for "ADD TO CART" button to appear
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[data-testid='golfer-select-radio-4']"))
        )
        four_golfers_button = driver.find_element(By.CSS_SELECTOR, "input[data-testid='golfer-select-radio-4']")
        four_golfers_button.click()
        print(f"Clicked 4 golfers button")
        add_to_card_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='add-to-cart-button']")
        add_to_card_button.click()
        print(f"Clicked add to cart button")

        # Wait for "CHECKOUT" button to appear
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[data-testid='shopping-cart-drawer-checkout-btn']"))
        )
        checkout_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='shopping-cart-drawer-checkout-btn']")
        checkout_button.click()

        # Wait for "I agree to Terms and Conditions" button to appear
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[name='chb-nm']"))
        )
        terms_conditions_button = driver.find_element(By.CSS_SELECTOR, "input[name='chb-nm']")
        terms_conditions_button.click()
        purchase_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='make-your-reservation-btn']")
        purchase_button.click()

        break  # Stop after booking one slot

print("ok done :D")
