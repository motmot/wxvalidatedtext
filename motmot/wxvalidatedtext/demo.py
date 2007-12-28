import pkg_resources # from setuptools

import wxvalidatedtext as wxvt

import wx

import wx.xrc as xrc

import os

RESFILE = pkg_resources.resource_filename(__name__,"demo.xrc") # trigger extraction
RESDIR = os.path.split(RESFILE)[0]
RES = xrc.EmptyXmlResource()
RES.LoadFromString(open(RESFILE).read())

def validate_int_range(val_str):
    # demonstrate new validator
    try:
        val = int(val_str)
    except ValueError,err:
        return False
    if 20<val<100:
        return True
    else:
        return False

class MyApp(wx.App):
    def OnInit(self):
        # see http://pythonide.stani.be/manual/html/manual7.html
        self.frame = RES.LoadFrame(None, "TEST_FRAME")
        
        ctrl =  xrc.XRCCTRL(self.frame, "TEXT_ENTRY_INT")
        wxvt.setup_validated_integer_callback(ctrl,
                                              ctrl.GetId(),
                                              self.OnValidInteger)
        
        ctrl =  xrc.XRCCTRL(self.frame, "TEXT_ENTRY_FLOAT")
        wxvt.setup_validated_float_callback(ctrl,
                                            ctrl.GetId(),
                                            self.OnValidFloat)
        
        ctrl =  xrc.XRCCTRL(self.frame, "TEXT_ENTRY_CUSTOM")
        validator = wxvt.Validator(ctrl,
                                   ctrl.GetId(),
                                   self.OnValidCustom,
                                   validate_int_range)
        self.frame.Show(True)
        return True
    
    def OnValidInteger(self,event):
        print 'validated integer:',int(event.GetEventObject().GetValue())
    def OnValidFloat(self,event):
        print 'validated float:',float(event.GetEventObject().GetValue())
    def OnValidCustom(self,event):
        print 'validated custom value:',int(event.GetEventObject().GetValue())


def main():
    app = MyApp(0)
    app.MainLoop()

if __name__=='__main__':
    main()
    
