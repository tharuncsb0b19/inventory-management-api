# models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Supplier(Base):
    __tablename__ = "suppliers"

    supplierid = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    phoneno = Column(String(20), nullable=False)

    # Relationships
    rawmaterials = relationship("RawMaterial", back_populates="supplier")
    orders = relationship("Order", back_populates="supplier")


class RawMaterial(Base):
    __tablename__ = "rawmaterials"

    materialid = Column(Integer, primary_key=True, index=True)
    unitprice = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)

    supplierid = Column(Integer, ForeignKey("suppliers.supplierid"), nullable=False)

    supplier = relationship("Supplier", back_populates="rawmaterials")


class Storage(Base):
    __tablename__ = "storage"

    storageid = Column(Integer, primary_key=True, index=True)
    pincode = Column(Integer, nullable=False)
    landmark = Column(String(50), nullable=False)
    cityname = Column(String(50), nullable=False)

    inventory_items = relationship("Inventory", back_populates="storage")


class Inventory(Base):
    __tablename__ = "inventory"

    inventoryid = Column(Integer, primary_key=True, index=True)
    itemname = Column(String(50), nullable=False)
    quantity = Column(Integer, nullable=False)

    storageid = Column(Integer, ForeignKey("storage.storageid"), nullable=False)

    storage = relationship("Storage", back_populates="inventory_items")


class Order(Base):
    __tablename__ = "orders"

    orderid = Column(Integer, primary_key=True, index=True)
    orderdate = Column(String(20), nullable=False)  # simple string "YYYY-MM-DD"
    totalprice = Column(Integer, nullable=False)

    suppliersid = Column(Integer, ForeignKey("suppliers.supplierid"), nullable=False)

    supplier = relationship("Supplier", back_populates="orders")