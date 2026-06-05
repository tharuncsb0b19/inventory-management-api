# Inventory Management System (FastAPI + React)

A full-stack **Inventory Management System** built from a DBMS project, with:

- **Backend API**: FastAPI + SQLAlchemy + SQLite  
- **Frontend UI**: React dashboard that consumes the API

The system manages suppliers, raw materials, storage locations, inventory items, and orders, and includes a supplier spending report.

---

## Repositories

- **Backend API (this repo)**  
  `https://github.com/tharuncsb0b19/inventory-management-api`

- **Frontend UI (React)**  
  `https://github.com/tharuncsb0b19/inventory-ui`

The frontend runs in the browser and communicates with this FastAPI backend over HTTP (using `fetch`).

---

## How the Frontend and Backend Work Together

- The **backend** exposes REST endpoints like `/suppliers`, `/inventory`, `/orders`, `/rawmaterials`, and `/reports/supplier-spending`.
- The **frontend** calls these endpoints using `fetch('http://127.0.0.1:8000/...')` inside React components.
- When you:
  - Open the **Suppliers** page, the UI calls `GET /suppliers` to list all suppliers.
  - Add a supplier in the UI, it sends `POST /suppliers` with JSON data.
  - Open the **Inventory** page, it calls `GET /inventory`.
  - Open **Reports**, it calls `GET /reports/supplier-spending` and visualizes the response.

So to use the full system:

1. Start the **backend server** (FastAPI)  
2. Start the **frontend dev server** (React)  
3. The React app talks to the backend at `http://127.0.0.1:8000`.

---

## Features

### Backend (API)

- CRUD operations for core entities:
  - Suppliers
  - Raw Materials
  - Storage Locations
  - Inventory Items
  - Orders
- Supplier spending report endpoint
- SQLAlchemy ORM models and relationships
- Pydantic schemas for request/response validation
- Auto-generated Swagger UI at `/docs`

### Frontend (UI)

- Dashboard with stats:
  - Total suppliers, inventory items, orders, raw materials
- Suppliers:
  - List suppliers
  - Add new supplier (modal form)
  - Delete supplier
- Inventory:
  - List inventory items with quantity and storage
  - Add new inventory item
  - Color-coded quantity status (In Stock / Low / Critical)
- Orders:
  - List orders
  - Add new order (modal form)
- Reports:
  - Visual supplier spending report using the `/reports/supplier-spending` API
- Clean sidebar layout and cards for a professional dashboard feel

---

## Tech Stack

### Backend

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

### Frontend

- React (functional components, hooks)
- Fetch API
- CSS-in-JS style object (inline `styles`)

---

## Backend Project Structure

```text
inventory-management-api/
├── main.py          # FastAPI app and routes
├── models.py        # SQLAlchemy ORM models
├── schemas.py       # Pydantic schemas (request/response)
├── database.py      # DB engine and session management
└── requirements.txt
```

---

## Database Tables

- `suppliers`
- `rawmaterials`
- `storage`
- `inventory`
- `orders`

---

## Running the Full Stack Locally

### 1. Start the Backend (FastAPI)

```bash
# Clone backend
git clone https://github.com/tharuncsb0b19/inventory-management-api.git
cd inventory-management-api

# Create and activate virtual env
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS / Linux

# Install dependencies
pip install -r requirements.txt

# Run FastAPI server
uvicorn main:app --reload
```

Backend will be available at:

- API base: `http://127.0.0.1:8000`
- Docs: `http://127.0.0.1:8000/docs`

### 2. Start the Frontend (React)

In a new terminal:

```bash
# Clone frontend
git clone https://github.com/tharuncsb0b19/inventory-ui.git
cd inventory-ui

# Install dependencies
npm install

# Start dev server
npm run dev    # or npm start, depending on your setup
```

Open the URL shown in the terminal (for example `http://localhost:5173` or `http://localhost:3000`).

Make sure the backend is running at `http://127.0.0.1:8000`, because the React app calls endpoints like:

- `GET /suppliers`
- `GET /inventory`
- `GET /orders`
- `GET /rawmaterials`
- `GET /reports/supplier-spending`

---

## API Overview

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

---

## Example Requests

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

---

## Why This Project Is Useful

This project turns a DBMS inventory design into a working **full-stack application**:

- Shows how to map SQL tables and relationships using SQLAlchemy ORM
- Shows how to expose those models via a FastAPI REST API
- Shows how a modern React frontend consumes those APIs to build a real UI

It’s a good portfolio piece demonstrating both backend and frontend skills.

---

## Future Improvements

- Add update and delete endpoints for all models
- Add shipment and shipment item models
- Add authentication and authorization
- Switch from SQLite to PostgreSQL
- Add pagination and advanced filtering
- Containerize with Docker and add deployment setup