from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey

from sqlalchemy.orm import relationship

from database.base_class import Base

class Job(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    company_name = Column(String, nullable=False)
    company_url = Column(String)
    location = Column(String)
    job_description = Column(String, nullable=False)
    date_posted = Column(Date, nullable=False)
    is_active = Column(Boolean, nullable=False, default=False)
    # owner_id = Column(Integer, )

