from typing import Container, Pattern, Text
from prompt_toolkit.application import Application
from prompt_toolkit.document import Document
from prompt_toolkit.filters import has_focus
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import Float, FloatContainer, HSplit, HorizontalAlign, VSplit, Window, WindowAlign
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.styles import Style, style
from prompt_toolkit.utils import Event
from prompt_toolkit.widgets import SearchToolbar, TextArea
from prompt_toolkit.widgets.base import Frame
from prompt_toolkit.widgets import Box, Button, Frame, Label, TextArea
from prompt_toolkit.shortcuts import set_title
from prompt_toolkit.application.current import get_app
from prompt_toolkit.shortcuts import yes_no_dialog
from prompt_toolkit.shortcuts import message_dialog

import time
import numpy as np
id2 = 0
class game:
    
    def __init__(self) -> None:

        self.it = 1
        self.count1 = 0
        self.text1 = "*"
        self.color = "bg:#ff3232"
        self.ar  = [["*","*","*"],["*","*","*"],["*","*","*"]]
        self.store1 = np.zeros((10,3,3))
        self.container1 = TextArea(text=self.text1,height=2,style="#e3103e bg:#ffffff")
        self.container2 = TextArea(text=self.text1,height=2,style="#e3103e bg:#ffffff")
        self.container3 = TextArea(text=self.text1,height=2,style="#e3103e bg:#ffffff")
        self.container4 = TextArea(text=self.text1,height=2,style="#e3103e bg:#ffffff")
        self.container5 = TextArea(text=self.text1,height=2,style="#e3103e bg:#ffffff")
        self.container6 = TextArea(text=self.text1,height=2,style="#e3103e bg:#ffffff")
        self.container7 = TextArea(text=self.text1,height=2,style="#e3103e bg:#ffffff")
        self.container8 = TextArea(text=self.text1,height=2,style="#e3103e bg:#ffffff")
        self.container9 = TextArea(text=self.text1,height=2,style="#e3103e bg:#ffffff")
        # Style.
        self.button1 = Button(text= " Exit ", width=10 ,
                              right_symbol= ">", left_symbol= "<", handler=self.do_exit)
        self.style = Style(
            [
                ("output-field", "bg:#000044 #ffffff"),
                ("input-field", "bg:#000000 #ffffff"),
                ("line", "#004400"),
            ]
        )
        # The key bindings.
        self.kb = KeyBindings()
        @self.kb.add("c-c")
        @self.kb.add("c-q")
        def _(event):
            "Pressing Ctrl-Q or Ctrl-C will exit the user interface."
            event.app.exit()
    
    def do_exit(self):
        get_app().exit()
        
    def on_invalidate(self,event):

        global id2
        if id2<self.count1:
            time.sleep(1)
            for i in range(3):
                for j in range(3):
                    if self.store1[id2][i][j]==0.0:
                        self.ar[i][j]="|###|\n|###|"
                    else:
                        self.ar[i][j]=str(self.store1[id2][i][j])
                        
            id2+=1
        else:
            time.sleep(2)
            get_app().exit()
        
        self.container1.buffer.document = Document(text = self.ar[0][0])
        self.container2.buffer.document = Document(text = self.ar[0][1])
        self.container3.buffer.document = Document(text = self.ar[0][2])
        self.container4.buffer.document = Document(text = self.ar[1][0])
        self.container5.buffer.document = Document(text = self.ar[1][1])
        self.container6.buffer.document = Document(text = self.ar[1][2])
        self.container7.buffer.document = Document(text = self.ar[2][0])
        self.container8.buffer.document = Document(text = self.ar[2][1])
        self.container9.buffer.document = Document(text = self.ar[2][2])

    def container(self):
        return Frame(
            FloatContainer(
            content=Box(
                HSplit(
                    [
                        VSplit([
                            Frame(
                                self.container1,
                                height=4,
                                ),
                            Frame(
                                self.container2,
                                height=4,
                                ),
                            Frame(
                                self.container3,
                                height=4,
                                ),
                            ],
                               padding_char='|',
                               padding=1,
                               ),
                        VSplit(
                            [
                                Frame(
                                    self.container4,
                                    height=4,
                                    ),
                                Frame(
                                    self.container5,
                                    height=4,
                                    ),
                                Frame(
                                    self.container6,
                                    height=4,
                                    ),
                                ],
                            padding_char='|',
                            padding=1,
                            ),
                        VSplit(
                            [
                                Frame(
                                    self.container7,
                                    height=4,
                                    ),
                                Frame(
                                    self.container8,
                                    height=4,
                                    ),
                                Frame(
                                    self.container9,
                                    height=4,
                                    ),
                                ],
                            padding_char='|',
                            padding=1,
                            ),
                        ],
                    padding=1,
                    padding_char='-',
                    padding_style='#00ffff',
                    ),
                ),
            floats=[
                Float(
                    xcursor=False,
                    ycursor=False,
                    content = Frame(
                        Box(
                            self.button1,
                        ),  
                    ),
                    top=1,
                    right=1,
                    
                )
            ] 
            ),
            style='bg:#0081db',
        )
        
        
    def run(self,store,count):
        application = Application(
            layout=Layout(self.container()),
            key_bindings=self.kb,
            style=self.style,
            mouse_support=True,
            full_screen=True,
            refresh_interval=0.1,
            on_invalidate=self.on_invalidate
        )
        self.count1 = count
        self.store1 = store
        application.run()
        finalscreen = message_dialog(
            title='8 PUZZLE GAME',
            text='Press Enter to Quit.'
            )
        finalscreen.run()


if __name__ == "__main__":
    set_title("8 PUZZLE GAME")
    # Game = game()
    # Game.run()