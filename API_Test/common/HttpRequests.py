# coding=utf-8

import json
import requests
import urllib3
from common.readFile import ReadFile


class HttpRequest():
    urllib3.disable_warnings()
    def __init__(self):
        self.sys_config_wms = ReadFile().read_yaml('sys_config_path').get('wms')

    def sso_login(self):
        '''SSO登录，输出token供wms请求的hearders调用'''
        url = self.sys_config_wms.get('url_sso')
        name = self.sys_config_wms.get('account').get('name')
        pwd = self.sys_config_wms.get('account').get('pwd')
        headers = {
            'Content-Type': 'application/json;charset=UTF-8'
        }
        body = json.dumps({"mobile": name, "password": pwd})
        try:
            urllib3.disable_warnings()
            response = requests.post(url, data=body, headers=headers, verify=False)
            token = response.json().get('row').get('token')
        except BaseException as e:
            print(f'登录失败:{e}')

        url = self.sys_config_wms.get('url_wms')
        headers = {
            'Cookie': 'token=' + token + ';qaToken=' + token
        }
        try:
            urllib3.disable_warnings()
            response = requests.post(url, data=body, headers=headers, verify=False)
            deli_tc_wms_token = response.cookies.get_dict().get('deli_tc_wms_token')
            return 'deli_tc_wms_token='+deli_tc_wms_token
        except BaseException as e:
            print(f'token获取失败:{e}')

    def post(self, url, body, headers):
        try:
            response = requests.post(url, data=body, headers=headers, verify=False)
            return response
        except BaseException as e:
            print(f'post请求异常:{e}')

    def get(self, url, headers):
        try:
            response = requests.post(url, headers=headers, verify=False)
            return response.json()
        except BaseException as e:
            print(f'get请求异常:{e}')
