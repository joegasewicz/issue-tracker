import os

import config
from utils.logger import log
from gui import Gui
from issue_tracker import IssueTracker
from config import Config

ISSUE_TRACKER_GUI = os.environ.get("ISSUE_TRACKER_GUI", False)
ISSUE_TRACKER_WEB = os.environ.get("ISSUE_TRACKER_WEB", False)


if __name__ == "__main__":
    if ISSUE_TRACKER_GUI:
        config = Config()
        config.APPLICATION_TYPE = "gui"
        log.info("Launching GUI")
        issue_tracker = IssueTracker(config=config)
        gui = Gui(issue_tracker=issue_tracker)
        gui.run()

    if ISSUE_TRACKER_WEB:
        config = Config()
        log.info("Running web server...")
