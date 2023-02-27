# 使用 flask 实现的动态发布页

Date 2022-02-25

你好，我是春木

春风绿地树先知，欢迎来到春木树洞

本网站使用 flask, sqlite3, bootstrap, jQuery 搭建，比较轻量，

用户可以随意上传动态，

同时很多功能还没实现，还请见谅

# 环境需求：

- python=3.11.0
- flask=2.2.3

# 使用

首先进入根目录，并在该目录下初始化一个 sqlite3 数据库：

```sh
python init_db.py
```

然后开启带有 flask 的环境并运行服务器：

```sh
conda activate YOUR_ENVIRONMENT
sh start.sh
```

关闭服务器可以输入：

```sh
sh stop.sh
```
