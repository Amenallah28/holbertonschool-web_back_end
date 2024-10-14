#!/usr/bin/env python3
"""
Methods to handle the apps
authentication and login related functions
"""
from db import DB
import bcrypt
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound

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
            registered_user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            registered_user = self._db.add_user(email, hashed_password)
            return registered_user
        else:
            raise ValueError