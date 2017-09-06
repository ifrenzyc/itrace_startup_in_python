# itrace_startup_in_python
2017 itrace startup in python

## 安装 pip
Python的第三方包依赖需要通过 pip 安装：
因此，我们在部署环境上需要先安装好pip，并安装第三方类库。Python2.x版本是没有自带pip 的：
``` shell
$ wget https://bootstrap.pypa.io/get-pip.py
$ su - root  # 切换到 root 用户
# python get-pip.py
```

## 选拔赛题目二：
**运行：**
``` shell
$ pip install Flask
$ python section02.py
```

## ORM 集成
集成了 SQLAlchemy 包，是 Python 语言的一个 ORM 包，支持多种数据库。

### 安装

``` shell
$ pip install SQLAlchemy flask-sqlalchemy pymysql
$ python section02.py
```

例子接口：
[http://127.0.0.1:5000/cust/get](http://127.0.0.1:5000/cust/get)

### 参考材料
- [Flask 开发之Model：Flask-SQLAlchemy](https://litaotju.github.io/flask/2016/06/21/Learning-Flask-ORM-SQLAlchemy/)
