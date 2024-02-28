# README
## oncoo.de Admin Area Scanner

This Python script continuously generates random IDs and checks if they lead to specific admin pages on the website oncoo.de. 
If a specific admin page is not found, it records the URL and opens it in the web browser. Additionally, it sends requests to a specific API endpoint to create new cards with predefined text.

### Requirements
- Python 3.x
- Requests library (`pip install requests`)

### How to Use
1. Install the Requests library using `pip install requests` if you haven't already.
2. Run the script.
3. The script will continuously generate random IDs and check if they lead to specific pages on the website.
4. If a page is not one of the specific ones, the script records the URL and opens it in the web browser.
5. Requests are sent to a specific API endpoint to create new cards with the predefined text.

### Disclaimer
This script is for educational purposes only. Use it responsibly and only on websites where you have permission to perform such actions.
