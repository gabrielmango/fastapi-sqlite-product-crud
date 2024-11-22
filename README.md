# fastapi-sqlite-product-crud

**Description:** A backend application for managing products using FastAPI and SQLite with full CRUD support.

---

## Features

- Create, Read, Update, and Delete (CRUD) operations for products.
- SQLite database for lightweight and efficient storage.
- Environment variable support using `.env`.
- Auto-generated API documentation via Swagger UI.

---

## Installation

### 1. Prerequisites

- Python 3.8 or higher
- Virtual environment tool (optional but recommended)

### 2. Clone the repository

```bash
git clone https://github.com/gabrielmango/fastapi-sqlite-product-crud.git
cd ProductCRUD-FastAPI
```

### 3. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Project Structure

```plaintext
ProductCRUD-FastAPI/
│
├── app/
│   ├── __init__.py         # Package initializer
│   ├── main.py             # Main application file
│   ├── database.py         # Database connection and session
│   ├── models.py           # SQLAlchemy models
│   ├── schemas.py          # Pydantic schemas
│   ├── crud.py             # CRUD operations
│   └── config.py           # Environment configuration
│
├── .env                    # Environment variables
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
```

---

## How to Run

1. Activate the virtual environment:
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Start the FastAPI server:
   ```bash
   fastapi dev app/main.py
   ```

3. Open your browser and go to:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## API Endpoints

### Base URL: `http://127.0.0.1:8000`

| Method | Endpoint            | Description                  |
|--------|---------------------|------------------------------|
| POST   | `/products/`        | Create a new product         |
| GET    | `/products/`        | Get a list of all products   |
| GET    | `/products/{id}`    | Get a specific product by ID |
| PUT    | `/products/{id}`    | Update a product by ID       |
| DELETE | `/products/{id}`    | Delete a product by ID       |

---

## Example Product JSON

### Create or Update Request:
```json
{
  "name": "Example Product",
  "description": "A sample description",
  "unit_price": 19.99
}
```

### Response:
```json
{
  "id": 1,
  "name": "Example Product",
  "description": "A sample description",
  "unit_price": 19.99
}
```

---

## Environment Variables

Create a `.env` file in the root of the project with the following content:

```plaintext
DATABASE_URL=sqlite:///./products.db
```

---

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/) - For building the backend.
- [SQLite](https://www.sqlite.org/) - Lightweight database.
- [SQLAlchemy](https://www.sqlalchemy.org/) - ORM for database interaction.
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation and parsing.

---

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add a feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## License

This project is licensed under the GPL-3.0 license. See the [LICENSE](LICENSE) file for details.

---

## Author

[Gabriel Mango](https://github.com/gabrielmango)
