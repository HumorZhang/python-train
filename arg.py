import json
from xlwt import *
def parse():
    with open("station.txt", "r", encoding='utf-8') as f:
        data = json.loads(f.read())    # load的传入参数为字符串类型
        for i  in range(len(data['city'])):
            for j in range(len(data['city'][i]['list'])):
                print(data['city'][i]['list'][j]['name'])


def get_arg():
    with open("formation", "r", encoding='utf-8') as f:
        list = f.readlines()
        for i in range(0, len(list)):
            list[i] = list[i].rstrip('\n')
        for i in range(len(list)):
            for j in range(len(list)):
                if(i==j):
                    continue
                else:
                    print(list[i],list[j])
if __name__ == '__main__':
    # parse()
    get_arg()

