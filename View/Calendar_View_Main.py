'''
VIEW GUI
made by KIM Myeong Jong, CHU Ho Jin, Yun Gun Hui, Park Un Che, Lee Sang Jin
start 2018-09-18 ~
if program was started than see this view
define main frame and framework
'''


from tkinter import *
from tkinter import ttk

from Controller import temp


class App_Main_View:
    def __init__(self,parent):


        self.main_frame = Frame(parent)
        # 프레임 생성
        print(dir(self.main_frame))
        parent.geometry('1400x750+50+50')

        parent.title("Calendar")

        #-------------------------------------------------------
        frame_padding = "2m"
        #-------------------------------------------------------

        self.main_container = Frame()
        self.main_container.pack()

        self.left_frame_schedule = Frame(self.main_container, background = "red", height=680,width=190)
        self.left_frame_schedule.pack(side=LEFT, fill=BOTH, padx=frame_padding, pady=frame_padding)
        # left frame        function schedule

        self.left_top_frame = Frame(self.left_frame_schedule, background = "pink", height=100, width=190)
        self.left_top_frame.pack(side=TOP, fill=BOTH)
        # left top frame    denote day of week

        self.right_frame_nav = Frame(self.main_container, background="blue", height=680, width=190)
        self.right_frame_nav.pack(side=RIGHT, padx=frame_padding, pady=frame_padding)
        # right frame       function navigation, wheather

        self.right_top_frame = Frame(self.right_frame_nav, background="green", height=100, width=190)
        self.right_top_frame.pack(side=TOP ,fill=BOTH)
        # right top frame   function/ weather

        self.right_bottom_frame = Frame(self.right_frame_nav, background="yellow", height=680, width=190)
        self.right_bottom_frame.pack(side=BOTTOM ,fill=BOTH)
        # right bottom frame    function navigation

        # self.right_bottom_Dday = Frame(self.right_bottom_frame, background="red", height=280, width=180)
        # self.right_bottom_Dday.pack(side=TOP)
        #
        # self.right_bottom_nav = Frame(self.right_bottom_frame, background="blue", height=280, width=180)
        # self.right_frame_nav.pack(side=BOTTOM)

        self.main_frame_calendar = Frame(self.main_container, background = "red", height=680,width=980)
        self.main_frame_calendar.pack(side=TOP, padx=frame_padding, pady=frame_padding)
        # main frame        function calendar

        self.main_frame_view_month = Frame(self.main_frame_calendar, background = "white", height=100, width=980)
        self.main_frame_view_month.pack(side=TOP, fill=BOTH)
        # main frame top    function view month

        self.label_month = Label(self.main_frame_view_month, background = "white", height=2, width=20 ,text=str(temp.date_test_year)+"년 "+str(temp.date_test_month)+"월" ,font = "Helvetica 30 bold italic")
        self.label_month.pack(side=TOP)

        self.main_frame_view_day = Frame(self.main_frame_calendar, background = "gray", height=580, width=980)
        self.main_frame_view_day.pack(side=BOTTOM)
        # main frame bottom function view day [main]

        #--------------------delete-----------------------
        # font = font.Font()
        #-------------------------------------------------

        for i in range(0,6):
            for j in range(0,7):

                self.button_main = Button(self.main_frame_view_day, width=6, height=2, background="gray24" ,foreground="yellow",text=","+str(temp.date_test_start_point),  font = "Helvetica 25 bold italic").grid(row = i, column = j)

        self.main_frame.pack()

        # lbl.pack()
        # 패커 관리자 - 간단한 레이아웃을 최적화 시켜줌

test = Tk()
a = App_Main_View(test)
test.mainloop()
