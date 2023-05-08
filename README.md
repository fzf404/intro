## 介绍

> 琴理工作室 2021 通识课项目
>
> [视频](https://www.bilibili.com/video/BV1kL4y1B7s5) & [教案](https://share.fzf404.art/通识课) & [预览](https://demo.fzf404.art/intro/web)

### 使用技术

- 前端：HTML、CSS、jQuery
- 后端：Pyhthon3.8 + Flask

### 目录管理

```bash
.
├── end
│   ├── allow.csv # 允许增加的学号、姓名列表
│   ├── app.py # 后端程序
│   └── data.csv # 全部自我介绍列表
├── web # 前端代码
│   ├── api # mock地址
│   │   ├── intro
│   │   ├── new
│   │   ├── total
│   │   └── update
│   ├── assets # 资源文件
│   │   ├── css # 样式表
│   │   │   ├── common.css # 通用
│   │   │   ├── new.css # 新增
│   │   │   └── total.css # 全部
│   │   └── js # js文件
│   │       ├── common.js # 通用
│   │       ├── error.js # 错误
│   │       ├── intro.js # 自我介绍详情
│   │       ├── new.js # 新增
│   │       ├── total.js # 全部
│   │       └── update.js # 修改
│   ├── error.html # 错误页
│   ├── favicon.ico # 图标
│   ├── index.html # 全部
│   ├── intro.html # 详情
│   ├── new.html # 新增
│   └── update.html # 更新
├── API.md # 接口文档
└── requires.txt # python依赖库
```

## 使用

1. 增加用户

   - `end/allow.csv`：允许用户列表
   - `end/data.csv`：全部用户列表

2. 部署

```bash
# clone 项目
git clone https://github.com/fzf404/intro.git
# 安装依赖
pip3 install -r requires.txt

# 启动后端
cd end
# 方式一
# 使用 gevent.pywsgi 部署
nohup python3 app.py &
# 方式二
# 使用 gunicorn 部署
apt install gunicorn -y
# -b :端口 文件名:变量名
gunicorn -b :8080 app:app

# 启动前端
cd web
nohup python3 -m http.server 80 &

# 查看后台程序
ps -ef | grep python

# 停止程序
kill <id>

```
