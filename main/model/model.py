from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from .utils import PrpCrypt

db = SQLAlchemy()
migrate = Migrate()
pc = PrpCrypt('imedtac-imedtac-')


class Category(db.Model):
    __tablename__ = 'Category'

    CategoryId = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    CategoryName = db.Column(db.String)
    CreateUser = db.Column(db.String)
    CreateTime = db.Column(db.DateTime, default=datetime.now)
    UpdateUser = db.Column(db.String)
    UpdateTime = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Read(db.Model):
    __tablename__ = 'Read'

    ReadId = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    URL = db.Column(db.String)
    Title = db.Column(db.String)
    Describe = db.Column(db.String)
    Star = db.Column(db.Integer)
    CategoryId = db.Column(db.Integer)
    Read = db.Column(db.Boolean, default=False, nullable=False)
    CreateUser = db.Column(db.String)
    CreateTime = db.Column(db.DateTime, default=datetime.now)
    UpdateUser = db.Column(db.String)
    UpdateTime = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Remain(db.Model):
    __tablename__ = 'Remain'

    RemainId = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    ReadNum = db.Column(db.Integer, default=1, nullable=False)
    ReadTime = db.Column(db.Integer, default=1, nullable=False)
    RemainTime = db.Column(db.Time, nullable=False)
    CreateUser = db.Column(db.String)
    CreateTime = db.Column(db.DateTime, default=datetime.now)
    UpdateUser = db.Column(db.String)
    UpdateTime = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
