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

Create virtual environment

# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate