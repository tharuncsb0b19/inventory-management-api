# schemas.py
from pydantic import BaseModel


# ----- Supplier Schemas -----

class SupplierBase(BaseModel):
    name: str
    email: str
    phoneno: str


class SupplierCreate(SupplierBase):
    pass


class SupplierOut(SupplierBase):
    supplierid: int

    class Config:
        orm_mode = True


# ----- RawMaterial Schemas -----

class RawMaterialBase(BaseModel):
    unitprice: int
    quantity: int
    supplierid: int


class RawMaterialCreate(RawMaterialBase):
    pass


class RawMaterialOut(RawMaterialBase):
    materialid: int

    class Config:
        orm_mode = True


# ----- Storage Schemas -----

class StorageBase(BaseModel):
    pincode: int
    landmark: str
    cityname: str


class StorageCreate(StorageBase):
    pass


class StorageOut(StorageBase):
    storageid: int

    class Config:
        orm_mode = True


# ----- Inventory Schemas -----

class InventoryBase(BaseModel):
    itemname: str
    quantity: int
    storageid: int


class InventoryCreate(InventoryBase):
    pass


class InventoryOut(InventoryBase):
    inventoryid: int

    class Config:
        orm_mode = True


# ----- Order Schemas -----

class OrderBase(BaseModel):
    orderdate: str      # "YYYY-MM-DD"
    totalprice: int
    suppliersid: int


class OrderCreate(OrderBase):
    pass


class OrderOut(OrderBase):
    orderid: int

    class Config:
        orm_mode = True


# ----- Report Schemas -----

class SupplierSpending(BaseModel):
    supplierid: int
    name: str
    totalspent: int