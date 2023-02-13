import requests
from bs4 import BeautifulSoup
import os
import random
# from helper import is_scrapable

class VideoScrapper:
    
    def video_from_url(url,folder_path=None):
        if not folder_path:
            folder_path='.'
        try:
            request=requests.get(url)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            if request.status_code==200:
                with open(f'{folder_path}/{random.randint(1,40000)}.mp4','wb') as f:
                    f.write(request.content) 
            else:
                pass
        except Exception as e:
            raise e

    def all_video_from_url(url,folder_path=None):
        if not folder_path:
            folder_path='.'
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            elements = soup.find_all("video")
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            for i, element in enumerate(elements):
                response = requests.get(element["src"])
                if response.status_code == 200:
                    try:
                        with open(f"{folder_path}/{i}-{random.randint(1,30000)}.mp4", "wb") as f:
                            f.write(response.content) 
                    except Exception as err:
                        print(err) 
                else:
                    pass
        except Exception as e:
            raise e

    def video_with_url_pattern(url,pattern,folder_path=None):
        if not folder_path:
            folder_path='.'
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            elements = soup.find_all("video")
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            for i, element in enumerate(elements):
                if pattern in element["src"]:
                    response = requests.get(element["src"])
                    if response.status_code == 200:
                        try:
                            with open(f"{folder_path}/{i}-{random.randint(1,30000)}.mp4", "wb") as f:
                                f.write(response.content) 
                        except Exception as err:
                            print(err) 
                    else:
                        pass
        except Exception as e:
            raise e

    def video_with_class(url,classname,folder_path=None):
        if not folder_path:
            folder_path='.'
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            elements = soup.find_all("video",class_=classname)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            for i, element in enumerate(elements):
                response = requests.get(element["src"])
                if response.status_code == 200:
                    try:
                        with open(f"{folder_path}/{i}-{random.randint(1,30000)}.mp4", "wb") as f:
                            f.write(response.content) 
                    except Exception as err:
                        print(err) 
                else:
                    pass
        except Exception as e:
            raise e

    def video_with_id(url,idname,folder_path=None):
        if not folder_path:
            folder_path='.'
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            elements = soup.find_all("video",id=idname)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            for i, element in enumerate(elements):
                response = requests.get(element["src"])
                if response.status_code == 200:
                    try:
                        with open(f"{folder_path}/{i}-{random.randint(1,30000)}.mp4", "wb") as f:
                            f.write(response.content) 
                    except Exception as err:
                        print(err) 
                else:
                    pass
        except Exception as e:
            raise e
            