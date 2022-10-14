'''
Author: fzf404
Date: 2021-10-12 21:56:02
LastEditTime: 2022-10-14 22:04:04
Description: 自我介绍后端
'''

import csv
from time import sleep

from flask import Flask, request
from flask_cors import *
from gevent import pywsgi

# 新建服务
app = Flask("intro")
# 跨域 OPTIONS 请求回应
CORS(app, supports_credentials=True)

# 数据路径
data_path = "data.csv"
allow_path = "allow.csv"

# 文件锁
csv_lock = False


'''
description: ping
'''


@app.route('/api/ping')
def ping():
    return 'pong'


'''
description: 获取全部用户
'''


@app.route('/api/total')
def total():

    # 存储数据的字典
    data = dict()
    # 获取原始数据
    data_raw = csv.reader(open(data_path, 'r', encoding='utf-8'))

    # 遍历获得全部信息
    for item in data_raw:
        id = item[0]
        name = item[1]
        data[id] = name

    return {
        "code": 200,
        "data": data,
        "msg": "Ok"
    }


'''
description: 获取用户介绍
'''


@app.route('/api/intro')
def intro():

    # 获得 GET 请求参数
    id = request.args.get('id')

    data_raw = csv.reader(open(data_path, 'r', encoding='utf-8'))

    # 遍历获得全部信息
    for item in data_raw:
        id_tmp = item[0]
        if id == id_tmp:
            return {
                "code": 200,
                "data": {
                    "name": item[1],
                    "sex": item[2],
                    "intro": item[3],
                    "about": item[4]
                },
                "msg": "Ok"
            }

    return {
        "code": 404,
        "data": {},
        "msg": "没有找到该用户,第一次使用别忘了新建用户!"
    }


'''
description: 增加用户介绍
'''


@app.route('/api/new', methods=["POST"])
def new():
    # 获得全部信息
    id = request.form.get('id')
    name = request.form.get('name')
    sex = request.form.get('sex')
    intro = request.form.get('intro')
    about = request.form.get('about')
    password = request.form.get('password')

    # 判断是否为None
    if (id and name and sex and intro and about and password) is None:
        return {
            "code": 400,
            "data": {},
            "msg": "所有字段不应为空，请输入所有字段哦!"
        }

    # 判断是否为空
    if (len(id) and len(name) and len(sex) and len(intro) and len(about) and len(password)) == 0:
        return {
            "code": 400,
            "data": {},
            "msg": "所有字段不应为空，请输入所有字段哦!"
        }

    # 验证用户是否已编辑
    data_raw = csv.reader(open(data_path, 'r', encoding='utf-8'))
    for item in data_raw:
        id_tmp = item[0]
        if id == id_tmp:
            return {
                "code": 403,
                "data": {},
                "msg": "该用户已存在，如需修改，请使用修改功能!"
            }

    # 加载 allow 列表
    allow = False
    allow_raw = csv.reader(open(allow_path, 'r', encoding='utf-8'))

    # 验证用户是否存在
    for item in allow_raw:
        id_tmp = item[0]
        name_tmp = item[1]
        if (id == id_tmp and name == name_tmp):
            allow = True
            break

    # 不允许则返回
    if not allow:
        return {
            "code": 403,
            "data": {},
            "msg": "该用户不在列表中，请联系管理员!"
        }

    # 获得锁值
    global csv_lock

    # 锁验证
    while csv_lock:
        sleep(0.1)

    csv_lock = True  # 为文件加锁
    # 打开文件并写入, 需指定换行符
    with open(data_path, 'a+', encoding='utf-8', newline='') as f:
        data_write = csv.writer(f)
        data_write.writerow([id, name, sex, intro, about, password])
    csv_lock = False  # 解锁

    return {
        "code": 200,
        "data": {
            "id": id,
            "name": name
        },
        "msg": "Ok"
    }


'''
description: 更新用户介绍
'''


@ app.route('/api/update', methods=["POST"])
def update():

    # 获得全部信息

    id = request.json['id']
    name = request.json['name']
    sex = request.json['sex']
    intro = request.json['intro']
    about = request.json['about']
    password = request.json['password']

    # 判断是否为None
    if (id and name and sex and intro and about and password) is None:
        return {
            "code": 400,
            "data": {},
            "msg": "所有字段不应为空，请输入所有字段哦!"
        }

    # 判断是否为空
    if (len(id) and len(name) and len(sex) and len(intro) and len(about) and len(password)) == 0:
        return {
            "code": 400,
            "data": {},
            "msg": "所有字段不应为空，请输入所有字段哦!"
        }

    data_raw = csv.reader(open(data_path, 'r', encoding='utf-8'))
    data = list(data_raw)

    # 遍历查找
    for index, item in enumerate(data):
        id_tmp = item[0]
        password_tmp = item[5]
        # 鉴权
        if id == id_tmp:
            if password == password_tmp:
                data[index] = [id, name, sex, intro, about, password]

                global csv_lock
                # 判断锁
                while csv_lock:
                    sleep(0.1)

                csv_lock = True

                # 覆盖原有数据
                with open(data_path, 'w', encoding='utf-8', newline='') as f:
                    data_write = csv.writer(f)
                    data_write.writerows(data)

                csv_lock = False

                # 成功返回
                return {
                    "code": 200,
                    "data": {
                        "id": id,
                        "name": name
                    },
                    "msg": "Ok"
                }
                break

            else:
                # 密码错误
                return {
                    "code": 403,
                    "data": {},
                    "msg": "密码不正确，忘记密码请联系管理员哦"
                }

    # 未修改则用户不存在
    return {
        "code": 404,
        "data": {},
        "msg": "该用户并不存在，请检查信息是否填写正确"
    }


# 开启服务
# app.run('0.0.0.0', port=8080)
# app.run('0.0.0.0', port=8080, threaded=False)
if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 8080), app)
    server.serve_forever()
