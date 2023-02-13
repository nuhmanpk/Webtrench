import requests
from bs4 import BeautifulSoup
import re
# from helper import is_scrapable

class MetaDataScrapper:
    def get_website_title(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            title = soup.title.string
            return title
        except Exception as e:
            raise e

    def get_website_description(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            description = soup.find("meta",  property="og:description")
            return description["content"]
        except Exception as e:
            raise e

    def get_website_keywords(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            keywords = soup.find("meta",  property="og:keywords")
            return keywords["content"]
        except Exception as e:
            raise e

    def get_website_image(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            image = soup.find("meta",  property="og:image")
            return image["content"]
        except Exception as e:
            raise e

    def get_website_url(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            url = soup.find("meta",  property="og:url")
            return url["content"]
        except Exception as e:
            raise e
    
    def get_website_type(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            type = soup.find("meta",  property="og:type")
            return type["content"]
        except Exception as e:
            raise e
    
    def get_website_site_name(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            site_name = soup.find("meta",  property="og:site_name")
            return site_name["content"]
        except Exception as e:
            raise e
    
    def get_website_locale(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            locale = soup.find("meta",  property="og:locale")
            return locale["content"]
        except Exception as e:
            raise e

    def meta_data(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            meta_data = soup.find_all("meta")
            return meta_data
        except Exception as e:
            raise e

    def with_property(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            meta_data = soup.find_all("meta",  property=True)
            return meta_data
        except Exception as e:
            raise e
    
    def with_name(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            meta_data = soup.find_all("meta",  name=True)
            return meta_data
        except Exception as e:
            raise e
        
    def with_http_equiv(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            meta_data = soup.find_all("meta",  http_equiv=True)
            return meta_data
        except Exception as e:
            raise e

    def with_content(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            meta_data = soup.find_all("meta",  content=True)
            return meta_data
        except Exception as e:
            raise e
    
    def with_charset(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            meta_data = soup.find_all("meta",  charset=True)
            return meta_data
        except Exception as e:
            raise e

    def with_itemprop(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            meta_data = soup.find_all("meta",  itemprop=True)
            return meta_data
        except Exception as e:
            raise e

    def with_scheme(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            meta_data = soup.find_all("meta",  scheme=True)
            return meta_data
        except Exception as e:
            raise e

    def with_lang(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            meta_data = soup.find_all("meta",  lang=True)
            return meta_data
        except Exception as e:
            raise e

    def with_dir(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            meta_data = soup.find_all("meta",  dir=True)
            return meta_data
        except Exception as e:
            raise e

    def with_xml_lang(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            meta_data = soup.find_all("meta",  xml_lang=True)
            return meta_data
        except Exception as e:
            raise e

    def with_xmlns(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            meta_data = soup.find_all("meta",  xmlns=True)
            return meta_data
        except Exception as e:
            raise e

    def with_xmlns_xsi(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            meta_data = soup.find_all("meta",  xmlns_xsi=True)
            return meta_data
        except Exception as e:
            raise e

    def with_xsi_schemaLocation(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            meta_data = soup.find_all("meta",  xsi_schemaLocation=True)
            return meta_data
        except Exception as e:
            raise e

    def with_xmlns_og(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            meta_data = soup.find_all("meta",  xmlns_og=True)
            return meta_data
        except Exception as e:
            raise e

    def with_xmlns_fb(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            meta_data = soup.find_all("meta",  xmlns_fb=True)
            return meta_data
        except Exception as e:
            raise e

    def with_xmlns_article(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            meta_data = soup.find_all("meta",  xmlns_article=True)
            return meta_data
        except Exception as e:
            raise e

    def with_xmlns_profile(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            meta_data = soup.find_all("meta",  xmlns_profile=True)
            return meta_data
        except Exception as e:
            raise e

    def with_xmlns_book(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            meta_data = soup.find_all("meta",  xmlns_book=True)
            return meta_data
        except Exception as e:
            raise e

    def with_xmlns_video(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            meta_data = soup.find_all("meta",  xmlns_video=True)
            return meta_data
        except Exception as e:
            raise e

    def with_xmlns_music(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            meta_data = soup.find_all("meta",  xmlns_music=True)
            return meta_data
        except Exception as e:
            raise e


    def with_xmlns_place(url):
        try:
            request=requests.get(url)
            html_content = request.content
            soup = BeautifulSoup(html_content, "html.parser")
            meta_data = soup.find_all("meta",  xmlns_place=True)
            return meta_data
        except Exception as e:
            raise e

    def get_keyword_density(url, keyword):
        response = requests.get(url)
        content = response.content.decode("utf-8").lower()
        word_count = len(re.findall(keyword, content))
        total_words = len(re.findall("\w+", content))
        density = (word_count / total_words) * 100
        return density

    def get_meta_data(url):
        response = requests.get(url)
        content = response.content.decode("utf-8")
        meta_data = {}
        meta_tags = re.findall("<meta.*?>", content)
        for meta_tag in meta_tags:
            name = re.search("name=['\"](.*?)['\"]", meta_tag)
            if name:
                name = name.group(1)
            else:
                name = re.search("property=['\"](.*?)['\"]", meta_tag)
                if name:
                    name = name.group(1)
                else:
                    continue
            value = re.search("content=['\"](.*?)['\"]", meta_tag)
            if value:
                value = value.group(1)
                meta_data[name] = value
        return meta_data