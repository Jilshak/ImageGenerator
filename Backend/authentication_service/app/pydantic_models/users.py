from pydantic import BaseModel

# this is the pydantic model for response and data validation
class UserBase(BaseModel):
    username: str
    hashed_password: str
