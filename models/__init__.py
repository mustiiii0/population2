# Placeholder for __init__.py

from extensions import db
from .user import User
from .person import Person
from .activity_log import ActivityLog

__all__ = ["db", "User", "Person", "ActivityLog"]

