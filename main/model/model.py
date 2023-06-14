from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from enum import Enum
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Time
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
    Read = db.Column(db.Boolean, default=False, nullable=False)
    CreateUser = db.Column(db.String)
    CreateTime = db.Column(db.DateTime, default=datetime.now)
    UpdateUser = db.Column(db.String)
    UpdateTime = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class User(db.Model):
    __tablename__ = 'User'
    __table_args__ = (
        db.Index('user_UserId_UserNo_Account_idx', 'UserId', 'UserNo', 'Account'),
    )

    UserId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    RoleId = db.Column(db.ForeignKey('Role.RoleId'))
    UserNo = db.Column(db.String, unique=True)
    UserName = db.Column(db.String)
    Account = db.Column(db.String, nullable=False, unique=True)
    PasswordHash = db.Column(db.String, nullable=False)
    AreaId = db.Column(db.ForeignKey('Area.Id'), nullable=True)
    UnitId = db.Column(db.ForeignKey('UserUnit.Id'), nullable=True)
    Email = db.Column(db.String)
    Phone = db.Column(db.String)
    Image = db.Column(db.Text)
    CreateTime = db.Column(db.DateTime, default=datetime.now)
    UpdateTime = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # property set method only read
    @property
    def Password(self):
        raise AttributeError('password is not a readable attribute')

    @Password.setter
    def Password(self, password):
        # self.PasswordHash = generate_password_hash(password)
        self.PasswordHash = str(pc.encrypt(password))[2:-1]

    def check_password(self, password):
        # return check_password_hash(self.PasswordHash, password)
        return self.PasswordHash == str(pc.encrypt(password))[2:-1]
