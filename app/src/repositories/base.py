from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session

from src.db.database import Database


class BaseRepository:

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory
