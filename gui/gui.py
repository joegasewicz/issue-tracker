import wx

from issue_tracker.issue_tracker import IssueTracker


class Gui:

    wx_app: wx.App
    main_frame: wx.Frame
    issue_tracker: IssueTracker

    def __init__(self, *, issue_tracker: IssueTracker):
        self.issue_tracker = issue_tracker
        self.wx_app = wx.App()
        self.main_frame = wx.Frame(parent=None, title="JIRA Issue Tracker")

    def run(self) -> None:
        self.main_frame.Show()
        self.wx_app.MainLoop()
