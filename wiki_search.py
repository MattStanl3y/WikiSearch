import requests
from bs4 import BeautifulSoup

def menu(): 
    print("\nWelcome to Wiki_Search!")
    print("----------------------------\n")

def getUserInput():
    return input("Enter Topic you would like to search for: ")

def constructWikipediaUrl(user_input):
    words = user_input.split()
    capitalized_words = [word.capitalize() for word in words]
    formatted_input = '_'.join(capitalized_words)
    return f'https://en.wikipedia.org/wiki/{formatted_input}'

def getInfo(url):
        page = requests.get(url)

        page_html = BeautifulSoup(page.content, 'html.parser')
        
        main_content = page_html.find('div', class_="mw-content-ltr")
        
        if main_content:
            paragraphs = main_content.find_all('p')
            
            for p in paragraphs:
                if p.text.strip():
                    return p.text.strip()
            
            return "No information found."
        else:
            return "Page structure not recognized."

def main():
    menu()
    keep_searching = True
    while keep_searching:
        user_input = getUserInput()
        url = constructWikipediaUrl(user_input)
        info = getInfo(url)
        print(f"\nInfo on '{user_input}':\n\n{info}\n")
        
        loop = input("Keep Searching? (y/n): ").lower()
        if loop != 'y':
            keep_searching = False

    print("Thank you for using Wikipedia_Search!\n")

if __name__ == "__main__":
    main()
