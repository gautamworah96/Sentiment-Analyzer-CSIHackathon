import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:gingerbread@localhost/sentiment'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'db_repository')

ACCESS_TOKEN = '329825480-65VX53oYNk9rirgk8DShOpfgYMikpy1EmWGfnQcT'
ACCESS_SECRET = 'tkvPVpptubusAEI1ZrixZNT8GYEHKw6ObtbScE2C2T4qN'
CONSUMER_KEY = 'MdiQtmezFB2hCrJXgA3lukETL'
CONSUMER_SECRET = 'CBDg9kBHp79y225zvbZ7FCJRKNmXOBZW2znGZUo0CluC7iJavf'

