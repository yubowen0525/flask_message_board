from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

# 确保其他扩展和实例获得正常的数值
app = Flask(__name__.split('.')[0])
app.config.from_pyfile('setting.py')
# 不知道什么意思
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
bootstrap = Bootstrap(app)
moment = Moment(app)

db = SQLAlchemy(app)

from sayhello import views,errors,commands


if __name__ == '__main__':
    app.run()
