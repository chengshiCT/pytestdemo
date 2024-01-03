import pymysql


def cleanData(
        host='192.168.1.216',
        user="root",
        passwd='okerp2019',
        db='gxlj_user',
        port=3306,
        sql="DELETE FROM emp_mst WHERE emp_code='U-202311-0013'"):

    conn = pymysql.connect(host=host, port=port, user=user, password=passwd, db=db)
    try:
        # 创建游标对象
        with conn.cursor() as cursor:  # 使用 with 语句确保 cursor 正确关闭
            cursor.execute(sql)
            print(f"Deleted {cursor.rowcount} rows")  # 输出被删除的行数
            conn.commit()  # 提交事务
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()  # 如果出现错误，回滚事务
    finally:
        conn.close()  # 确保在出现异常时连接也被关闭


