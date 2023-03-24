import requests
from bs4 import BeautifulSoup

class NovelCrawler:
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }

    base_uri = 'https://api.karyakarsa.com/api'

    
    def get_chapters(self, series):
        skip = 0
        length = 10
        chapters = []
        while True:
            url = f'{self.base_uri}/v1/series/{series}/posts?top=10&skip={skip}&count=true&&order_by=post_series.position%20asc'
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                content = response.json()
                for chapter in content["data"]:
                    chapters.append({
                        "id": chapter["id"],
                        "title": chapter["title"],
                        "slug": chapter["slug"],
                        "has_access": chapter["has_access"]["status"],
                    })
                
                if len(chapters) > int(content["total"]) or skip > int(content["total"]):
                    break
                skip += length
            else:
                pass
        return chapters
    

    def get_chapter(self, slug: str):
        url = f'{self.base_uri}/post/{slug}'

        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            content = response.json()
            return content
        
        return None

