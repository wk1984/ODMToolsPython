"""
    ADD Point Cell Editor Logic
"""
from collections import OrderedDict

import wx
import wx.combo
from wx.lib import masked

__author__ = 'Jacob'

#### Options ####
utcOffSetBounds = (-12, 12)

class CellEdit():
    def __init__(self, serviceManager, recordService):
        self.serviceManager = serviceManager
        self.recordService = recordService
        self.cvService = serviceManager.get_cv_service()
        self.censorCodeChoices = ["NULL"] + [x.term for x in self.cvService.get_censor_code_cvs()]
        d = {x.lab_sample_code: x.id for x in self.cvService.get_samples()}
        self.labSampleChoices = ["NULL"] + OrderedDict(d).keys()

    """
        --------------------
        Custom Image Getters
        --------------------
    """
    def imgGetterDataValue(self, point):
        """Required Element

        :param point:
        :return:
        """

        if not point.dataValue:
            return "error"
        if isinstance(point.dataValue, basestring):
            for type in [int, float]:
                try:
                    value = type(point.dataValue)
                    if isinstance(value, type):
                        return "check"
                except ValueError:
                    continue
        elif isinstance(point.dataValue, int):
            return "check"
        elif isinstance(point.dataValue, float):
            return "check"
        return "error"

    def imgGetterCensorCode(self, point):
        """Required Element

        :param point:
        :return:
        """
        if not point.censorCode:
            return "error"
        if not point.censorCode in censorCodeOptions:
            return "error"
        return "check"

    def imgGetterUTCOFFset(self, point):
        """Required Element

        :param point:
        :return:
        """

        value = point.utcOffSet
        if not value:
            return "error"

        if isinstance(value, basestring):
            try:
                newValue = int(value)
                if isinstance(newValue, int):
                    if utcOffSetBounds[0] <= newValue <= utcOffSetBounds[1]:
                        return "check"
            except ValueError as e:
                pass
        return "error"

    def imgGetterValueAcc(self, point):
        """
        """
        value = point.valueAccuracy
        if not value:
            return "error"


    """
        --------------------
        Custom Value Getters
        --------------------
    """
    def valueGetterValueAccuracy(self, point):
        """Not Required

        :param point:
        :return:
        """
        if not point.valueAccuracy:
            return "error"

    """
        --------------------
        Custom Value Setters
        --------------------
    """
    def valueSetterDataValue(self, point, newValue):
        """

        :param point:
        :return:
        """
        point.dataValue = newValue

        '''
        for type in [int, float]:
            try:
                value = type(newValue)
                if isinstance(value, type):
                    point.dataValue = newValue
                    return
            except ValueError:
                continue
        '''
        # dv = point.dataValue
        #if not dv:
        #    return "NULL"
        #return "NULL"
    def valueSetterUTCOffset(self, point, newValue):
        point.utcOffSet = newValue


    """
        ------------------------
        Custom String Converters
        ------------------------
    """
    def strConverterDataValue(self, value):
        """
        """

        try:
            return str(value)
        except Exception as e:
            return str("NULL")

    def strConverterLocalTime(self, time):
        """Required Element

        :param time:
        :return:
        """
        try:
            return str(time)
        except UnicodeEncodeError as e:
            # print "Error! in the unicode encoding..."
            return str("00:00:00")

    """
        ------------------
        Custom CellEditors
        ------------------
    """

    def localTimeEditor(self, olv, rowIndex, subItemIndex):
        """

        :param olv:
        :param rowIndex:
        :param subItemIndex:
        :return:
        """

        # odcb = masked.TimeCtrl(olv, fmt24hr=True)
        odcb = TimePicker(olv)

        odcb.Bind(wx.EVT_KEY_DOWN, olv._HandleChar)
        return odcb

    def censorCodeEditor(self, olv, rowIndex, subItemIndex):
        """

        :param olv:
        :param rowIndex:
        :param subItemIndex:
        :return:
        """

        odcb = CustomComboBox(olv, choices=self.censorCodeChoices)
        # OwnerDrawnComboxBoxes don't generate EVT_CHAR so look for keydown instead
        odcb.Bind(wx.EVT_KEY_DOWN, olv._HandleChar)
        return odcb

    def labSampleCodeEditor(self, olv, rowIndex, subItemIndex):
        """

        :param olv:
        :param rowIndex:
        :param subItemIndex:
        :return:
        """

        odcb = CustomComboBox(olv, choices=self.labSampleChoices)
        odcb.Bind(wx.EVT_KEY_DOWN, olv._HandleChar)
        return odcb


class TimePicker(masked.TimeCtrl):
    """

    """
    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        kwargs['fmt24hr'] = True
        kwargs['value'] = "00:00:00"
        kwargs['style'] = wx.TE_PROCESS_ENTER
        masked.TimeCtrl.__init__(self, *args, **kwargs)

    def SetValue(self, value):
        """Put a new value into the editor"""
        print "In SetValue ", value, type(value)
        newValue = value or ""
        try:
            super(self.__class__, self).SetValue(newValue)
        except UnicodeEncodeError as e:
            newValue = unicode('00:00:00')
            super(self.__class__, self).SetValue(newValue)

class CustomComboBox(wx.combo.OwnerDrawnComboBox):
    """

    """
    def __init__(self, *args, **kwargs):
        self.popupRowHeight = kwargs.pop("popupRowHeight", 24)
        kwargs['style'] = kwargs.get('style', 0) | wx.CB_READONLY
        self.evenRowBackground = kwargs.pop("evenRowBackground", wx.WHITE)
        self.oddRowBackground = kwargs.pop("oddRowBackground", wx.Colour(191, 239, 255))
        wx.combo.OwnerDrawnComboBox.__init__(self, *args, **kwargs)

    def OnDrawBackground(self, dc, rect, item, flags):
        # If the item is selected, or we are painting the combo control itself, then use
        # the default rendering.
        if flags & (wx.combo.ODCB_PAINTING_CONTROL | wx.combo.ODCB_PAINTING_SELECTED):
            wx.combo.OwnerDrawnComboBox.OnDrawBackground(self, dc, rect, item, flags)
            return

        # Otherwise, draw every other background with different colour.
        if item & 1:
            backColour = self.oddRowBackground
        else:
            backColour = self.evenRowBackground
        dc.SetBrush(wx.Brush(backColour))
        dc.SetPen(wx.Pen(backColour))
        dc.DrawRectangleRect(rect)