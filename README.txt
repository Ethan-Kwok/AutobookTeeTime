Automated Tee Time Reservation Script
This Python-based script automates the process of booking a tee time on the TeeItUp Golf website. It opens a browser, waits for the right time (9:00 PM EST when tee times open up), searches for available slots, and books a tee time for you. The program works for both Mac and PC with minimal setup, and it runs in the background with no need for user intervention after the initial setup.

Features:
- Automated Booking: The program allows you to log into your account and then books a tee time automatically.

- Wait for the Right Time: The script waits until 9:00 PM EST when tee time slots become available before starting to search.

- Customizable Course: You can select the desired golf course(s) that you would like to reserve.

- Customizable Date and Time: You can specify the earliest tee time you'd like to reserve (e.g., 9:00 AM). The program searches for available times on a given day within a 6-hour window, prioritizing the earliest available slot.

- No Installation Needed: Simply download the appropriate file for your operating system and run it without needing to install Python or any dependencies.

Supported Platforms:
- PC (Windows): Download the .exe file and run it.

- Mac: Download the .app file and run it.

Installation:
- Download the .exe (Windows) or .app (Mac) file:

Usage:
1. Double-click the .exe file (Windows) or .app file (Mac) to start the application.

2. Log In to Your Account: The program will open a Chrome browser window. Log in to your account on the booking site.

3. Enter Your Preferred Tee Time: After logging in, the program will prompt you to enter the earliest tee time you'd like to reserve (e.g., 9:00 AM). You can use the following formats: 9:00 AM, 9:00 am, 9:00AM, 9:00am

4. Wait for the Program to Work: The program will wait until 9:00 PM EST before starting the search. It will search for available slots and attempt to book the earliest valid one within a 6-hour window.

5. Reservation Complete: Once the program successfully books a tee time, it will notify you. After that, you can close the browser and the terminal.

Notes:
- Chrome is required: The program uses Chrome to interact with the booking website.

- Keep the browser open: While the script runs in the background, the Chrome browser must remain open. You can minimize it and do other things after logging in and entering the time.

- Timezone: The script uses EST (Eastern Standard Time) for timing. Make sure to adjust your system time accordingly.

Troubleshooting:
- If you encounter any issues, ensure you have the latest version of Chrome and the correct .exe or .app file for your system.

- The program will automatically retry the booking process in case of failure, but if the issue persists, consider checking the network or the website's availability. Also, ensure that you're logged in properly.

Example Output:
Hello! Loading Chrome...
DevTools listening on ___
Opened! Please LOG IN to your account!
Start time set to: 09:30 AM
Waiting until 9:00 PM
It's time! Running the script...
Tea times loaded! Time to search!
End time set to: 03:00 PM
Valid time found: 10:00 AM
Clicked BOOK NOW for 10:00 AM
Clicked 4 golfers button
Clicked add to cart
Clicked CHECKOUT
Agreed to Terms and Conditions
Clicked PURCHASE button!
Finished! Make sure the reservation has been made, then press Enter to close the browser...
Closing!

License:
- This software is provided under the MIT License. Feel free to use and modify it for personal or educational purposes.
