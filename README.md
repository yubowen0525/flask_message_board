# Moment
统一各个时区时间，好用的库

# Forge
生成各种虚拟的数据

# Bootstrap-Flask
简化页面开发流程，很多好用的模板 css/js
```python
from flask_bootstrap import Bootstrap
from flask import Flask

app = Flask(__name__)
bootstrap = Bootstrap(app)
```
该对象提供了两种方法用来生成资源引用代码
- 加载CSS文件的bootstrap.load_css()
- 加载js文件的bootstrap.load_js()