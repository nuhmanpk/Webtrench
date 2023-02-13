import requests
from bs4 import BeautifulSoup
import os
import random
# from helper import is_scrapable

class AudioScrapper:
    
    def audio_from_url(url,folder_path=None):
        if not folder_path:
            folder_path='.'
        try:
            request=requests.get(url)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            if request.status_code==200:
                with open(f'{folder_path}/{random.randint(1,40000)}.mp3','wb') as f:
                    f.write(request.content) 
            else:
                pass
        except Exception as e:
            raise e

    def all_audio_from_url(url,folder_path=None):
        if not folder_path:
            folder_path='.'
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            elements = soup.find_all("audio")
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            for i, element in enumerate(elements):
                response = requests.get(element["src"])
                if response.status_code == 200:
                    try:
                        with open(f"{folder_path}/{i}-{random.randint(1,30000)}.mp3", "wb") as f:
                            f.write(response.content) 
                    except Exception as err:
                        print(err) 
                else:
                    pass
        except Exception as e:
            raise e

    def audio_with_url_pattern(url,pattern,folder_path=None):
        if not folder_path:
            folder_path='.'
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            elements = soup.find_all("audio")
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            for i, element in enumerate(elements):
                if pattern in element["src"]:
                    response = requests.get(element["src"])
                    if response.status_code == 200:
                        try:
                            with open(f"{folder_path}/{i}-{random.randint(1,30000)}.mp3", "wb") as f:
                                f.write(response.content) 
                        except Exception as err:
                            print(err) 
                    else:
                        pass
        except Exception as e:
            raise e
        
    def audio_with_class(url,cls,folder_path=None):
        if not folder_path:
            folder_path='.'
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            elements = soup.find_all("audio",{"class":cls})
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            for i, element in enumerate(elements):
                response = requests.get(element["src"])
                if response.status_code == 200:
                    try:
                        with open(f"{folder_path}/{i}-{random.randint(1,30000)}.mp3", "wb") as f:
                            f.write(response.content) 
                    except Exception as err:
                        print(err) 
                else:
                    pass
        except Exception as e:
            raise e

    def audio_with_id(url,cls,folder_path=None):
        if not folder_path:
            folder_path='.'
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            elements = soup.find_all("audio",{"id":cls})
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            for i, element in enumerate(elements):
                response = requests.get(element["src"])
                if response.status_code == 200:
                    try:
                        with open(f"{folder_path}/{i}-{random.randint(1,30000)}.mp3", "wb") as f:
                            f.write(response.content) 
                    except Exception as err:
                        print(err) 
                else:
                    pass
        except Exception as e:
            raise e

    def audio_with_attribute(url,attr,folder_path=None):
        if not folder_path:
            folder_path='.'
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            elements = soup.find_all("audio",attrs=attr)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            for i, element in enumerate(elements):
                response = requests.get(element["src"])
                if response.status_code == 200:
                    try:
                        with open(f"{folder_path}/{i}-{random.randint(1,30000)}.mp3", "wb") as f:
                            f.write(response.content) 
                    except Exception as err:
                        print(err) 
                else:
                    pass
        except Exception as e:
            raise e

    def audio_with_attribute_value(url,attr,value,folder_path=None):
        if not folder_path:
            folder_path='.'
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            elements = soup.find_all("audio",attrs={attr:value})
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            for i, element in enumerate(elements):
                response = requests.get(element["src"])
                if response.status_code == 200:
                    try:
                        with open(f"{folder_path}/{i}-{random.randint(1,30000)}.mp3", "wb") as f:
                            f.write(response.content) 
                    except Exception as err:
                        print(err) 
                else:
                    pass
        except Exception as e:
            raise e

    def audio_with_attribute_value_pattern(url,attr,value,folder_path=None):
        if not folder_path:
            folder_path='.'
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            elements = soup.find_all("audio",attrs={attr:value})
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            for i, element in enumerate(elements):
                if value in element[attr]:
                    response = requests.get(element["src"])
                    if response.status_code == 200:
                        try:
                            with open(f"{folder_path}/{i}-{random.randint(1,30000)}.mp3", "wb") as f:
                                f.write(response.content) 
                        except Exception as err:
                            print(err) 
                    else:
                        pass
        except Exception as e:
            raise e

    