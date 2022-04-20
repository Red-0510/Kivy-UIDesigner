from kivy.uix.boxlayout import BoxLayout
class My_Box_Layout(BoxLayout):
    def __init__(self,poshints,size,keys,**kwargs):
        self.heirarchy={}
        super(My_Box_Layout,self).__init__(orientation="horizontal",pos_hint=poshints,size_hint=size,**keys,**kwargs)
    