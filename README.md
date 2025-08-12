# 📖 Word Declaration App – Backend

A FastAPI-powered backend that helps users save, retrieve, and search Bible verses to encourage them whenever they feel sad.

It uses OpenAI embeddings for semantic verse matching and supports secure user authentication.

## 🚀 Features
- User Authentication – Secure registration and login using JWT.

- Save Favorite Verses – Store personal verses for future encouragement.

- Semantic Search – Find verses similar in meaning to a user’s input using embeddings & cosine similarity.

- Protected Routes – Only authenticated users can save or view their own verses.

- SQLite Database – Persistent local storage (easily swappable for Postgres/MySQL).

## 🛠️ Tech Stack
- Python
- FastAPI - API framework
- SQLAlchemy - ORM for database management
- SQLite - Default database
- JWT(PyJWT) - Authentication
- bcrypt - Password hashing
- OpenAI API - Embedding generation
- uvicorn - ASGI server

## 📁 Project Structure
```
word-declaration-app/
│── app/
│   ├── main.py              
│   ├── models/
|   |   ├── database.py
|   |   ├── saved_verse_model.py            
│   |   ├── schemas.py
|   |   ├── users_model.py           
│   ├── routes/
│   │   ├── auth.py        
│   │   ├── saved-verses.py   
|   |   ├── scripture.routes.py      
│   ├── services/
│   │   ├── generate_embeddings.py
│   │   ├── openai_service.py
|   |   ├── utils.py 
│── requirements.txt                        
│── README.md
```

## ⚙️ Setup & Installation

1. **Clone this repo**
   ```bash
   git clone https://github.com/jmeiza/word-declaration-app.git
   cd word-declaration-app
   ```

2. **Create Virtual Environment and Install Dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate     #Mac/Linux
   venv\Scripts\activate        #Windows
   ```

3. **Configure Environment Variables**
    Create a .env file in the root directory and add:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    SECRET_KEY=your_secret_key
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```

4. **Start server**
   uvicorn app.main:app --reload


## 📡 API Endpoints
    Method	Endpoint	    Description
    POST	/auth/register	Create new user

    POST	/auth/login	    Login & get token

    GET     /get-scripture  Return scripture based on feeling

    POST    /saved-verses   Save verse to user's account (needs jwt token)

    GET     /saved-verses   Retrieve all of user's saved verses (needs jwt token)

### Register Example
    POST /auth/register
    Content-Type: application/json
    ```json
    {
        "username": "test",
        "email": "test@example.com,
        "password": "password1"
    }
    ```

### Login Example
    POST /auth/login
    Content-Type: application/json
    {
        "email": "test@example.com,
        "password": "password1"
    }
### Login return
    ```
    {
        "access_token": "your.jwt.token
        "token_type": "bearer"
    }
    ```
    
### Get Scripture Example (Postman)
    GET /get-scripture

    http://127.0.0.1:8000/get-scripture?feeling=I am feeling anxious and unhappy.

### Save a Verse
    POST /saved-verses
    Headers:
    ```
    Authorization: Bearer <your_access_token_here>
    Content-Type: application/json
    ```
    Request Body:
    ```
    {
    "verse": "For I know the plans I have for you, declares the LORD, plans to prosper you and not to harm you, plans to give you a future and a hope.",
    "reference": "Jeremiah 29:11",
    "feeling": "Hopeful"
    }
    ```