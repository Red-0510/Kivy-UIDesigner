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
from kivy.uix.screenmanager import ScreenManager,Screen,SlideTransition
from layouts import my_button,my_label,my_relative_layout,my_text_input

Builder.load_file("./layouts/layout.kv")
class LayoutManager(Screen):
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
        poshints={'x':pos[0]/parent_object.width,'y':pos[1]/parent_object.height}
        size=[pos[2]/parent_object.width,pos[3]/parent_object.height]
        if self.type=="RL":
            layout=my_relative_layout.My_Relative_Layout(poshints,size,self.args)
        elif self.type=="BL":
            layout=my_button.My_Button_Layout(poshints,size,self.args)
        elif self.type=='LL':
            layout=my_label.My_Label_Layout(poshints,size,self.args)
        elif self.type=='TI':
            layout=my_text_input.My_Text_Input(poshints,size,self.args)
        self.layout[self.name]={"parent":self.parent.add_button.parent_object.text,
                    "type":self.type,"arguments":self.args,"size_hint":layout.size_hint,"pos_hint":layout.pos_hint}
        self.parent.add_button.name.text=''
        self.parent.add_button.button.state='normal'
        self.i_x,self.i_y=None,None
        self.heirarchy[self.name]=layout
        parent_object.add_widget(layout)
        # print(self.heirarchy)
        # print(parent_object)
        # print(";;;;;;;;;;;")
        #print(self.layout)
    def show_heirarchy(self):
        print('///////////////')
        for k,v in self.heirarchy.items():
            print(k,v)
    def go_to_App_Screen(self,button):
        # print('Generating Layout')
        self.parent.parent.parent.current='app_screen'
        self.parent.parent.parent.app_screen.generate_layout(self.layout)
    def delete_widget(self,button):
        if len(self.heirarchy)>1:
            widget=self.heirarchy.popitem()
            widget[1].parent.remove_widget(widget[1])
            self.layout.pop(widget[0])
            self.parent.parent.parent.app_screen.delete_widget(widget[0])

class Add_Button(RelativeLayout):
    def __init__(self,**kwargs):
        super(Add_Button,self).__init__(**kwargs)
class Window_Manager(ScreenManager):
    def __init__(self,**kwargs):
        super(Window_Manager,self).__init__(**kwargs)
        self.layout_screen=LayoutManager(name="layout_screen")
        self.app_screen=App_Screen(name="app_screen")
        self.add_widget(self.layout_screen)
        self.add_widget(self.app_screen)
        self.current="layout_screen"
class MyDesignerApp(App):
    def build(self):
        manager=Window_Manager()
        return manager
class App_Screen(Screen):
    def __init__(self,layout={},**kwargs):
        self.layout={}
        super(App_Screen,self).__init__(**kwargs)
        # self.generate_layout({'l1': {'parent': '', 'type': 'LL', 'arguments': {'text': 'hello'}, 'size_hint': [0.77, 0.06066666666666667], 'pos_hint': {'x': 0.09375, 'y': 0.8461666666666666}}})
    def generate_layout(self,layout):# dict of elements name:{parent,type,arguments,size_hint,pos_hint}
        for k,v in layout.items():
            if k in self.layout:
                continue
            if v['parent']=='' or v['parent']=='root':
                parent_object=self.background
            else:
                parent_object=self.layout[v['parent']]
            if v['type']=='RL':
                widget=my_relative_layout.My_Relative_Layout(v['pos_hint'],v['size_hint'],v['arguments'])
            elif v['type']=='BL':
                widget=my_button.My_Button_Layout(v['pos_hint'],v['size_hint'],v['arguments'])
            elif v['type']=='LL':
                widget=my_label.My_Label_Layout(v['pos_hint'],v['size_hint'],v['arguments'])
            elif v['type']=='TI':
                widget=my_text_input.My_Text_Input(v['pos_hint'],v['size_hint'],v['arguments'])
            parent_object.add_widget(widget)
            self.layout[k]=widget
    def change_layout(self,button):
        self.parent.current='layout_screen'

    def get_element_by_id(self,name):
        for k,v in self.layout.items():
            if k==name:
                return v   
        return None
    def delete_widget(self,name):
        # print("hello")
        if name in self.layout:
            widget=self.layout.pop(name)
            widget.parent.remove_widget(widget)

MyDesignerApp().run()