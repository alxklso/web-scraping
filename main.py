# program for testing basic web scraping capabilities


# libraries 
import webbrowser, os, requests

def displayMenu():
    print('''
    1. Google something
    2. Search Google Maps
    3. Check weather
    4. Open App
    5. Download Webpage
    ''')

def openInChrome(url): 
    # this function takes a URL as an input parameter and opens it
    # in Google Chrome
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open(url)

def googleSomething():
    # this function asks the user what they would like to Google
    # and then searches Google for it by calling the openInChrome function
    google = "http://google.com/search?q=" 
    search = list(input("What would you like to Google? ").split())

    # appending words to google url
    google += search[0]
    for i in search[1::]:
        google+= "+" + i

    openInChrome(google)    # pass google URL through openInChrome function
    
def googleMaps():
    # this function takes an address or location as input and searches
    # it on Google Maps
    url = "http://google.com/maps/place/"
    address = list(input("Please enter an address: ").split())

    # appending words to google url
    url += address[0]
    for i in address[1::]:
        url+= "+" + i

    openInChrome(url)

def checkWeather():
    # this function takes a location as input and search
    # for the current weather on Google
    url = "http://google.com/search?q="
    location = list(input("Enter a location to check its weather: ").split())

    # appending location to weather.com ten-day forecast URL
    url += location[0]
    for i in location[1::]:
        url += "+" + i
    url += "+weather"

    openInChrome(url)

def openApp():
    # this function allows the user to open an array of apps
    # on the MacOS
    print('''
    1. Music
    2. Mail
    3. Messages
    4. Discord
    ''')
    choice = input("Which app would you like to open? ")

    if choice == '1':
        os.system("open /System/Applications/Music.app")
    elif choice == '2':
        os.system("open /System/Applications/Mail.app")
    elif choice == '3':
        os.system("open /System/Applications/Messages.app")
    elif choice == '4':
        os.system("open /System/Applications/FaceTime.app")

def downloadAndSaveWebPage():
    # this functions attempts to download and save a text file from online
    # if the file doesn't download, an exception is raised. 
    # otherwise the file is written into a text file and saved on the local drive.
    req = requests.get('http://automatetheboringstuff.com/files/rj.txt')

    try:
        req.raise_for_status()
    except Exception as exc:
        print('There was a problem: ' + str(exc))

    playFile = open('RomeoAndJuliet.txt', 'wb')

    for chunk in req.iter_content(200000):
        playFile.write(chunk)

    print("The file was successfully downloaded and saved.")
    playFile.close()


# main program
def main():
    displayMenu()
    choice = input("Please select an option from the menu: ")

    if choice == '1':
        googleSomething()
    elif choice == '2':
        googleMaps()
    elif choice == '3':
        checkWeather()
    elif choice == '4':
        openApp()
    elif choice == '5':
        downloadAndSaveWebPage()


# call main
main()
