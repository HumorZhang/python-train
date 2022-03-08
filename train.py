# -*- coding : UTF-8 -*-
import requests
import re
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="123456", database="ticket",charset="utf8mb4")
cursor = conn.cursor()
file = 'formation.txt'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
}


def website(from_station,to_station):
    url="https://www.suanya.cn/pages/trainList?fromCn="+from_station+"&toCn="+to_station+"&fromDate=2022-03-10"
    response=requests.get(url,headers=headers)
    response.encoding = response.apparent_encoding
    if response.status_code == 200:
        parse(response.text)
    return None
def parse(html):

    pre = []
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
    if(result == pre):
        return
    for r in result:
        if(r[0]=='D' or r[0]=='G'):
            sql = 'INSERT INTO gd_info(train_number,from_city,to_city,from_time,to_time,total_time,' \
                  'secondseat_num,secondseat_price,' \
                  'firstseat_num,firstseat_price,' \
                  'business_num,business_price)' \
                  'VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'

            data= {
                'train_number':r[0]+r[1],
                'from_time':r[2],
                'to_time':r[3].strip()[0:5],
                'from_city':r[4],
                'to_city':r[5].strip(),
                'total_time':r[6].strip(),
                'secondseat_num':r[8],
                'secondseat_price':r[7],
                'firstseat_num':r[10],
                'firstseat_price':r[9],
                'business_num':r[12],
                'business_price':r[11]
            }
            try:
                cursor.execute(sql%(data['train_number'],
                                    data['from_city'],
                                    data['to_city'],
                                    data['from_time'],
                                    data['to_time'],
                                    data['total_time'],
                                    data['secondseat_num'],
                                    data['secondseat_price'],
                                    data['firstseat_num'],
                                    data['firstseat_price'],
                                    data['business_num'],
                                    data['business_price']
                                    ))
            except Exception as e:
                print("插入失败:",e)
            conn.commit()

        else:
            sql = 'INSERT INTO train_info(train_number,from_time,to_time,from_city,to_city,total_time,' \
                  'noseat_num,noseat_price,' \
                  'hardseat_num,hardseat_price,' \
                  'hardsleeper_num,hardsleeper_price,' \
                  'softsleeper_num,softsleeper_price) ' \
                  'VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'
            data= {
                'train_number':r[0]+r[1],
                'from_time':r[2],
                'to_time':r[3].strip()[0:5],
                'from_city':r[4],
                'to_city':r[5].strip(),
                'total_time':r[6].strip(),
                'hardseat_num':r[8],
                'hardseat_price':r[7],
                'hardsleeper_num':r[10],
                'hardsleeper_price':r[9],
                'softsleeper_num':r[12],
                'softsleeper_price':r[11],
                'noseat_num':r[14],
                'noseat_price':r[13]

            }

            try:
                cursor.execute(sql%(data['train_number'],
                                    data['from_time'],
                                    data['to_time'],
                                    data['from_city'],
                                    data['to_city'],
                                    data['total_time'],
                                    data['noseat_num'],
                                    data['noseat_price'],
                                    data['hardseat_num'],
                                    data['hardseat_price'],
                                    data['hardsleeper_num'],
                                    data['hardsleeper_price'],
                                    data['softsleeper_num'],
                                    data['softsleeper_price']
                                    ))
            except Exception as e:
                print("插入失败:",e)
            conn.commit()

def get_arg():
    sql = 'select * from record_info where status = "0"'
    k = 1
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            from_station = row[0]
            to_station = row[1]
            status = row[2]
            print(from_station,to_station,k)
            website(from_station,to_station)
            updatesql = 'update record_info set status = "1" where from_station="'+from_station+'" and to_station="'+to_station+'"'
            cursor.execute(updatesql)
            conn.commit()
            k+=1

    except Exception as e:
        print("select faild:",e)


if __name__ == '__main__':
    get_arg()
    cursor.close()
    conn.close()






