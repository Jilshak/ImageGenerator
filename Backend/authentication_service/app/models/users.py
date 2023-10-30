from sqlalchemy import Column, Integer, String, Boolean, ARRAY
from ..models import database
# from models import database --> for using it in local without docker
# from pydantic_models import users --> for using it in local without docker
from ..pydantic_models import users


class UserModel(users.UserBase):
    id: int
    class Config:
        from_attributes = True

# tha database schema
class User(database.Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    hashed_password = Column(String)