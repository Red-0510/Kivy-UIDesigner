from kivy.uix.label import Label
class My_Label_Layout(Label):
    def __init__(self,pos,parent_object,keys,**kwargs):
        poshints={'x':pos[0]/parent_object.width,'y':pos[1]/parent_object.height}
        size=(pos[2]/parent_object.width,pos[3]/parent_object.height)
        self.heirarchy={}
        super(My_Label_Layout,self).__init__(pos_hint=poshints,size_hint=size,**keys,**kwargs)