#!/usr/bin/env python3
"""manage the API authentication"""

from flask import request
from typing import List, TypeVar
from os import getenv


class Auth():
    """Auth Class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth method"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        for i in range(len(excluded_paths)):
            if excluded_paths[i].rstrip('/') == path.rstrip('/'):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """authorization_header method"""
        if request is None:
            return None
        if "Authorization" in request.headers:
            return request.headers["Authorization"]

    def current_user(self, request=request) -> TypeVar('User'):
        """current_user method"""
        return None

    def session_cookie(self, request=None):
        """session_cookie that returns a cookie value from a request"""

        if request is None:
            return None
        sessionName = getenv("SESSION_NAME")
        _my_session_id = request.cookies.get(sessionName)
        return _my_session_id