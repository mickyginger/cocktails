import os

secret = os.getenv('SECRET', 'shh')
db_uri = os.getenv('DATABASE_URL', 'postgres://localhost:5432/cocktails')
