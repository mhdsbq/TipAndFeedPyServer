import jwt
from datetime import datetime, timedelta
import os


class TokenService:
    def __init__(self):
        self.secret_key = os.getenv("JWT_SECRET")

    def create_access_token(
        self, data: dict, expires_delta: timedelta = timedelta(minutes=30)
    ):
        to_encode = data.copy()
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm="HS256")
        return encoded_jwt

    def decode_access_token(self, token: str):
        try:
            decoded_token = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            return decoded_token
        except jwt.ExpiredSignatureError:
            return {"error": "Token expired"}
        except jwt.InvalidTokenError:
            return {"error": "Invalid token"}
