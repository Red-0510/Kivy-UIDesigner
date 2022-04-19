from kivy.uix.button import Button

class My_Button_Layout(Button):
    def __init__(self,poshints,size,keys,**kwargs):
        self.heirarchy={}
        super(My_Button_Layout,self).__init__(pos_hint=poshints,size_hint=size,**keys,**kwargs)
