import hashlib


class HasherService:
    def hash_password(self, password):
        hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
        return hashed_password

    def verify_password(self, plain_password, hashed_password):
        return self.hash_password(plain_password) == hashed_password
