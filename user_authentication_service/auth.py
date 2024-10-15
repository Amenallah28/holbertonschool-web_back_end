#!/usr/bin/env python3
"""
Methods to handle the apps
authentication and login related functions
"""
from db import DB
import bcrypt
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound
import uuid

def _hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt's hashpw method with a generated salt.

    Args:
        password (str): The password to be hashed.

    Returns:
        bytes: The hashed password as bytes.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password

def _generate_uuid() -> str:
    """generates a new uuid and returns it s string reprensation"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Method to register a new user in the database
        """
        try:
            existing_user = self._db.find_user_by(email=email)
            raise ValueError
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email=email, hashed_password=hashed_password)
            
            return new_user
        
    def valid_login(self, email: str, password: str) -> bool:
        """
        Method that locates the user by email.
        If the password matches returns True,
        otherwise returns False.
        """
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
            else:
                return False
        except NoResultFound:
            return False
        
    def create_session(self, email: str) -> str:
        """
        Method that creates a user's session ID
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id,session_id=session_id)
            return session_id
        except NoResultFound:
            return None
        
        