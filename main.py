# main.py
from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from database import SessionLocal, engine, Base
import models
import schemas

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---- Supplier endpoints ----

@app.post("/suppliers", response_model=schemas.SupplierOut)
def create_supplier(
    supplier: schemas.SupplierCreate,
    db: Session = Depends(get_db),
):
    db_supplier = models.Supplier(
        name=supplier.name,
        email=supplier.email,
        phoneno=supplier.phoneno,
    )
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier


@app.get("/suppliers", response_model=List[schemas.SupplierOut])
def list_suppliers(db: Session = Depends(get_db)):
    suppliers = db.query(models.Supplier).all()
    return suppliers


@app.get("/suppliers/{supplierid}", response_model=schemas.SupplierOut)
def get_supplier(supplierid: int, db: Session = Depends(get_db)):
    supplier = (
        db.query(models.Supplier)
        .filter(models.Supplier.supplierid == supplierid)
        .first()
    )
    if supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return supplier


# ---- RawMaterial endpoints ----

@app.post("/rawmaterials", response_model=schemas.RawMaterialOut)
def create_rawmaterial(
    rm: schemas.RawMaterialCreate,
    db: Session = Depends(get_db),
):
    supplier = (
        db.query(models.Supplier)
        .filter(models.Supplier.supplierid == rm.supplierid)
        .first()
    )
    if supplier is None:
        raise HTTPException(status_code=400, detail="Supplier does not exist")

    db_rm = models.RawMaterial(
        unitprice=rm.unitprice,
        quantity=rm.quantity,
        supplierid=rm.supplierid,
    )
    db.add(db_rm)
    db.commit()
    db.refresh(db_rm)
    return db_rm


@app.get("/rawmaterials", response_model=List[schemas.RawMaterialOut])
def list_rawmaterials(db: Session = Depends(get_db)):
    rms = db.query(models.RawMaterial).all()
    return rms


# ---- Storage endpoints ----

@app.post("/storage", response_model=schemas.StorageOut)
def create_storage(
    storage: schemas.StorageCreate,
    db: Session = Depends(get_db),
):
    db_storage = models.Storage(
        pincode=storage.pincode,
        landmark=storage.landmark,
        cityname=storage.cityname,
    )
    db.add(db_storage)
    db.commit()
    db.refresh(db_storage)
    return db_storage


@app.get("/storage", response_model=List[schemas.StorageOut])
def list_storage(db: Session = Depends(get_db)):
    return db.query(models.Storage).all()


@app.get("/storage/{storageid}", response_model=schemas.StorageOut)
def get_storage(storageid: int, db: Session = Depends(get_db)):
    storage = (
        db.query(models.Storage)
        .filter(models.Storage.storageid == storageid)
        .first()
    )
    if storage is None:
        raise HTTPException(status_code=404, detail="Storage not found")
    return storage


# ---- Inventory endpoints ----

@app.post("/inventory", response_model=schemas.InventoryOut)
def create_inventory(
    inv: schemas.InventoryCreate,
    db: Session = Depends(get_db),
):
    storage = (
        db.query(models.Storage)
        .filter(models.Storage.storageid == inv.storageid)
        .first()
    )
    if storage is None:
        raise HTTPException(status_code=400, detail="Storage does not exist")

    db_inv = models.Inventory(
        itemname=inv.itemname,
        quantity=inv.quantity,
        storageid=inv.storageid,
    )
    db.add(db_inv)
    db.commit()
    db.refresh(db_inv)
    return db_inv


@app.get("/inventory", response_model=List[schemas.InventoryOut])
def list_inventory(db: Session = Depends(get_db)):
    return db.query(models.Inventory).all()


@app.get("/inventory/{inventoryid}", response_model=schemas.InventoryOut)
def get_inventory(inventoryid: int, db: Session = Depends(get_db)):
    inv = (
        db.query(models.Inventory)
        .filter(models.Inventory.inventoryid == inventoryid)
        .first()
    )
    if inv is None:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    return inv


@app.get("/inventory/by-city", response_model=List[schemas.InventoryOut])
def list_inventory_by_city(cityname: str, db: Session = Depends(get_db)):
    inv_items = (
        db.query(models.Inventory)
        .join(models.Storage)
        .filter(models.Storage.cityname == cityname)
        .all()
    )
    return inv_items


# ---- Order endpoints ----

@app.post("/orders", response_model=schemas.OrderOut)
def create_order(
    order: schemas.OrderCreate,
    db: Session = Depends(get_db),
):
    supplier = (
        db.query(models.Supplier)
        .filter(models.Supplier.supplierid == order.suppliersid)
        .first()
    )
    if supplier is None:
        raise HTTPException(status_code=400, detail="Supplier does not exist")

    db_order = models.Order(
        orderdate=order.orderdate,
        totalprice=order.totalprice,
        suppliersid=order.suppliersid,
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


@app.get("/orders", response_model=List[schemas.OrderOut])
def list_orders(db: Session = Depends(get_db)):
    return db.query(models.Order).all()


# ---- Report endpoint ----

@app.get("/reports/supplier-spending", response_model=List[schemas.SupplierSpending])
def get_supplier_spending(db: Session = Depends(get_db)):
    rows = (
        db.query(
            models.Supplier.supplierid,
            models.Supplier.name,
            func.sum(models.Order.totalprice).label("totalspent"),
        )
        .join(models.Order, models.Supplier.supplierid == models.Order.suppliersid)
        .group_by(models.Supplier.supplierid, models.Supplier.name)
        .all()
    )

    result = [
        {
            "supplierid": supplierid,
            "name": name,
            "totalspent": totalspent,
        }
        for supplierid, name, totalspent in rows
    ]
    return result