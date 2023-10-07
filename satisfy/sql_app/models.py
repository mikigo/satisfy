from sqlalchemy import Column, Integer, String
from .database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    args = Column(String)
    func_name = Column(String)
    sys_arch = Column(String)
    px = Column(String)
    location_x = Column(Integer)
    location_y = Column(Integer)