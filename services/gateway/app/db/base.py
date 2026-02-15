from sqlalchemy.orm import declarative_base

Base = declarative_base()

from app.models import tenant # ensures model registration