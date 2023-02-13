import requests
from bs4 import BeautifulSoup
# from helper import is_scrapable
import os
import random

class ImageScrapper:

    def image_from_url(url,folder_path=None):
        if not folder_path:
            folder_path='.'
        try:
            request=requests.get(url)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            if request.status_code==200:
                with open(f'{folder_path}/{random.randint(1,40000)}.jpg','wb') as f:
                    f.write(request.content) 
            else:
                pass
        except Exception as e:
            raise e

    def all_image_from_url(url,folder_path=None):
        if not folder_path:
            folder_path='.'
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            elements = soup.find_all("img")
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            for i, element in enumerate(elements):
                response = requests.get(element["src"])
                if response.status_code == 200:
                    try:
                        with open(f"{folder_path}/{i}-{random.randint(1,30000)}.png", "wb") as f:
                            f.write(response.content) 
                    except Exception as err:
                        print(err) 
                else:
                    pass
        except Exception as e:
            raise e
    
    def image_with_url_pattern(url,pattern,folder_path=None):
        if not folder_path:
            folder_path='.'
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            elements = soup.find_all("img")
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            for i, element in enumerate(elements):
                if pattern in element["src"]:
                    response = requests.get(element["src"])
                    if response.status_code == 200:
                        with open(f"{folder_path}/{i}-{random.randint(1,30000)}.png", "wb") as f:
                            f.write(response.content)
                    else:
                        pass
        except Exception as e:
            raise e

    def image_with_class(url,class_name,folder_path=None):
        if not folder_path:
            folder_path='.'
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            elements = soup.find_all("img",class_=class_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            for i, element in enumerate(elements):
                response = requests.get(element["src"])
                if response.status_code == 200:
                    with open(f"{folder_path}/{i}-{random.randint(1,30000)}.png", "wb") as f:
                        f.write(response.content)
                else:
                    pass
        except Exception as e:
            raise e

    def image_with_id(url,id_name,folder_path=None):
        if not folder_path:
            folder_path='.'
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            elements = soup.find_all("img",id=id_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            for i, element in enumerate(elements):
                response = requests.get(element["src"])
                if response.status_code == 200:
                    with open(f"{folder_path}/{i}-{random.randint(1,30000)}.png", "wb") as f:
                        f.write(response.content)
                else:
                    pass
        except Exception as e:
            raise e

    def image_with_alt(url,alt_name,folder_path=None):
        if not folder_path:
            folder_path='.'
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            elements = soup.find_all("img",alt=alt_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            for i, element in enumerate(elements):
                response = requests.get(element["src"])
                if response.status_code == 200:
                    with open(f"{folder_path}/{i}-{random.randint(1,30000)}.png", "wb") as f:
                        f.write(response.content)
                else:
                    pass
        except Exception as e:
            raise e

    def image_with_title(url,title_name,folder_path=None):
        if not folder_path:
            folder_path='.'
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            elements = soup.find_all("img",title=title_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            for i, element in enumerate(elements):
                response = requests.get(element["src"])
                if response.status_code == 200:
                    with open(f"{folder_path}/{i}-{random.randint(1,30000)}.png", "wb") as f:
                        f.write(response.content)
                else:
                    pass
        except Exception as e:
            raise e
    
    def image_with_height(url,height,folder_path=None):
        if not folder_path:
            folder_path='.'
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            elements = soup.find_all("img",height=height)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            for i, element in enumerate(elements):
                response = requests.get(element["src"])
                if response.status_code == 200:
                    with open(f"{folder_path}/{i}-{random.randint(1,30000)}.png", "wb") as f:
                        f.write(response.content)
                else:
                    pass
        except Exception as e:
            raise e

    def image_with_width(url,width,folder_path=None):
        if not folder_path:
            folder_path='.'
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            elements = soup.find_all("img",width=width)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            for i, element in enumerate(elements):
                response = requests.get(element["src"])
                if response.status_code == 200:
                    with open(f"{folder_path}/{i}-{random.randint(1,30000)}.png", "wb") as f:
                        f.write(response.content)
                else:
                    pass
        except Exception as e:
            raise e
    
    def image_with_style(url,style,folder_path=None):
        if not folder_path:
            folder_path='.'
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            elements = soup.find_all("img",style=style)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            for i, element in enumerate(elements):
                response = requests.get(element["src"])
                if response.status_code == 200:
                    with open(f"{folder_path}/{i}-{random.randint(1,30000)}.png", "wb") as f:
                        f.write(response.content)
                else:
                    pass
        except Exception as e:
            raise e
        