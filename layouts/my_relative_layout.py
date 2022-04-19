from kivy.uix.relativelayout import RelativeLayout
class My_Relative_Layout(RelativeLayout):
    def __init__(self,poshints,size,keys,**kwargs):
        self.heirarchy={}
        super(My_Relative_Layout,self).__init__(pos_hint=poshints,size_hint=size,**keys,**kwargs)
    