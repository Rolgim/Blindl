import os

from sqlalchemy import create_engine

# URL based on docker-compose.yml
# if not, use a default local database URL
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:root_password@db:3306/my_app_db")

engine = create_engine(DATABASE_URL)