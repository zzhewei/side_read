from datetime import timedelta
import os


class BaseConfig:  # 基本配置
    ACCESS_EXPIRES = timedelta(hours=1)
    SECRET_KEY = os.urandom(24)
    # 不設定的話Flask會使用緩存的js跟css不會更新
    SEND_FILE_MAX_AGE_DEFAULT = timedelta(seconds=1)
    # 中文設置
    JSON_AS_ASCII = False


class DevelopmentConfig(BaseConfig):
    JWT_SECRET_KEY = "SideProject_read"
    JWT_ACCESS_TOKEN_EXPIRES = BaseConfig.ACCESS_EXPIRES
    JWT_REFRESH_TOKEN_EXPIRES = BaseConfig.ACCESS_EXPIRES * 24 * 30
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "postgresql://manga_1h1z_user:6xR37NTVTVsXQ9nJrB551sEVhtpKKZ0c@dpg-ch5lg0orddl7albugqeg-a.singapore-postgres.render.com/sideread"
    # if use docker compose use this
    # SQLALCHEMY_DATABASE_URI = "postgresql://postgres:root@read_postgresql:5432/sideread"


class TestingConfig(BaseConfig):
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}
