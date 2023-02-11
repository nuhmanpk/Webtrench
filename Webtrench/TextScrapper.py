import requests
from bs4 import BeautifulSoup
# from helper import is_scrapable

class TextScrapper:

    def text_from_url(url):
        try:

            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            text = soup.get_text()
            return text
        except Exception as e:
            print(f"An error occurred while trying to extract text from the URL {url}: {e}")
            return None
    
    def text_from_file(file):
        try:
            with open(file, 'r') as f:
                text = f.read()
            return text
        except Exception as e:
            print(f"An error occurred while trying to extract text from the file {file}: {e}")
            return None

    def text_from_html(html):
        try:    
            soup = BeautifulSoup(html, 'html.parser')
            text = soup.get_text()
            return text
        except Exception as e:
            print(f"An error occurred while trying to extract text from the HTML: {e}")
            return None
            
    def paragraph_from_url(url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            paragraphs = soup.find_all('p')
            return paragraphs
        except Exception as e:
            print(f"An error occurred while trying to extract paragraphs from the URL {url}: {e}")
            return None
            
    def link_from_url(url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            links = soup.find_all('a')
            return links
        except Exception as e:
            print(f"An error occurred while trying to extract links from the URL {url}: {e}")
            return None
            
    def text_from_class(url, class_name):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            elem = soup.find('div', {'class': class_name})
            if elem is not None:
                return elem.get_text().strip()
            else:
                return None
        except Exception as e:
            print(f"An error occurred while trying to extract text from the class {class_name} of the URL {url}: {e}")
            return None
            
    def text_from_id(url, id_name):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            elem = soup.find(id=id_name)
            if elem is not None:
                return elem.get_text().strip()
            else:
                return None
        except Exception as e:
            print(f"An error occurred while trying to extract text from the id {id_name} of the URL {url}: {e}")
            return None

    def heading_from_url(url, heading_tag):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            elem = soup.find(heading_tag)
            if elem is not None:
                return elem.get_text().strip()
            else:
                return None
        except Exception as e:
            print(f"An error occurred while trying to extract text from the url {url}: {e}")
            None

    def all_headings_from_url(url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            all_headings = []
            for heading_tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                heading = soup.find(heading_tag)
                if heading is not None:
                    all_headings.append((heading_tag, heading.get_text().strip()))
            return all_headings
        except Exception as e:
            print(f"An error occurred while trying to extract text from the url {url}: {e}")
            None

    def list_from_url(url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            lists = soup.find_all(['ul', 'ol'])
            return lists
        except Exception as e:
            print(f"An error occurred while trying to extract text from the url {url}: {e}")
            None
    
    def list_item_from_url(url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            list_items = soup.find_all('li')
            return list_items
        except Exception as e:
            print(f"An error occurred while trying to extract text from the url {url}: {e}")
            None

    def table_from_url(url):
        try:    
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            tables = soup.find_all('table')
            return tables
        except Exception as e:
            print(f"An error occurred while trying to extract text from the url {url}: {e}")
            None
    
    def table_row_from_url(url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            table_rows = soup.find_all('tr')
            return table_rows
        except Exception as e:
            print(f"An error occurred while trying to extract text from the url {url}: {e}")
            None

    def table_data_from_url(url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            table_cells = soup.find_all(['th', 'td'])
            return table_cells
        except Exception as e:
            print(f"An error occurred while trying to extract text from the url {url}: {e}")
            None