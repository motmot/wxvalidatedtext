import wx
__version__ = '0.5.1' # keep in sync with setup.py

def integer_validator(input_string):
    try:
        int(input_string)
    except ValueError:
        return False
    return True

def float_validator(input_string):
    try:
        float(input_string)
    except ValueError:
        return False
    return True

class Validator:
    def __init__(self,ctrl,id,callback_func,validator_func,
                 ignore_initial_value=False,
                 pending_color='#FF7F7F',
                 valid_color=None,
                 text_color=None):

        self.ctrl = ctrl
        self.id = id
        self.callback_func = callback_func

        self.validator_func = validator_func

        self.pending_color = pending_color
        if valid_color is None:
            self.valid_color = self.ctrl.GetBackgroundColour()
        else:
            self.valid_color = valid_color
        if text_color is None:
            self.text_color = self.ctrl.GetForegroundColour()
        else:
            self.text_color = text_color

        self.ctrl.SetForegroundColour(self.text_color)

        if ignore_initial_value:
            #print 'ignoring'
            self.set_state('pending')
            self.last_valid_value = None
        else:
            if self.validator_func(self.ctrl.GetValue()):
                self.set_state('valid')
                self.last_valid_value = self.ctrl.GetValue()
            else:
                raise ValueError('initial value for ctrl is invald!')

        style = self.ctrl.GetWindowStyleFlag() # oh, yeah, baby!
        if not (style & wx.TE_PROCESS_ENTER):
            self.ctrl.SetWindowStyle( style | wx.TE_PROCESS_ENTER )

        wx.EVT_TEXT(self.ctrl, self.id, self._OnText)
        wx.EVT_TEXT_ENTER(self.ctrl, self.id, self._OnTextEnter)
        wx.EVT_KILL_FOCUS(self.ctrl, self._OnKillFocus)

    def set_state(self,state):
        if state=='valid':
            self.state = state
            self.ctrl.SetBackgroundColour(self.valid_color)
            self.last_valid_value = self.ctrl.GetValue()
        elif state=='pending':
            self.state = state
            self.ctrl.SetBackgroundColour(self.pending_color)
        else:
            raise ValueError('did not understand state')

    def _fix_value(self,event):
        value = self.ctrl.GetValue()
        if value != self.last_valid_value:
            if self.validator_func(value):
                if self.callback_func is not None:
                    self.callback_func(event)
            else:
                if self.last_valid_value is not None:
                    self.ctrl.SetValue(self.last_valid_value)
                else:
                    return
        self.set_state('valid')

    def _OnKillFocus(self,event):
        self._fix_value(event)

    def _OnTextEnter(self,event):
        self._fix_value(event)

    def _OnText(self,event):
        value = self.ctrl.GetValue()
        if value == self.last_valid_value:
            self.set_state('valid')
        else:
            self.set_state('pending')

def setup_validated_integer_callback(ctrl, id, callback_func,
                                     ignore_initial_value=False,**kwargs):
    return Validator(ctrl,
                     id,
                     callback_func,
                     integer_validator,
                     ignore_initial_value=ignore_initial_value,
                     **kwargs)

def setup_validated_float_callback(ctrl, id, callback_func,
                                   ignore_initial_value=False,**kwargs):
    return Validator(ctrl,
                     id,
                     callback_func,
                     float_validator,
                     ignore_initial_value=ignore_initial_value,
                     **kwargs)


