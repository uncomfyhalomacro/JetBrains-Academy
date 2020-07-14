import requests  # already imported in project but just to be sure
from bs4 import BeautifulSoup  # already imported but just to be sure
import os
from colorama import Fore, init



class PseudoBrowser:

    def __init__(self):
        self.history = []
        while True:
            self.create = f"C:/Users/User/Desktop/DODONG/Text-Based Browser/Text-Based Browser/task/tb_tabs"
            self.url = input()
            if self.url == 'exit':
                break
            elif '.' in self.url:
                self.url_name = self.url.rstrip(self.url[self.url.rindex('.'):])

                if self.url_name not in self.history:
                    self.history.append(self.url_name)
                    self.add_http()
                    self.connect_req(self.url)

                else:
                    with open(rf"{self.create}\{self.url_name}.html", "r") as read_page:
                        for lines in read_page:
                            print(lines)

            elif self.url in self.history:
                with open(rf"{self.create}\{self.url}.html", "r", encoding='utf-8') as read_page:
                    for lines in read_page:
                        print(lines)
            elif self.url == 'back':
                try:
                    self.history.pop()
                    with open(rf"{self.create}\{self.history[-1]}.html", "r", encoding='utf-8') as read_page:
                        for lines in read_page:
                            print(lines)
                except IndexError:
                    print("ERROR: No more URLs in history")

            else:
                print('Error: Incorrect URL')



    # check if input url has 'https://' else append 'https://'
    def add_http(self):
        if self.url.count('https://') == 0:
            self.url = 'https://' + self.url

    def connect_req(self, url_):
        self.r = requests.get(url_)
        soup = BeautifulSoup(self.r.content, 'html.parser')

        if self.r:
            with open(rf"{self.create}\{self.url_name}.html", "w+", encoding='utf-8') as page:
                for tags in soup.find_all(('a','p')):
                    if tags.name == 'a':
                        print(Fore.BLUE + tags.text.replace('\n', ' ').strip(), file=page, flush=True)
                    else:
                        print(tags.text.replace('\n',' ').strip(), file=page, flush=True)

            with open(rf"{self.create}\{self.url_name}.html", "r", encoding='utf-8') as read_page:
                for lines in read_page:
                    print(lines)

        else:
            print('Fail')


def main(dir_name):
    try:
        os.makedirs(dir_name)

    except FileExistsError:
        pass

    PseudoBrowser()

if __name__ == "__main__":
    main(f"C:/Users/User/Desktop/DODONG/Text-Based Browser/Text-Based Browser/task/tb_tabs")


