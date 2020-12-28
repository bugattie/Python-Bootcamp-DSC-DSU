import csv
import requests
from bs4 import BeautifulSoup


def read_from_file():
    with open('fb-page-url.csv') as file_read:
        csv_reader = csv.reader(file_read, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                ls.append(row[0])
            else:
                line_count += 1
        print(ls)


def return_raw_input(url):
    res = requests.get(url)
    return res.content.decode()


def scrap_endpoint_page(res):
    soup = BeautifulSoup(res, "html.parser")
    return soup.select_one('span[class="_52id _50f5 _50f7"]').text[1:7]


def get_likes():
    base_url = 'https://www.facebook.com/'
    for item in ls:
        base_url += item
        raw_data = return_raw_input(base_url)
        likes = scrap_endpoint_page(raw_data)
        like.append(likes)
        base_url = 'https://www.facebook.com/'


def write_to_file():
    with open('fb-page-url.csv', 'w') as file:
        csv_writer = csv.writer(file, delimiter=',')
        csv_writer.writerow(['FB_Page_Handles', 'Likes_Count'])
        for i in range(len(ls)):
            csv_writer.writerow([ls[i], like[i]])


def main():
    read_from_file()
    get_likes()
    write_to_file()


if __name__ == "__main__":
    ls = []
    like = []
    main()
