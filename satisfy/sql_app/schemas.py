from typing import Union

from pydantic import BaseModel


class ItemBase(BaseModel):
    args: str
    func_name: str
    sys_arch: str
    px: str



class ItemGet(ItemBase):
    pass


class ItemCreate(ItemBase):
    location_x: int
    location_y: int


class Item(ItemBase):
    id: int
    location_x: int
    location_y: int

    class Config:
        orm_mode = True
