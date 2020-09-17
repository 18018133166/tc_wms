# coding=utf-8

import allure
import pytest

from common.execSql import ExecSql
from cases.goods_management import *


# class Test_goods_management():
#
#     def response(self, response):
#         allure.attach(str(response[1]), 'headers')
#         allure.attach(response[2], 'url')
#         allure.attach(response[3], 'body')
#         allure.attach(str(response[0]), 'response')
#
#
#     @allure.feature('1.商品管理')
#     @allure.story('1.1.添加商品')
#     @allure.severity('critical')
#     def test_01_add_goods(self):
#         '''
#         首次新增商品,商品名称根据当前时间命名（后缀格式年月日时分秒）,goods_name定义为全局变量
#         '''
#         response = add_goods()
#         code = response[0].get('code')
#         global goods_name
#         goods_name = response[4]
#         with allure.step("步骤1，新增商品是否成功：code == 0"):
#             allure.attach(goods_name, '商品名称')
#             self.response(response)
#             assert code == 0
#         sql = f'SELECT * FROM sm_goods WHERE goods_name = \'{goods_name}\''
#         result = ExecSql().exec_sql('wms', 'select_one', sql)
#         with allure.step('步骤2，数据库是否落地成功：sql执行结果 != None'):
#             allure.attach(sql, 'sql语句')
#             allure.attach(str(result), '执行结果')
#             assert result != None
#
#
#     @allure.feature('1.商品管理')
#     @allure.story('1.1.添加商品')
#     @allure.severity('normal')
#     def test_02_add_goods_repeat(self):
#         '''
#         新增重复商品（根据商品名称判断，传入test_01_add_定义的全局变量goods_name）
#         '''
#         response = add_goods_repeat(goods_name)
#         code = response[0].get('code')
#         with allure.step("步骤1，新增重复商品是否失败：code == 2"):
#             allure.attach(goods_name, '商品名称')
#             self.response(response)
#             assert code == 2
#         sql = f'SELECT count(1) FROM sm_goods WHERE goods_name = \'{goods_name}\''
#         result = ExecSql().exec_sql('wms', 'select_list', sql)
#         count = result[0][0]
#         with allure.step('步骤2，数据库是否未插入数据：count == 1'):
#             allure.attach(sql, 'sql语句')
#             allure.attach(str(result), '执行结果')
#             assert count == 1
#
#
#     @allure.feature('1.商品管理')
#     @allure.story('1.2.商品审核')
#     @allure.severity('critical')
#     def test_03_goods_check(self):
#         '''
#         商品审核通过
#         '''
#         sql_1 = f'SELECT check_status FROM sm_goods WHERE goods_name = \'{goods_name}\''
#         sql_2 = f'SELECT id FROM sm_goods WHERE goods_name = \'{goods_name}\''
#         check_status_before = ExecSql().exec_sql('wms', 'select_one', sql_1)
#         check_status_before = check_status_before[0]
#         with allure.step(f'步骤1，检查商品的当前状态是否为待审核：check_status == 1'):
#             allure.attach(sql_1, 'sql语句')
#             allure.attach(str(check_status_before), '执行结果')
#             assert check_status_before == 1
#         goods_id = ExecSql().exec_sql('wms', 'select_one', sql_2)[0]
#         response = goods_check(goods_id)
#         code = response[0].get('code')
#         with allure.step(f'步骤2，审核通过操作：code == 0'):
#             allure.attach(str(goods_id), '商品ID')
#             self.response(response)
#             assert code == 0
#         check_status_after = ExecSql().exec_sql('wms', 'select_one', sql_1)
#         check_status_after = check_status_after[0]
#         with allure.step(f'步骤3，检查商品的当前状态是否审核通过：check_status == 2'):
#             allure.attach(sql_1, 'sql语句')
#             allure.attach(str(check_status_after), '执行结果')
#             assert check_status_after == 2
