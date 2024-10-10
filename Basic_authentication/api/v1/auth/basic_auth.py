#!/usr/bin/env python3
""" Module of Basic Authentication
"""
from api.v1.auth.auth import Auth
from typing import TypeVar
from base64 import b64decode

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
    
    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """Decodes the value of a base64 string
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None
        try:
            encoded = base64_authorization_header.encode('utf-8')
            decoded64 = b64decode(encoded)
            decoded = decoded64.decode('utf-8')
        except BaseException:
            return None

        return decoded