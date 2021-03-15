import wx
import helloWX


class subClass(helloWX.MyFrame1):
    def __init__(self, parent):
        helloWX.MyFrame1.__init__(self, parent)

    def m_button1OnButtonClick(self, event):
        frame2.Show()


class subClass2(helloWX.MyFrame2):
    def __init__(self, parent):
        helloWX.MyFrame2.__init__(self, parent)


app = wx.App()
frame = subClass(parent=None)
frame2 = subClass2(parent=None)
frame.Show()
app.MainLoop()
