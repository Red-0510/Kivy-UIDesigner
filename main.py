import kivy
from kivy.app import App 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics import Line
from kivy.uix.textinput import TextInput
from ast import literal_eval
from kivy.lang import Builder
from layouts import my_button,my_label,my_relative_layout,my_text_input

Builder.load_file("./layouts/layout.kv")
class ScreenLayout(BoxLayout):
    pass
class DrawingSpace(RelativeLayout):
    def __init__(self,**kwargs):
        self.i_x,self.i_y=None,None
        self.figure=None
        self.i_x,self.i_y=None,None
        self.name=None
        self.type=None
        self.args=None
        self.heirarchy={'root':self}
        self.layout={}#{"id":{parent,type,arguments,pos_hints,size_hints}}
        super(DrawingSpace,self).__init__(**kwargs)
    def on_touch_down(self, touch):
        if self.parent.add_button.button.state=='down' and self.collide_point(touch.x,touch.y):
            if not self.figure:
                self.name=self.parent.add_button.name.text
                self.type=self.parent.add_button.type.text
                try:
                    self.args=literal_eval(self.parent.add_button.args.text)
                except :
                    self.args={}
                x,y=self.to_widget(touch.x,touch.y)
                self.i_x,self.i_y=x,y
                self.draw(x,y)
        return super().on_touch_down(touch)

    def draw(self,x,y):
        with self.canvas:
            self.figure=Line(rectangle=(x,y,1,1))
    def on_touch_move(self, touch):
        if self.figure and self.collide_point(touch.x,touch.y):
            x,y=self.to_widget(touch.x,touch.y)
            self.canvas.remove(self.figure)
            with self.canvas:
                self.figure=Line(rectangle=(self.i_x,self.i_y,x-self.i_x,y-self.i_y))
        return super().on_touch_move(touch)
    def on_touch_up(self, touch):
        if self.figure:
            self.canvas.remove(self.figure)
            x,y=self.to_widget(touch.x, touch.y)
            self.widgetize(x,y)
            self.figure=None
        return super().on_touch_up(touch)
    def widgetize(self,x,y):
        if self.parent.add_button.parent_object.text=='' or self.parent.add_button.parent_object.text=='root':
            pos=(self.i_x,y,x-self.i_x,self.i_y-y)
            parent_object=self
        else:
            parent_object=self.heirarchy[self.parent.add_button.parent_object.text]
            pos=(self.i_x-parent_object.x,y-parent_object.y,x-self.i_x,self.i_y-y)
        if self.type=="RL":
            layout=my_relative_layout.My_Relative_Layout(pos,parent_object,self.args)
        elif self.type=="BL":
            layout=my_button.My_Button_Layout(pos,parent_object,self.args)
        elif self.type=='LL':
            layout=my_label.My_Label_Layout(pos,parent_object,self.args)
        elif self.type=='TI':
            layout=my_text_input.My_Text_Input(pos,parent_object,self.args)
        self.layout[self.name]={"parent":self.parent.add_button.parent_object.text,
                    "type":self.type,"arguments":self.args,"pos_hint":layout.pos_hint,"size_hint":layout.size_hint}
        self.parent.add_button.name.text=''
        self.parent.add_button.button.state='normal'
        self.i_x,self.i_y=None,None
        self.heirarchy[self.name]=layout
        parent_object.add_widget(layout)
        # self.show_heirarchy()
        print(self.layout)
    def show_heirarchy(self):
        print('///////////////')
        for k,v in self.heirarchy.items():
            print(k,v)
    
    def get_element_by_id(self,name):
        for k,v in self.heirarchy.items():
            if k==name:
                return v 
        return None

class Add_Button(RelativeLayout):
    def __init__(self,**kwargs):
        super(Add_Button,self).__init__(**kwargs)

class MyDesignerApp(App):
    def build(self):
        return ScreenLayout()
# class Logic():

         
MyDesignerApp().run()