import requests
import re

def scrapable(url):
    try:
        # Check if robots.txt allows scraping
        robots_txt = requests.get(url + '/robots.txt').text
        if "Disallow:" in robots_txt:
            print("The website does not allow scraping.")
            return False
        
        # Send a request to the URL
        response = requests.get(url)
        
        # Check if the response status code is 200
        if response.status_code != 200:
            print(f"The website returned a response status code of {response.status_code}, which indicates that the website is not scraping friendly.")
            return False
        
        # Check if the website's terms of use allow scraping
        terms_of_use = re.search(r'Terms of Use', response.text)
        if terms_of_use is None:
            print("The terms of use of the website do not mention anything about web scraping.")
            return True
        
        # Check if the terms of use allow scraping
        if "prohibited" in terms_of_use.group(0):
            print("Web scraping is prohibited according to the terms of use of the website.")
            return False
        
        print("The website is scraping friendly.")
        return True
        
    except Exception as e:
        print(f"An error occurred while checking the scraping friendliness of the website: {e}")
        return False
