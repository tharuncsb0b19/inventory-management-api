# Inventory Management API

A FastAPI + SQLAlchemy based Inventory Management System built from a DBMS project.  
It manages suppliers, raw materials, storage locations, inventory items, and orders with a report endpoint for supplier spending.

## Features

- Create, read, update, and delete core records.
- Supplier management.
- Raw material tracking.
- Storage and inventory management.
- Order management.
- Report endpoint for total supplier spending.
- SQLAlchemy ORM relationships between tables.
- Clean and simple REST API design.

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

## Project Structure

```text
inventory-api/
├── main.py
├── models.py
├── schemas.py
├── database.py
└── requirements.txt
```

## Database Tables

- Suppliers
- RawMaterials
- Storage
- Inventory
- Orders

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/inventory-api.git
cd inventory-api
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
uvicorn main:app --reload
```

### 5. Open API docs

Go to:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### Suppliers
- `POST /suppliers`
- `GET /suppliers`
- `GET /suppliers/{supplierid}`

### Raw Materials
- `POST /rawmaterials`
- `GET /rawmaterials`

### Storage
- `POST /storage`
- `GET /storage`
- `GET /storage/{storageid}`

### Inventory
- `POST /inventory`
- `GET /inventory`
- `GET /inventory/{inventoryid}`
- `GET /inventory/by-city?cityname=City 1`

### Orders
- `POST /orders`
- `GET /orders`

### Reports
- `GET /reports/supplier-spending`

## Example Request

### Create Supplier
```json
{
  "name": "Supplier A1",
  "email": "a1@example.com",
  "phoneno": "1000000001"
}
```

### Create Storage
```json
{
  "pincode": 110001,
  "landmark": "Landmark 1",
  "cityname": "City 1"
}
```

### Create Inventory
```json
{
  "itemname": "Item 1",
  "quantity": 53,
  "storageid": 1
}
```

## Why this project is useful

This project converts a DBMS inventory design into a working backend application. It shows how SQL tables can be modeled using SQLAlchemy ORM and exposed through FastAPI endpoints.

## Future Improvements

- Add update and delete endpoints for all models.
- Add shipment and shipment item models.
- Add authentication.
- Use PostgreSQL instead of SQLite.
- Add pagination and filtering.