import os
import requests
import re


class Test(object):
    def run(cls, web_url):
        res = requests.get(url=web_url).content.decode(encoding='utf-8')
        urls = re.findall(pattern, res)
        for url in urls[1::]:
            curr_url = web_url + url
            if curr_url[-1] == '/':
                print(curr_url)
                cls.run(curr_url)
            else:
                print(curr_url)
                dir_path = './' + '/'.join(curr_url.split('/')[2:-1:])
                filename = ''.join(curr_url.split('/')[-1::])
                os.makedirs(dir_path, exist_ok=True)
                file = requests.get(curr_url)
                open(dir_path + '/' + filename, 'wb').write(file.content)


if __name__ == '__main__':
    web_url = "https://www.somd5.com/download/dict/"
    pattern = r'<a.*?>(.*?)<\/a>'
    Test().run(web_url)
