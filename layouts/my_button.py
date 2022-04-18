from kivy.uix.button import Button

class My_Button_Layout(Button):
    def __init__(self,pos,parent_object,keys,**kwargs):
        poshints={'x':pos[0]/parent_object.width,'y':pos[1]/parent_object.height}
        size=(pos[2]/parent_object.width,pos[3]/parent_object.height)
        self.heirarchy={}
        super(My_Button_Layout,self).__init__(pos_hint=poshints,size_hint=size,**keys,**kwargs)
