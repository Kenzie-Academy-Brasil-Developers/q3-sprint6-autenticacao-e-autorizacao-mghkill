from app.configs.database import db
from sqlalchemy import Column, Integer, String, DateTime
from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash

@dataclass
class UserModel(db.Model):

    
    name: str
    last_name: str
    email: str
    

    __tablename__ = "hash_user"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(127), nullable=False)
    last_name = Column(String(511), nullable=False)
    email = Column(String(255), unique=True, nullable=False )
    password_hash = Column(String(511), nullable=False)
    
    @property
    def password(self):
        raise AttributeError("Inaccessible password")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def check_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)