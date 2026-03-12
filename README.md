# Project API

A simple **FastAPI** backend API to manage projects.  
Supports **GET** and **POST** operations. Each project has:

- `id` (auto-generated)  
- `title`  
- `description`  
- `image_url`  
- `date_of_creation` (auto-generated)

---

## Tech Stack

- **Backend:** FastAPI  
- **Database:** MySQL  
- **ORM:** SQLAlchemy  
- **Driver:** PyMySQL  
- **Environment Variables:** python-dotenv  

---

## Project Structure
project-api/
├── main.py # FastAPI app and endpoints
├── crud.py # CRUD functions
├── models.py # SQLAlchemy models
├── schemas.py # Pydantic schemas
├── database.py # Database connection
├── requirements.txt # Project dependencies
├── .gitignore
├── README.md
└── .env.example # Sample environment variables



---

## Setup & Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/project-api.git
cd project-api

 2️⃣ Create virtual environment

# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

 3️⃣ Install dependencies
 pip install -r requirements.txt

 4️⃣ Configure environment variables

Create a .env file based on .env.example:

DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=project_api

⚠️ Do not push your real .env to GitHub.

 5️⃣ Run MySQL server

Make sure your MySQL database is running:

CREATE DATABASE project_api;
 6️⃣ Run the FastAPI app
uvicorn main:app --reload

Open Swagger docs: http://127.0.0.1:8000/docs

Open ReDoc docs: http://127.0.0.1:8000/redoc
