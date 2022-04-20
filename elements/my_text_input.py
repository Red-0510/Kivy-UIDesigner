from kivy.uix.textinput import TextInput
class My_Text_Input(TextInput):
    def __init__(self,poshints,size,keys,**kwargs):
        self.heirarchy={}
        super(My_Text_Input,self).__init__(pos_hint=poshints,size_hint=size,**keys,**kwargs)