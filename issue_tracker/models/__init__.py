from issue_tracker.models.base import Model
from issue_tracker.models.users import UserModel


tables = [
    UserModel.__table__,
]