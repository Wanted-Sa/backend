import re

from pydantic import BaseModel, validator


class AccountValidator(BaseModel):
    email: str 
    password: str 
    
    @validator("email")
    def email_validator(cls, email):
        email_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+[.]?\w{2,3}$'
        if not re.search(email_regex, email):
            raise ValueError("Invalid email format")
        
    @validator("password")
    def password_validator(cls, password):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters")


    