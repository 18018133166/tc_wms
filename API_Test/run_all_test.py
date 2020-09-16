#!/usr/bin/env python
# coding:utf-8
import pytest, os

if __name__ == "__main__":
    # 生成测试报告json
    pytest.main(["-s", "-q", '--alluredir', 'D:/API_Test/report/result'])
    # 将测试报告转为html格式
    split = 'allure ' + 'generate ' + 'D:/API_Test/report/result ' + '-o ' + 'D:/API_Test/report/html ' + '--clean'
    os.system('cd D:/API_Test/report')
    os.system(split)
    print(split)