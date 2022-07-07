# program for testing basic web scraping capabilities
# libraries 
import webbrowser, sys

def displayMenu():
    print('''
    1. Google something
    2. Search Google Maps
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
    maps = "http://google.com/maps/place/"
    address = list(input("Please enter an address: ").split())

    # appending words to google url
    maps += address[0]
    for i in address[1::]:
        maps+= "+" + i

    openInChrome(maps)

# main program
def main():
    displayMenu()
    choice = input("Please select an option from the menu: ")

    if choice == "1":
        googleSomething()
    elif choice == "2":
        googleMaps()

# call main
main()
