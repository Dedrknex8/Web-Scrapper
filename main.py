import requests
from bs4 import BeautifulSoup

def scrap():
    url = input("Enter the url to screape : ")
    #Check if url starts with http or https
    if not (url.startswith('http://') or url.startswith('https://')):
        print("Please include http or https")
        return
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text,'html.parser')
            find_title = soup.find('title')
            if find_title:
                print(find_title.text.strip())
            else:
                print('title cannot be found for this url')
        else:
            print(f'Cannt find the site')
    except requests.RequestException as e:
        print(f"Something went worng {e}")
    
if __name__ == '__main__':
    scrap()
 