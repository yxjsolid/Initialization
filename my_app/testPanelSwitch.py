from wxPython.wx import *
#import wx


class MyFrame(wxFrame):
    """
    This is MyFrame.  It just shows a few controls on a wxPanel,
    and has a simple menu.
    """
    def __init__(self, parent, title):
        wxFrame.__init__(self, parent, -1, title, size=(350, 200))

        menuBar = wxMenuBar()
        menu = wxMenu()
        menu.Append(101, "E&xit\tAlt-X", "Exit demo")
        EVT_MENU(self, 101, self.OnButton)
        menuBar.Append(menu, "&File")
        self.SetMenuBar(menuBar)

        self.Panel1()


    def Panel1(self):
        panel = wxPanel(self, -1)
        text = wxStaticText(panel, -1, "Hello World!")
        text.SetFont(wxFont(12, wxSWISS, wxNORMAL, wxBOLD))
        text.SetSize(text.GetBestSize())
        btn = wxButton(panel, -1, "Panel2")
        btn.SetDefault()

        sizer = wxBoxSizer(wxVERTICAL)
        sizer.Add(text, 0, wxALL, 10)
        sizer.Add(btn, 0, wxALL, 10)
        panel.SetSizer(sizer)
        panel.SetAutoLayout(True)
        panel.Layout()

        EVT_BUTTON(self, btn.GetId(), self.OnButton1)
        self.panel1 = panel

    def OnButton1(self, evt):
        """Event handler for the button click."""
        print "OnButton1"
        self.panel1.Destroy()
        self.Panel2()
        
        self.Update()
        
        

    def Panel2(self):
#        panel = wxPanel(self, -1)
        panel = wxPanel(self, -1, size=self.GetClientSize())
        text = wxStaticText(panel, -1, "Hello again!")
        text.SetFont(wxFont(12, wxSWISS, wxNORMAL, wxBOLD))
        text.SetSize(text.GetBestSize())
        btn = wxButton(panel, -1, "Close")
        btn.SetDefault()

        sizer = wxBoxSizer(wxVERTICAL)
        sizer.Add(text, 0, wxALL, 10)
        sizer.Add(btn, 0, wxALL, 10)
        panel.SetSizer(sizer)
        panel.SetAutoLayout(True)
        panel.Layout()

        EVT_BUTTON(self, btn.GetId(), self.OnButton)

        # what should I do here to show the new panel???
        # The calls below did not work.
        #self.Refresh()
        #self.Update()
        #wxSafeYield()
        #panel.Show()


    def OnButton(self, evt):
        """Event handler for the button click."""
        print "OnButton"
        self.Close()

app = wxPySimpleApp()
frame = MyFrame(None, "Simple wxPython App")
frame.Show(True)
app.MainLoop() 