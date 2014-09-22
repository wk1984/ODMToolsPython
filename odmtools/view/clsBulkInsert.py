# -*- coding: utf-8 -*- 

# ##########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
try:
    import wx.lib.platebtn as platebtn
except ImportError:
    import platebtn
from wx.lib.agw import gradientbutton as GB
from odmtools.common.icons.icons4addpoint import *



###########################################################################
## Class BulkInsert
###########################################################################

class BulkInsert(wx.MiniFrame):
    def __init__(self, parent):
        wx.MiniFrame.__init__(self, parent, id=wx.ID_ANY, title="- ODMTools Bulk Insert -",
                              size=(400, 600), style=wx.CAPTION | wx.TAB_TRAVERSAL |
                                                     wx.FRAME_FLOAT_ON_PARENT)
        mainPanel = wx.Panel(self, -1)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        #self.csvLabel = wx.StaticText(mainPanel, wx.ID_ANY, u"Select a CSV", wx.DefaultPosition, wx.DefaultSize, 0)
        self.uploadBtn = GB.GradientButton(mainPanel, wx.ID_ANY, upload_2_32.GetBitmap(), ' Upload')
        #self.saveTemplateLabel = wx.StaticText(mainPanel, wx.ID_ANY, u"Save Template", wx.DefaultPosition, wx.DefaultSize, 0)
        self.templateBtn = GB.GradientButton(mainPanel, wx.ID_ANY, downloading_updates_32.GetBitmap(), ' Download')
        #self.templateBtn = wx.BitmapButton(mainPanel, wx.ID_ANY, downloading_updates_32.GetBitmap(), name=' Download', pos=wx.DefaultPosition, size=wx.DefaultSize,  )
        self.closeBtn = GB.GradientButton(mainPanel, wx.ID_ANY, close_window_32.GetBitmap(), " Close")
        #self.saveBtn = GB.GradientButton(mainPanel, wx.ID_ANY,check_mark_3_32.GetBitmap() , " Done" )

        #self.csvLabel.Wrap(-1)
        #self.saveTemplateLabel.Wrap(-1)
        self._initSizers(mainPanel)

        self.Bind(wx.EVT_BUTTON, self.onUpload, self.uploadBtn)
        self.Bind(wx.EVT_BUTTON, self.onTemplate, self.templateBtn)
        self.Bind(wx.EVT_BUTTON, self.onClose, self.closeBtn)

    def _initSizers(self, mainPanel):
        mainSizer = wx.BoxSizer(wx.VERTICAL)

        sbCSVSizer = wx.StaticBoxSizer(wx.StaticBox(mainPanel, wx.ID_ANY, u"Upload CSV"), wx.VERTICAL)

        fgCSVSizer = wx.FlexGridSizer(0, 2, 0, 0)
        fgCSVSizer.SetFlexibleDirection(wx.VERTICAL)
        # fgCSVSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        #fgCSVSizer.Add(self.csvLabel, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        fgCSVSizer.Add(self.uploadBtn, 0, wx.ALL, 5)

        sbCSVSizer.Add(fgCSVSizer, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        mainSizer.Add(sbCSVSizer, 1, wx.EXPAND, 5)

        sbTemplateSizer = wx.StaticBoxSizer(wx.StaticBox(mainPanel, wx.ID_ANY, u"Download CSV Template"), wx.VERTICAL)
        fgTemplateSizer = wx.FlexGridSizer(0, 2, 0, 0)
        fgTemplateSizer.SetFlexibleDirection(wx.VERTICAL)
        #fgTemplateSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        #fgTemplateSizer.Add(self.saveTemplateLabel, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        fgTemplateSizer.Add(self.templateBtn, 0, wx.ALL, 5)

        sbTemplateSizer.Add(fgTemplateSizer, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        mainSizer.Add(sbTemplateSizer, 1, wx.EXPAND, 5)

        fgButtonSizer = wx.FlexGridSizer(0, 2, 0, 0)
        fgButtonSizer.SetFlexibleDirection(wx.VERTICAL)
        fgButtonSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        fgButtonSizer.Add(self.closeBtn, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        #fgButtonSizer.Add(self.saveBtn, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        mainSizer.Add(fgButtonSizer, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 15)

        mainPanel.SetSizer(mainSizer)
        mainSizer.Layout()
        mainSizer.Fit(self)


    def __del__(self):
        pass

    ## Virtual event handlers, overridden in inherited class
    def onUpload(self, event):
        event.Skip()
    def onTemplate(self, event):
        event.Skip()
    def onClose(self, event):
        event.Skip()



