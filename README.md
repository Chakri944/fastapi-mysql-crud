***Created FastAPI simple Data model CRUD operations***

## 🚀 Features
* **FastAPI Framework:** High-performance, easy-to-learn web framework.
* **MySQL Integration:** Relational database storage for data persistence.
* **Automatic Documentation:** Interactive API docs via Swagger UI.

## 🛠️ Prerequisites
Before running this project, ensure you have the following installed:
* Python 3.8+
* MySQL Server

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com
cd YOUR_REPOSITORY_NAME
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
# Activate on Windows:
venv\Scripts\activate
# Activate on macOS/Linux:
source venv/bin/bin/activate
```

### 3. Install Dependencies
```bash
pip install fastapi uvicorn sqlalchemy pymysql
```
*(Note: Change `pymysql` to your specific MySQL driver if different)*

### 4. Environment Variables
Create a `.env` file in the root directory and add your database credentials:
```env
DATABASE_URL=mysql+pymysql://YOUR_USER:YOUR_PASSWORD@localhost:3306/YOUR_DB_NAME
```

### 5. Run the Application
```bash
uvicorn main:app --reload
```

## 📖 API Documentation
Once the server is running, you can view the interactive API documentation at:
* **Swagger UI:** http://127.0.0
* **ReDoc:** http://127.0.0


## 📂 Project Structure
```text
├── main.py                   # FastAPI application entry point
├── database.py               # MySQL database connection setup
├── database_models.py        # SQLAlchemy data models
├── models.py                 # SQLAlchemy data models
├── .env                      # Local environment variables (Secret!)
```
