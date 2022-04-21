from kivy.uix.label import Label
class My_Label_Layout(Label):
    def __init__(self,poshints,size,keys,**kwargs):
        self.heirarchy={}
        super(My_Label_Layout,self).__init__(pos_hint=poshints,size_hint=size,**keys,**kwargs)