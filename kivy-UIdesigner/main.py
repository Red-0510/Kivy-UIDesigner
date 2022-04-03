import kivy
from kivy.app import App 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics import Line
from kivy.uix.textinput import TextInput
from ast import literal_eval

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
        self.heirarchy={}
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
        return super().on_touch_up(touch)
    def widgetize(self,x,y):
        pos=(self.i_x,y,x,self.i_y)
        if self.type=="RL":
            layout=My_RelativeLayout(pos,self,self.args)
            self.add_widget(layout)
    
class My_RelativeLayout(RelativeLayout):
    def __init__(self,pos,ds,keys,**kwargs):
        poshints={'x':pos[0]/ds.width,'y':pos[1]/ds.height}
        size=((pos[2]-pos[0])/ds.width,(pos[3]-pos[1])/ds.height)
        super(My_RelativeLayout,self).__init__(pos_hint=poshints,size_hint=size,**keys,**kwargs)

class Add_Button(RelativeLayout):
    def __init__(self,**kwargs):
        super(Add_Button,self).__init__(**kwargs)

class MyDesignerApp(App):
    def build(self):
        return ScreenLayout()
         
MyDesignerApp().run()