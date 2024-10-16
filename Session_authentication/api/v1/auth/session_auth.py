#!/usr/bin/env python3
"""Session authentication"""

from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """SessionAuth class"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """create_session method that creates a Session ID for a user_id"""

        if user_id is None or type(user_id) != str:
            return None
        sessionId = str(uuid4())
        self.user_id_by_session_id[sessionId] = user_id
        return sessionId

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """user_id_for_session_id that returns
        a User ID based on a Session ID"""

        if session_id is None or type(session_id) != str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """current_user that returns a User instance based on a cookie value"""

        user_id = self.user_id_for_session_id(self.session_cookie(request))
        return User.get(user_id)

    def destroy_session(self, request=None):
        """destroy_session that deletes
        the user session / logout"""

        if request is None:
            return False
        session_id = self.session_cookie(request)
        if not session_id:
            return False
        if not self.user_id_for_session_id(session_id):
            return False
        del self.user_id_by_session_id[session_id]
        return True