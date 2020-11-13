# Python基础

## 设置pip下载源
```
在windows文件管理器中输入%APPDATA%,找到pip/pip.ini(没有就新建该文件夹/文件)文件，代码如下
[global]
timeout = 6000
index-url = http://pypi.douban.com/simple
trusted-host = pypi.douban.com
```

## 文件/文件夹说明
```
dataType.py：数据类型
codeNorm.py：代码规范
basis：基础
```

### 注意
> 1.python3以上版本使用pip3命令
> 2.pip不是系统命令：添加python安装文件下的Scripts路径到系统path变量中(例如：D:\Python39-32\Scripts)
> 3.搜索库对应的whl文件(https://www.lfd.uci.edu/~gohlke/pythonlibs/#scrapy)，使用pip3 install D:\开发工具\Python\whl\Scrapy-2.4.0-py3-none-any.whl安装库