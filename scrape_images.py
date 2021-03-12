from bs4 import BeautifulSoup
import requests
import uuid
import os

def scrape_images(keyword, page_range):
    if not os.path.exists('pics'):
        os.makedirs('pics')

    if not os.path.exists('pics/'+keyword):
        os.makedirs('pics/'+keyword)
        
    directory = 'pics/' + keyword + '/'

    handled_keyword = '%20'.join(keyword.split(' '))

    url_base = "https://www.roundtheclockmall.com/index.php?route=product/search&search=" + handled_keyword + "&page="
    
    for page in range(page_range[0],page_range[1]+1):
        print("Scraping page number " + str(page) + "...")

        url = url_base + str(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        product_links = [div_tag.find("div", class_="name").find('a')['href'] for div_tag in soup.find_all("div", class_="caption")]
        print("There are " + str(len(product_links)) + " products on page " + str(page) + ".")
        
        for idx, product_url in enumerate(product_links):
            print("Scraping product " + str(idx+1) + ": " + product_url)
            product_response = requests.get(product_url)
            product_soup = BeautifulSoup(product_response.text, "html.parser")
            link_list = ['https://'+div_tag.find("img")["srcset"].split(',')[1][3:-3] for div_tag in product_soup.find_all("div", class_="swiper-slide")]
            splited_link_list = [link.split('_') for link in link_list]
            img_links = ['_'.join(link) for link in splited_link_list if (len(link)==2 or link[-1]=='pic.jpg')]
            for img_link in img_links:
                try:
                    img_response = requests.get(img_link)
                    filename = str(uuid.uuid4())
                    file = open(directory + filename + '.jpg' , "wb")
                    file.write(img_response.content)
                    file.close()
                except Exception as e:
                    print(e)
                    print("Error downloading image.")

# Accepted format in txt file: 
# keyword, 1, 3

if __name__ == '__main__':
    with open("download.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        line_list = [i.strip('\n').strip(' ') for i in line.split(',')]
        print(line_list)
        keyword = line_list[0]
        page_range = (int(line_list[1]), int(line_list[2]))
        print("Keyword: " + keyword + ", page range: " + str(page_range))
        scrape_images(keyword, page_range)