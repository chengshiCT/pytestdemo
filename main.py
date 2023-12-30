import pytest


if __name__ == '__main__':
    # 通过pytest运行项目目录下的所有测试用例，并结果输出到report目录下的report.html文件报告中
    pytest.main(['--html=./report/report.html'])