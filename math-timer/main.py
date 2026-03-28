from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient
import jwt
from jwt import encode as jwt_encode
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException
from bson import ObjectId

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    username: str = None
    email: str
    password: str

client = MongoClient("mongodb://localhost:27017")
db = client["ppDB"]
users_collection = db["users"]

SECRET_KEY = "not-yet-generated"
security = HTTPBearer()

@app.get("/")
def homepage():
    return {"message": "Welcome text"}

@app.post("/login")
def login(user: User):
    user_data = users_collection.find_one(
        {"email": user.email, "password": user.password}
    )

    if user_data:
        token = generate_token(user.email)
        user_data["_id"] = str(user_data["_id"])
        user_data["token"] = token
        return user_data
    
    return {"message":"Invalid email or password"}

@app.post("/register")
def register(user: User):
    existing_user = users_collection.find_one({"email": user.email})

    if existing_user:
        return{"message": "User already exists"}

    user_dict = user.dict()
    users_collection.insert_one(user_dict)
    token = generate_token(user.email)
    user_dict["_id"] = str(user_dict["_id"])
    user_dict["token"] = token
    return user_dict

@app.get("/api/user")
def get_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    user_data = {
        "username": "TestUser",
        "email": "example@mail.cpm"
    }

    if user_data["username"] and user_data["email"]:
        return user_data
    raise HTTPException(status_code = 401, detail="Invalid token")

def generate_token(email: str) -> str:
    payload = {"email": email}
    token = jwt_encode(payload, SECRET_KEY, algorithm="HS256")
    return token

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

