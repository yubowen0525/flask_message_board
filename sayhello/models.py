from datetime import datetime
from sayhello import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    # 存储每一条信息的发表时间,这里的是datetime.now的原因是传入对象方法，在插入对象时才执行
    # 不在使用.now 而是 .utcnow ，获取不包含时间信息的时间戳UTC(coordinated universal time)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    # 使用 flask_moment 解决不同地区时区不一致的问题，使用UTC时间存储，到达浏览器根据浏览器时区进行转化
    # flask_moment其实简化了Moment.js库的使用过程，集成了常用的时间和日期处理函数
    # 基类base.html加载Moment.js
