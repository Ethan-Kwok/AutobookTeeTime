SETTING UP AND RUNNING THE TEE TIME BOOKING SCRIPT

1. INSTALL NECESSARY DEPENDENCIES (Only needed once)
Open Command Prompt and run the following commands:

pip install selenium
pip install pytz

2. OPEN DEBUG MODE ON GOOGLE CHROME
WINDOWS
Run the following command in Command Prompt:
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\selenium_session"

MAC
Run the following command in Terminal:
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/Users/YOUR_USERNAME/selenium_session"
(Replace `YOUR_USERNAME` with your actual Mac username.)

3. OPEN THE TEE TIME WEBSITE AND LOG IN
Manually navigate to the tee time booking website and log in.

https://somerset-group-v2.book.teeitup.com/

4. RUN THE CODE
Run the Python script below:
python bookteetime.py
(Replace `bookteetime.py` with the correct file name, or click the "Run" button if available.)

5. ENTER THE START TIME WHEN PROMPTED
Acceptable formats: "9:00 AM", "9:00 am", "9:00AM", "9:00am"

6. KEEP CHROME OPEN
- Leave the Google Chrome tab open.
- Keep the Chrome window enlarged to ensure automation runs smoothly.
