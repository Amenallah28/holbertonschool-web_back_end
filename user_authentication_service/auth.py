#!/usr/bin/env python3
"""
Methods to handle the apps
authentication and login related functions
"""
import bcrypt

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