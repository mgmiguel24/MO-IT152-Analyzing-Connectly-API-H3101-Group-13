# MO-IT152 | Connectly API
### Section H3101 | Group 13

A REST API built with Django and Django REST Framework simulating a simple social platform with Users, Posts, and Comments.

---

## 🚀 How to Run This Project

### 1. Install requirements
```bash
pip3 install -r requirements.txt
```

### 2. Set up the database
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### 3. Create an admin account
```bash
python3 manage.py createsuperuser
```

### 4. Start the server
```bash
python3 manage.py runserver
```

### 5. Open your browser
- API Root: http://127.0.0.1:8000/api/
- Admin Panel: http://127.0.0.1:8000/admin/

---

## 📡 API Endpoints

| Method | URL | What it does |
|--------|-----|-------------|
| GET | /api/users/ | List all users |
| POST | /api/users/ | Create a user |
| GET | /api/users/{id}/ | Get one user |
| PUT | /api/users/{id}/ | Update a user |
| DELETE | /api/users/{id}/ | Delete a user |
| GET | /api/posts/ | List all posts |
| POST | /api/posts/ | Create a post |
| GET | /api/posts/{id}/ | Get one post |
| PUT | /api/posts/{id}/ | Update a post |
| DELETE | /api/posts/{id}/ | Delete a post |
| GET | /api/comments/ | List all comments |
| POST | /api/comments/ | Create a comment |
| GET | /api/comments/{id}/ | Get one comment |
| PUT | /api/comments/{id}/ | Update a comment |
| DELETE | /api/comments/{id}/ | Delete a comment |

---

## 📦 Tech Stack
- Python 3
- Django 4.2+
- Django REST Framework 3.14+
- SQLite (database)

---

## 👥 Team Members
- Kirk Martin Sevillano
- Harvey Punsalan
- Akeem Karlo Apura
- Mikee Miguel
