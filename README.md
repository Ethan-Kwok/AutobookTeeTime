# 🏌️ Automated Tee Time Reservation Script

This Python-based script automates the process of booking a tee time on the [Somerset TeeItUp Golf website](https://somerset-group-v2.book.teeitup.com/teetimes).  
It opens a browser, waits for the right time (9:00 PM EST when tee times open up), searches for available slots, and books a tee time for you.  
The program works for both Mac and PC with minimal setup, and it runs in the background with no need for user intervention after the initial setup.

---

## ✅ Features

- **Automated Booking**: Log into your account, and the script will book a tee time automatically.
- **Wait for the Right Time**: Waits until 9:00 PM EST before starting the search.
- **Customizable Course**: Choose your preferred golf course(s) to reserve.
- **Customizable Date and Time**: Specify the earliest tee time (e.g., 9:00 AM); searches within a 6-hour window for the earliest available slot.
- **No Installation Needed**: Just download and run — no Python or dependencies required.

---

## 💻 Supported Platforms

- 🖥️ **PC (Windows)**: Download the `.exe` file and run it.
- 🍎 **Mac**: Download the `.app` file and run it.

---

## 📦 Installation

- Download the `.exe` (Windows) or `.app` (Mac) file from the **Releases** section.

---

## 🚀 Usage

1. **Run the App**  
   Double-click the `.exe` (Windows) or `.app` (Mac) file to start the application.

2. **Log In to Your Account**  
   A Chrome browser window will open. Log in to your account on the booking site.

3. **Enter Your Preferred Tee Time**  
   After logging in, enter the earliest tee time you'd like to reserve.  
   Accepted formats: `9:00 AM`, `9:00 am`, `9:00AM`, `9:00am`

4. **Let the Program Work**  
   The script will wait until 9:00 PM EST before beginning the search and booking process.  
   It will attempt to reserve the earliest available slot within a 6-hour window.

5. **Reservation Complete**  
   Once successful, the script will notify you. You can then close the browser and the terminal.

---

## 📎 Notes

- **Chrome is required**: The script uses Chrome to interact with the booking website.
- **Keep the browser open**: Chrome must stay open while the script runs. You can minimize it after login.
- **Timezone**: The script uses **EST (Eastern Standard Time)**. Adjust your system clock accordingly.

---

## 🛠️ Troubleshooting

- Ensure you're using the latest version of Chrome.
- Use the correct `.exe` or `.app` for your system.
- The script automatically retries in case of failure.
- Check your internet connection and confirm that you're logged in.

---

## 🖥️ Example Output

```plaintext
Hello! Loading Chrome...
DevTools listening on ___
Opened! Please LOG IN to your account!
Start time set to: 09:30 AM
Waiting until 9:00 PM
It's time! Running the script...
Tee times loaded! Time to search!
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
```

---

## 📄 License

This software is provided under the MIT License.
Feel free to use and modify it for personal or educational purposes.
