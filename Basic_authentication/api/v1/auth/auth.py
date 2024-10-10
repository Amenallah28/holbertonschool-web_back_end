#!/usr/bin/env python3
""" Module of Authentication
"""

from flask import request
from typing import List, TypeVar

class Auth:
     """ Class to manage the API authentication 
     """
     def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
           """ Method for requiring authentication """
           if path is None:
               return True
           if ( excluded_paths is None or excluded_paths == []):
               return True
           if ( path in excluded_paths or (path + "/") in excluded_paths):
               return False
           else:
               return True
           
           
     
     def authorization_header(self, request=None) -> str:
      """Method that handles authorization header
      """
      if request is None:
          return None
      if request.headers.get("Authorization"):
          return request.headers.get("Authorization")
       
     
     def current_user(self, request=None) -> TypeVar('User'):
        """ Validates current user """
        return None
     
     