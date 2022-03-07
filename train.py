# -*- coding : UTF-8 -*-
import requests
import re
file = 'formation.txt'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
}
def arg_to_url():
    None

def website(url):
    response=requests.get(url,headers=headers)
    response.encoding = response.apparent_encoding
    if response.status_code == 200:
        return response.text
    return None
def parse(html):
    pattern=re.compile('<div class="railway_list" data-v-9079722a><div class="w1" data-v-9079722a><div data-v-9079722a><strong data-v-9079722a>(.*?)(\d+)</strong>'
                       '.*?<div class="w2" data-v-9079722a><div data-v-9079722a><strong data-v-9079722a>(.*?)</strong>'
                       '.*?<label data-v-9079722a>(.*?)</label>'
                       '.*?<span data-v-9079722a>(.*?)</span></div>'
                       '.*?<span data-v-9079722a>(.*?)</span></div>'
                       '.*?<div data-v-9079722a>(.*?)</div></div>'
                     
                       '.*?<b data-v-9079722a>(.*?)</b>.*?<em data-v-9079722a>(.*?)</em>'
                       '.*?<b data-v-9079722a>(.*?)</b>.*?<em data-v-9079722a>(.*?)</em>'
                       '.*?<b data-v-9079722a>(.*?)</b>.*?<em data-v-9079722a>(.*?)</em>'
                       '.*?<b data-v-9079722a>(.*?)</b>.*?<em data-v-9079722a>(.*?)</em>'
                       '',re.S)
    result = re.findall(pattern, html)
    for r in result:
        if(r[0]=='D' or r[0]=='G'):
            test={
                'trainno':r[0],
                'number':r[0]+r[1],
                'from_time':r[2],
                'to_time':r[3].strip()[0:5],
                'from_station':r[4],
                'to_station':r[5],
                'all_time':r[6].strip(),
                'secondseat_price':r[7],
                'secondseat_num':r[8],
                'firstseat_price':r[9],
                'firstseat_num':r[10],
                'noseat_price':r[11],
                'noseat_num':r[12],

            }
            print(test)
        else:
            test={
                'trainno':r[0],
                'number':r[0]+r[1],
                'from_time':r[2],
                'to_time':r[3].strip()[0:5],
                'from_station':r[4],
                'to_station':r[5],
                'all_time':r[6].strip(),
                'hardseat_price':r[7],
                'hardseat_num':r[8],
                'hardsleeper_price':r[9],
                'hardsleeper_num':r[10],
                'softsleeper_price':r[11],
                'softsleeper_num':r[12],
                'noseat_price':r[13],
                'noseat_num':r[14],
            }
            print(test)


def write_to_txt(html):
    with open(file,'a',encoding='utf-8') as f:
        f.write(html)
        print("write success!")




if __name__ == '__main__':
    # from_statio="呼和浩特"
    # to_station="石家庄"

    # from_statio="武汉"
    # to_station="厦门"

    from_statio="呼和浩特"
    to_station="拉萨"

    url_one="https://www.suanya.cn/pages/trainList?fromCn="+from_statio+"&toCn="+to_station+"&fromDate=2022-03-08"
    html=website(url_one)

    k=parse(html)
    print(k)



