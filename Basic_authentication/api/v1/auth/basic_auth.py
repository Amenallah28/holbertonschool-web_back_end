#!/usr/bin/env python3
""" Module of Basic Authentication
"""
from api.v1.auth.auth import Auth
from typing import TypeVar

class BasicAuth(Auth):
    """basic authenticatin class
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Extract Base 64 Authorization Header"""
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return (authorization_header[6:])
    
