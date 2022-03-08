import pymysql

conn = pymysql.connect(host="localhost", user="root", password="123456", database="ticket",charset="utf8mb4")
cursor = conn.cursor()
def use_mysql():
    sql = 'INSERT INTO record_info(from_station,to_station,status) VALUES ("%s","%s", 0)'
    k=1
    with open("formation", "r", encoding='utf-8') as f:
        list = f.readlines()
        for i in range(0, len(list)):
            list[i] = list[i].rstrip('\n')
        for i in range(len(list)):
            for j in range(len(list)):
                if(i==j):
                    continue
                else:
                    cursor.execute(sql%(list[i],list[j]))
                    k+=1
                    print(k)


    cursor.close()
    conn.commit()
    conn.close()
    f.close()
def test_mysql():


    sql = 'INSERT INTO record_info(from_station,to_station,status) VALUES ("123","weqq", 0)'

    try:

        cursor.execute(sql)

        conn.commit()       # 事务是访问和更新数据库的一个程序执行单元
        print("插入完成")
    except:

        conn.rollback()

# 关闭数据库连接
    conn.close()

if __name__ == '__main__':
    use_mysql()
    # test_mysql()