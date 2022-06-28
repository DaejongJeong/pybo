import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db')) # 데이터 베이스에 접근할 수 있는 경로 집어넣기
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "dev"