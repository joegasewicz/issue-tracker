import os


class Config:
    APPLICATION_TYPE = os.environ.get("APPLICATION_TYPE", "gui")
    SQLITE_DATABASE_NAME = os.environ.get("SQLITE_DATABASE_NAME", "issue_tracker.sqlite")
