from common import db_util


def test_baidu_query_case_3():
    """
    异常断言不通过的用例
    """
    print("start to call mysql")
    delSql = "delete from demo where id = 1"
    db_util.cleanData(host="127.0.0.1", passwd="1qaz@wsx", db="stp", sql=delSql)
