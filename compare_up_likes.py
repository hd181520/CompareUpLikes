import os.path
from selenium import webdriver

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def compare_likes(urls, log=False):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=800x500')
    options.add_argument("disable-gpu")

    driver_path = os.path.join(CURRENT_DIR, './chromedriver')
    driver = webdriver.Chrome(driver_path, chrome_options=options)

    likes = []
    for url in urls:
        driver.get(url)
        driver.implicitly_wait(10)
        temp = driver.find_element_by_id('PagesLikesCountDOMID').text
        if log:
            print('[*] ', f'"{url}"', temp)
        likes.append(temp)

    return ' VS '.join(likes)


if __name__ == '__main__':
    LINKS = [
        'https://www.facebook.com/CIVAR18',
        'https://www.facebook.com/UNIverse-CONquest-316272942366152'
    ]
    print(compare_likes(LINKS, log=True))
