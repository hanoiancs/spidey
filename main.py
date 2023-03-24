import requests
from bs4 import BeautifulSoup


def extract_product_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    accepted_properties = ('og:title', 'og:url')
    meta_tags = soup.find_all('meta')
    result = {}
    for tag in meta_tags:
        if 'property' in tag.attrs and tag.attrs['property'] in accepted_properties:
            result[tag.attrs['property']] = tag.attrs['content']
    
    image = soup.css.select_one('img.product-carousel__item')
    if image and 'src' in image.attrs:
        result['og:image'] = image.attrs['src']

    return result


if __name__ == '__main__':
    headers = {
        'user-agent': 'facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)',
    }
    r = requests.get('https://shopee.vn/F0-9F-92-8B-V-C3-A1y-C4-90-E1-BA-A7m-Voan-T-C6-A1-Tr-E1-BB-85-Vai-T-E1-BA-A1o-H-C3-ACnh-N-C6-A1-C4-90-C3-ADnh-C4-90-C3-A1-C-E1-BB-B1c-Sang-i.39534704.19520579491', headers=headers)
    if r.status_code == 200:
        tags = extract_product_data(r.content)
        print(tags)
    else:
        print(f'Status code: {r.status_code}')