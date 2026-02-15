import uuid
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.db.base import Base


class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_name = Column(String, nullable=False)
    api_key_hash = Column(String, nullable=False)
    rate_limit = Column(Integer, default=1000)
    created_at = Column(DateTime(timezone=True), server_default=func.now())