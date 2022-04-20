
import kivy
from kivy.app import App 
from kivy.uix.stacklayout import StackLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Line,Color
from ast import literal_eval
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
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
        self.layout={'Header': {'parent': '', 'type': 'RL', 'arguments': {}, 'size_hint': [0.985, 0.2275], 'pos_hint': {'x': 0.00625, 'y': 0.753}},
                    'Title': {'parent': 'Header', 'type': 'LL', 'arguments': {'markup': 'True', 'font_size': '50sp', 'text': '[b]Hunters Shop[/b]'}, 'size_hint': [0.6230964467005076, 0.3142857142857143], 'pos_hint': {'x': 0.19035532994923857, 'y': 0.6476190476190476}},
                    'Name': {'parent': 'Header', 'type': 'LL', 'arguments': {'markup': 'True', 'font_size': '25sp', 'text': '[b]Name:[/b]'}, 'size_hint': [0.18781725888324874, 0.26666666666666666], 'pos_hint': {'x': 0.006345177664974619, 'y': 0.3333333333333333}}, 
                    'Date': {'parent': 'Header', 'type': 'LL', 'arguments': {'markup': 'True', 'font_size': '25sp', 'text': '[b]Date:[/b]'}, 'size_hint': [0.18781725888324874, 0.22857142857142856], 'pos_hint': {'x': 0.006345177664974619, 'y': 0.06666666666666667}}, 
                    'Name_input': {'parent': 'Header', 'type': 'TI', 'arguments': {}, 'size_hint': [0.7017766497461929, 0.26666666666666666], 'pos_hint': {'x': 0.19923857868020303, 'y': 0.3142857142857143}}, 
                    'Date_input': {'parent': 'Header', 'type': 'TI', 'arguments': {}, 'size_hint': [0.26903553299492383, 0.23809523809523755], 'pos_hint': {'x': 0.19923857868020303, 'y': 0.03809523809523864}}, 
                    'Time': {'parent': 'Header', 'type': 'LL', 'arguments': {'markup': 'True', 'font_size': '25sp', 'text': '[b]Time:[/b]'}, 'size_hint': [0.18274111675126903, 0.24761904761904707], 'pos_hint': {'x': 0.4987309644670051, 'y': 0.028571428571429112}}, 
                    'Time_input': {'parent': 'Header', 'type': 'TI', 'arguments': {}, 'size_hint': [0.20939086294416243, 0.2571428571428566], 'pos_hint': {'x': 0.6916243654822335, 'y': 0.028571428571429112}}, 
                    'Item_details': {'parent': '', 'type': 'RL', 'arguments': {}, 'size_hint': [0.98625, 0.6174999999999999], 'pos_hint': {'x': 0.00625, 'y': 0.12466666666666675}}, 
                    'Functional_buttons': {'parent': '', 'type': 'RL', 'arguments': {}, 'size_hint': [0.9825, 0.10616666666666666], 'pos_hint': {'x': 0.0075, 'y': 0.009833333333333414}}, 
                    'Item_name': {'parent': 'Item_details', 'type': 'LL', 'arguments': {'markup': 'True', 'font_size': '25sp', 'text': '[b]Item Name[/b]'}, 'size_hint': [0.46134347275031684, 0.11228070175438616], 'pos_hint': {'x': 0.0063371356147021544, 'y': 0.8736842105263155}}, 
                    'Quantity': {'parent': 'Item_details', 'type': 'LL', 'arguments': {'markup': 'True', 'font_size': '25sp', 'text': '[b]Quantity[/b]'}, 'size_hint': [0.1761723700887199, 0.10877192982456141], 'pos_hint': {'x': 0.4740177439797212, 'y': 0.8736842105263155}}, 
                    'Rate': {'parent': 'Item_details', 'type': 'LL', 'arguments': {'markup': 'True', 'font_size': '20sp', 'text': '[b]Rate(1 piece)[/b]'}, 'size_hint': [0.17110266159695817, 0.10877192982456141], 'pos_hint': {'x': 0.6552598225602028, 'y': 0.8736842105263155}}, 
                    'Total': {'parent': 'Item_details', 'type': 'LL', 'arguments': {'markup': 'True', 'font_size': '25sp', 'text': '[b]Total[/b]'}, 'size_hint': [0.16096324461343473, 0.11578947368421072], 'pos_hint': {'x': 0.8326996197718631, 'y': 0.8701754385964909}}, 
                    'Add_item': {'parent': 'Functional_buttons', 'type': 'BL', 'arguments': {'markup': 'True', 'font_size': '25sp', 'text': '[b]Add Item[/b]'}, 'size_hint': [0.3053435114503817, 0.8367346938775504], 'pos_hint': {'x': 0.005089058524173028, 'y': 0.08163265306122391}}, 
                    'Total_up': {'parent': 'Functional_buttons', 'type': 'BL', 'arguments': {'markup': 'True', 'font_size': '25sp', 'text': '[b]Total Up[/b]'}, 'size_hint': [0.356234096692112, 0.8163265306122444], 'pos_hint': {'x': 0.3155216284987278, 'y': 0.10204081632653003}},
                    'Print': {'parent': 'Functional_buttons', 'type': 'BL', 'arguments': {'markup': 'True', 'font_size': '25sp', 'text': '[b]Print[/b]'}, 'size_hint': [0.32061068702290074, 0.7959183673469382], 'pos_hint': {'x': 0.6755725190839694, 'y': 0.12244897959183615}},
                    'Data_box': {'parent': '', 'type': 'RL', 'arguments': {}, 'size_hint': [0.9725, 0.4658333333333334], 'pos_hint': {'x': 0.0125, 'y': 0.18316666666666662}}, 
                    'Grand_total': {'parent': '', 'type': 'LL', 'arguments': {'markup': 'True', 'font_size': '25sp', 'text': '[b]Grand Total :[/b]'}, 'size_hint': [0.175, 0.04983333333333327], 'pos_hint': {'x': 0.65875, 'y': 0.129}}, 
                    'Grand_total_value': {'parent': '', 'type': 'LL', 'arguments': {'font_size': '25sp', 'text': ''}, 'size_hint': [0.14875, 0.04983333333333327], 'pos_hint': {'x': 0.8375, 'y': 0.129}}
                    }#{"id":{parent,type,arguments,pos_hints,size_hints}}
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
            self.initialize_layout()

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
        
        self.layout_screen.ids._drawing_area.initialize_layout()
        self.logic_block=Logic_Block(self.app_screen,self.layout_screen)
        self.current="app_screen"

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
            if field=='quantity' and entry.text!='':
                self.logic_block.item_data[self]['quantity']=int(entry.text)
            elif field=='rate' and entry.text!='':
                self.logic_block.item_data[self]['rate']=float(entry.text)
            else:
                self.logic_block.item_data[self][field]=entry.text
        else:
            quantity=0
            rate=0
            try:
                quantity=int(self.quantity.text)
                print(quantity,type(quantity))
                rate=float(self.rate.text)
                print(rate,type(rate))
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
        self.box=StackLayout(orientation="tb-lr",size_hint=(1,1))
        self.data=Item_Data(self)
        self.box.add_widget(self.data)
        data_box.add_widget(self.box)
    def add_item(self,button):
        self.total_up(None)
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