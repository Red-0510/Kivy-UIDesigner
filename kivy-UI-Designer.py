
import kivy
from kivy.app import App 
from kivy.uix.stacklayout import StackLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Line,Color
from ast import literal_eval
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.metrics import dp
from elements import my_button,my_label,my_relative_layout,my_text_input
import json

Builder.load_file("./elements/layout.kv")
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
            Color(0,0,0,1)
            self.figure=Line(rectangle=(x,y,1,1))
    def on_touch_move(self, touch):
        if self.figure and self.collide_point(touch.x,touch.y):
            x,y=self.to_widget(touch.x,touch.y)
            self.canvas.remove(self.figure)
            with self.canvas:
                Color(0,0,0,1)
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
        # print(self.layout)
        self.parent.parent.parent.current='app_screen'
        self.parent.parent.parent.app_screen.generate_layout(self.layout)
    def delete_widget(self,button):
        if len(self.heirarchy)>1:
            widget=self.heirarchy.popitem()
            widget[1].parent.remove_widget(widget[1])
            self.layout.pop(widget[0])
            self.parent.parent.parent.app_screen.delete_widget(widget[0])
    def initialize_layout(self):
        self.parent.parent.parent.app_screen.generate_layout(self.layout)
        for k,v in self.layout.items():
            if k in self.heirarchy:
                continue
            if v['parent']=='' or v['parent']=='root':
                parent_object=self
            else:
                parent_object=self.heirarchy[v['parent']]
            if v['type']=='RL':
                widget=my_relative_layout.My_Relative_Layout(v['pos_hint'],v['size_hint'],v['arguments'])
            elif v['type']=='BL':
                widget=my_button.My_Button_Layout(v['pos_hint'],v['size_hint'],v['arguments'])
            elif v['type']=='LL':
                widget=my_label.My_Label_Layout(v['pos_hint'],v['size_hint'],v['arguments'])
            elif v['type']=='TI':
                widget=my_text_input.My_Text_Input(v['pos_hint'],v['size_hint'],v['arguments'])
            parent_object.add_widget(widget)
            self.heirarchy[k]=widget
    def save_layout(self,button):
        j=json.dumps(self.layout)
        with open('layouts.json','w') as fh:
            fh.write(j)
    def open_layout(self,button):
        layout={}
        try:
            layout=json.load(open('layouts.json'))
        except:
            pass
        if len(layout)>0:
            self.layout=layout
            self.parent.parent.parent.initialize_layout_logic()


class Add_Button(RelativeLayout):
    def __init__(self,**kwargs):
        super(Add_Button,self).__init__(**kwargs)

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
        # name=self.layout_name

class Window_Manager(ScreenManager):
    def __init__(self,**kwargs):
        super(Window_Manager,self).__init__(**kwargs)
        self.layout_screen=LayoutManager(name="layout_screen")
        self.app_screen=App_Screen(name="app_screen")
        self.add_widget(self.layout_screen)
        self.add_widget(self.app_screen)
        self.current="app_screen"
    def initialize_layout_logic(self):# initialises the logic_block and adds it into the application
        self.layout_screen.ids._drawing_area.initialize_layout()
        self.logic_block=Logic_Block(self.app_screen,self.layout_screen)
class MyDesignerApp(App):
    def build(self):
        manager=Window_Manager()
        return manager

#####################################################################
# start with your logic class and use get_element_by_id function 
# to obtain required widgets and implement the logic
#####################################################################
class Item_Data(BoxLayout):
    def __init__(self,logic_block,**kwargs):
        self.logic_block=logic_block
        super(Item_Data,self).__init__(**kwargs)
    def update(self,entry,field):
        if self in self.logic_block.item_data:
            if field=='item_name':
                self.logic_block.item_data[self]['item_name']=entry.text
                return
            try:
                self.logic_block.item_data[self][field]=float(entry.text)
            except:
                self.logic_block.item_data[self][field]=0
        else:
            quantity=0
            rate=0
            try:
                quantity=int(self.quantity.text)
                rate=float(self.rate.text) 
            except:
                pass
            self.logic_block.item_data[self]={'item_name':self.item_name.text,'quantity':quantity,'rate':rate,'total':0}
        #print(self.logic_block.item_data)

class Logic_Block():
    def __init__(self,app_screen,layout_screen):
        self.item_data={}
        self.total=0
        self.app_screen=app_screen
        self.layout_screen=layout_screen
        self.name=self.app_screen.get_element_by_id("Name_input")
        self.date=self.app_screen.get_element_by_id("Date_input")
        self.time=self.app_screen.get_element_by_id("Time_input")
        self.add_button=self.app_screen.get_element_by_id("Add_item")
        self.total_button=self.app_screen.get_element_by_id("Total_up")
        self.print_button=self.app_screen.get_element_by_id("Print")
        self.grand_total=self.app_screen.get_element_by_id("Grand_total_value")
        data_box=self.app_screen.get_element_by_id("Data_box")
        self.add_button.bind(on_press=self.add_item)
        self.total_button.bind(on_press=self.total_up)
        self.print_button.bind(on_press=self.print_data)
        scrollview=ScrollView(size_hint=(1,1))
        self.box=StackLayout(orientation="tb-lr",size_hint=(1,None),height='250dp')
        self.data=Item_Data(self)
        self.box.add_widget(self.data)
        scrollview.add_widget(self.box)
        #self.box.bind(minimum_height=self.box.setter('height'))
        data_box.add_widget(scrollview)
    def add_item(self,button):
        self.total_up(None)
        self.box.height+=dp(25)
        self.data=Item_Data(self)
        self.box.add_widget(self.data)
    def total_up(self,button):
        self.total=0
        for k,v in self.item_data.items():
            if v['quantity']!=0 and v['rate']!=0:
                v['total']=v['quantity']*v['rate']
                if v['total']!='':
                    self.total+=v['total']
                k.total.text=str(v['total'])
        self.grand_total.text=str(self.total)
        
    def print_data(self,button):
        #to save the data in file or to print the data 
        pass

MyDesignerApp().run()