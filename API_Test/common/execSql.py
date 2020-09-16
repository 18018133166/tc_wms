#!/usr/bin/env python
# _*_coding:utf-8_*_
from common.readFile import ReadFile
import pymysql
import sys



class ExecSql():
    """
    执行sql语句类
    """

    _instance=None
    def __new__(cls,*args,**kwargs):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
        return cls._instance

    def __init__(self):
        """
        初始化mysql配置
        :param platform_name:
        """
        #self.sql_conf = self._get_sql_conf(platform_name)
        self.sql_conf=None

    def _get_sql_conf(self, project):
        """
        获取mysql配置
        :param platform_name:
        :return:
        """
        try:
            return ReadFile().read_yaml('sys_config_path')[project]['mysql']
        except:
            print(f"找不到对应项目：{project}")

    def connect_db(self):
        """
        连接mysql
        :return:
        """
        host = self.sql_conf['host']
        port = self.sql_conf['port']
        user = self.sql_conf['user']
        pwd = self.sql_conf['pwd']
        test_db = self.sql_conf['test_db']
        try:
            self.conn = pymysql.connect(host=host, user=user, password=pwd, db=test_db, port=port, charset="utf8")
        except Exception as e:
            print(f"连接mysql失败：{e}")

    def get_cursor(self):
        """
        获取游标
        :return:
        """
        self.cursor=self.conn.cursor()
        return self.cursor

    def exec_sql(self,project,sql_type,sql):
        """
        执行sql语句
        :param sql_type:
        :param sql:
        :return:
        """
        self.sql_conf = self._get_sql_conf(project)
        try:
            if sql_type == 'select_one':
                self.connect_db()
                cursor = self.get_cursor()
                cursor.execute(sql)
                result = cursor.fetchone()
            elif sql_type == 'select_list':
                self.connect_db()
                cursor = self.get_cursor()
                cursor.execute(sql)
                result = cursor.fetchall()
            elif sql_type == 'update' or sql_type == 'del' or sql_type == 'insert':
                self.connect_db()
                result = self.get_cursor().execute(sql)
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
            return result
        except Exception as e:
            print(f"sql类型或sql错误：{e}")