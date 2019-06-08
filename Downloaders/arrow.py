import sys

try:
    # Python 3.x
    from urllib.request import urlopen, urlretrieve, quote
    from urllib.parse import urljoin
except ImportError:
    # Python 2.x
    from urllib import urlopen, urlretrieve, quote
    from urlparse import urljoin

from bs4 import BeautifulSoup
import requests


def progress(count, total, status):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()


def get_ep_no(lis):
    global prev
    global episode
    fname = ""
    fname1 = ""
    if (episode < 10):
        fname = "S06E0" + str(episode)
        fname1 = "s06e0" + str(episode)
    else:
        fname = "S06E" + str(episode)
        fname1 = "s06e" + str(episode)
    for link in lis:
        s_list = link.text.split(".")
        if fname in s_list or fname1 in s_list:
            prev = episode
            episode += 1
            get_ep_no(lis)
            break


def get_file_name(episode, lis):
    if (episode < 10):
        fname = "S06E0" + str(episode)
        fname1 = "s06e0" + str(episode)
    else:
        fname = "S06E" + str(episode)
        fname1 = "s06e" + str(episode)
    flag = -1
    file_name = ""
    for link in lis:
        s_list = link.text.split(".")
        if fname in s_list or fname1 in s_list:
            if "720p" in s_list:
                file_name = link.get('href')
                flag = 0
                break
    if flag == -1:
        for link in lis:
            s_list = link.text.split(".")
            if fname in s_list or fname1 in s_list:
                if "480p" in s_list:
                    file_name = link.get('href')
                    flag = 0
                    break
    if flag == -1:
        print("File not found")
    else:
        return file_name


def download(file_name, url):
    href = urljoin(url, quote(file_name))
    try:
        # create response object
        r = requests.get(href, stream=True)
        total = r.headers['Content-length']
        total = int(total)
        x = total / (1024 * 1024)
        print("Size = %d MB" % x)
        print(
            "Enter path of folder(in format /x/y/z/) where you want to place the file (Leave empty to download in current directory)")
        file_path = ""
        file_path = input()
        file_path = file_path + file_name
        # download started
        size = 0
        status = "Downloading file:" + (file_name)
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    size += 1024 * 1024
                    f.write(chunk)
                    progress(size, total, status)

        print("%s downloaded!\n" % (file_name))
    except:
        print('failed to download')


prev = 0
episode = 1
url = "http://dl.dlfile.pro/6/Series/Arrow/"
u = urlopen(url)
try:
    html = u.read().decode('utf-8')
finally:
    u.close()
soup = BeautifulSoup(html, "lxml")
lis = soup.find_all('a')
get_ep_no(lis)
# print(prev)
file_name = get_file_name(prev, lis)
print(file_name)
download(file_name, url)

