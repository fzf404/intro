## 使用

```bash
# clone 项目
git clone https://github.com/fzf404/intro.git
# 安装依赖
pip3 install -r requires.txt

# 启动后端
cd end
# 方式一
nohup python3 app.py &
# 方式二 - 持续部署 - tmux
apt install gunicorn -y
# -b :端口 文件名:变量名
gunicorn -b :8080 app:app

# 启动前端
cd web
nohup python3 -m http.server 80 &

# 查看后台程序
ps -ef | grep python
```