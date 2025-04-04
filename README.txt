SETTING UP AND RUNNING THE TEE TIME BOOKING SCRIPT

1. INSTALL NECESSARY PYTHON AND DEPENDENCIES (Only needed once)
  - Install the latest version of Python (3.13.2 as of April 2025):
  https://www.python.org/downloads/

  - Download the "bookteetime.py" file above.

  - Open Command Prompt (Windows) or Terminal (Mac) and run the following command:
  pip3 install selenium pytz

2. OPEN DEBUG MODE ON GOOGLE CHROME
  WINDOWS
  - Run the following command in Command Prompt:
  "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\selenium_session"

  MAC
  - Run the following command in Terminal:
  /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/Users/YOUR_USERNAME/selenium_session"
  - (Replace `YOUR_USERNAME` with your actual Mac username.)

3. OPEN THE TEE TIME WEBSITE AND LOG IN
  - Manually navigate to the tee time booking website and log in.
  https://somerset-group-v2.book.teeitup.com/

4. RUN THE CODE
  - In the Command Prompt or Terminal, CD into the folder containing the bookteetime.py script. For example, if you downloaded it to your Downloads folder, run:
  cd downloads

  - In the Command Prompt or Terminal, run the Python script:
  python3 bookteetime.py

5. ENTER THE START TIME WHEN PROMPTED
  - The code will prompt you with instructions in the Command Prompt or Terminal.
  - Acceptable time formats: "9:00 AM", "9:00 am", "9:00AM", "9:00am"

6. KEEP CHROME OPEN AND WAIT!
  - Leave the Google Chrome tab open.
  - Keep the Chrome window enlarged to ensure automation runs smoothly.
  - At 9:00 PM EST, the automation will run. Once complete, the code will return "ok done :D"
