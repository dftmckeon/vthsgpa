#VTHS GPA Calculator, Developed By: Daniel McKeon
from Tkinter import *

class Application(Frame):
    ''' VTHS GPA Calculator
    '''
    def __init__(self, master):
        ''' Initialize the Frame
        '''
        Frame.__init__(self, master)
        self.grid()
        self.button_clicks = 0 #count button clicks
        self.create_widgets()
        
    def create_widgets(self):
        ''' Create widgets to input GPA
        '''
        Label(self, text = "VTHS Basic GPA Calculator").grid(row = 0, column = 0, sticky = W)
        
        #Instructions
        #Label(self, text = "Enter your grades in each blank and select course level:").grid(row = 1, column = 0, sticky = W)
        
        
        
        #P1 Class
        self.p1label = Label(self, text = "Period 1:")
        self.p1label.grid(row = 2, column = 0, sticky = W)
        self.p1entry = Entry(self)
        self.p1entry.grid(row = 2, column = 1, sticky = W)
        
        self.p1button1 = BooleanVar()
        Checkbutton(self, text = "Standard", variable = self.p1button1, command = self.updatemult1).grid(row = 2, column = 3, sticky = W)
        
        self.p1button2 = BooleanVar()
        Checkbutton(self, text = "CP", variable = self.p1button2, command = self.updatemult1).grid(row = 2, column = 4, sticky = W)
        
        self.p1button3 = BooleanVar()
        Checkbutton(self, text = "Honors", variable = self.p1button3, command = self.updatemult1).grid(row = 2, column = 5, sticky = W)
        
        self.p1button4 = BooleanVar()
        Checkbutton(self, text = "AP", variable = self.p1button4, command = self.updatemult1).grid(row = 2, column = 6, sticky = W)
        
        
        
        #P2 Class
        self.p2label = Label(self, text = "Period 2:")
        self.p2label.grid(row = 3, column = 0, sticky = W)
        self.p2entry = Entry(self)
        self.p2entry.grid(row = 3, column = 1, sticky = W)
        
        self.p2button1 = BooleanVar()
        Checkbutton(self, text = "Standard", variable = self.p2button1, command = self.updatemult2).grid(row = 3, column = 3, sticky = W)
        
        self.p2button2 = BooleanVar()
        Checkbutton(self, text = "CP", variable = self.p2button2, command = self.updatemult2).grid(row = 3, column = 4, sticky = W)
        
        self.p2button3 = BooleanVar()
        Checkbutton(self, text = "Honors", variable = self.p2button3, command = self.updatemult2).grid(row = 3, column = 5, sticky = W)
        
        self.p2button4 = BooleanVar()
        Checkbutton(self, text = "AP", variable = self.p2button4, command = self.updatemult2).grid(row = 3, column = 6, sticky = W)
        
        
        
        #P3 Class
        self.p3label = Label(self, text = "Period 3:")
        self.p3label.grid(row = 4, column = 0, sticky = W)
        self.p3entry = Entry(self)
        self.p3entry.grid(row = 4, column = 1, sticky = W)
        
        self.p3button1 = BooleanVar()
        Checkbutton(self, text = "Standard", variable = self.p3button1, command = self.updatemult3).grid(row = 4, column = 3, sticky = W)
        
        self.p3button2 = BooleanVar()
        Checkbutton(self, text = "CP", variable = self.p3button2, command = self.updatemult3).grid(row = 4, column = 4, sticky = W)
        
        self.p3button3 = BooleanVar()
        Checkbutton(self, text = "Honors", variable = self.p3button3, command = self.updatemult3).grid(row = 4, column = 5, sticky = W)
        
        self.p3button4 = BooleanVar()
        Checkbutton(self, text = "AP", variable = self.p3button4, command = self.updatemult3).grid(row = 4, column = 6, sticky = W)
        
        
        
        #P4 Class
        self.p4label = Label(self, text = "Period 4:")
        self.p4label.grid(row = 5, column = 0, sticky = W)
        self.p4entry = Entry(self)
        self.p4entry.grid(row = 5, column = 1, sticky = W)
        
        self.p4button1 = BooleanVar()
        Checkbutton(self, text = "Standard", variable = self.p4button1, command = self.updatemult4).grid(row = 5, column = 3, sticky = W)
        
        self.p4button2 = BooleanVar()
        Checkbutton(self, text = "CP", variable = self.p4button2, command = self.updatemult4).grid(row = 5, column = 4, sticky = W)
        
        self.p4button3 = BooleanVar()
        Checkbutton(self, text = "Honors", variable = self.p4button3, command = self.updatemult4).grid(row = 5, column = 5, sticky = W)
        
        self.p4button4 = BooleanVar()
        Checkbutton(self, text = "AP", variable = self.p4button4, command = self.updatemult4).grid(row = 5, column = 6, sticky = W)
        
        
        
        #P5 Class
        self.p5label = Label(self, text = "Period 5:")
        self.p5label.grid(row = 6, column = 0, sticky = W)
        self.p5entry = Entry(self)
        self.p5entry.grid(row = 6, column = 1, sticky = W)
        
        self.p5button1 = BooleanVar()
        Checkbutton(self, text = "Standard", variable = self.p5button1, command = self.updatemult5).grid(row = 6, column = 3, sticky = W)
        
        self.p5button2 = BooleanVar()
        Checkbutton(self, text = "CP", variable = self.p5button2, command = self.updatemult5).grid(row = 6, column = 4, sticky = W)
        
        self.p5button3 = BooleanVar()
        Checkbutton(self, text = "Honors", variable = self.p5button3, command = self.updatemult5).grid(row = 6, column = 5, sticky = W)
        
        self.p5button4 = BooleanVar()
        Checkbutton(self, text = "AP", variable = self.p5button4, command = self.updatemult5).grid(row = 6, column = 6, sticky = W)
        
        
        
        #P6 Class
        self.p6label = Label(self, text = "Period 6:")
        self.p6label.grid(row = 7, column = 0, sticky = W)
        self.p6entry = Entry(self)
        self.p6entry.grid(row = 7, column = 1, sticky = W)
        
        self.p6button1 = BooleanVar()
        Checkbutton(self, text = "Standard", variable = self.p6button1, command = self.updatemult6).grid(row = 7, column = 3, sticky = W)
        
        self.p6button2 = BooleanVar()
        Checkbutton(self, text = "CP", variable = self.p6button2, command = self.updatemult6).grid(row = 7, column = 4, sticky = W)
        
        self.p6button3 = BooleanVar()
        Checkbutton(self, text = "Honors", variable = self.p6button3, command = self.updatemult6).grid(row = 7, column = 5, sticky = W)
        
        self.p6button4 = BooleanVar()
        Checkbutton(self, text = "AP", variable = self.p6button4, command = self.updatemult6).grid(row = 7, column = 6, sticky = W)
        
        
        
        #P7 Class
        self.p7label = Label(self, text = "Period 7:")
        self.p7label.grid(row = 8, column = 0, sticky = W)
        self.p7entry = Entry(self)
        self.p7entry.grid(row = 8, column = 1, sticky = W)
        
        self.p7button1 = BooleanVar()
        Checkbutton(self, text = "Standard", variable = self.p7button1, command = self.updatemult7).grid(row = 8, column = 3, sticky = W)
        
        self.p7button2 = BooleanVar()
        Checkbutton(self, text = "CP", variable = self.p7button2, command = self.updatemult7).grid(row = 8, column = 4, sticky = W)
        
        self.p7button3 = BooleanVar()
        Checkbutton(self, text = "Honors", variable = self.p7button3, command = self.updatemult7).grid(row = 8, column = 5, sticky = W)
        
        self.p7button4 = BooleanVar()
        Checkbutton(self, text = "AP", variable = self.p7button4, command = self.updatemult7).grid(row = 8, column = 6, sticky = W)
        
        
        
        #P8 Class
        self.p8label = Label(self, text = "Period 8:")
        self.p8label.grid(row = 9, column = 0, sticky = W)
        self.p8entry = Entry(self)
        self.p8entry.grid(row = 9, column = 1, sticky = W)
        
        self.p8button1 = BooleanVar()
        Checkbutton(self, text = "Standard", variable = self.p8button1, command = self.updatemult8).grid(row = 9, column = 3, sticky = W)
        
        self.p8button2 = BooleanVar()
        Checkbutton(self, text = "CP", variable = self.p8button2, command = self.updatemult8).grid(row = 9, column = 4, sticky = W)
        
        self.p8button3 = BooleanVar()
        Checkbutton(self, text = "Honors", variable = self.p8button3, command = self.updatemult8).grid(row = 9, column = 5, sticky = W)
        
        self.p8button4 = BooleanVar()
        Checkbutton(self, text = "AP", variable = self.p8button4, command = self.updatemult8).grid(row = 9, column = 6, sticky = W)
                       
        #Calculate Button
        self.calc_button = Button(self, text = "Calculcate GPA", command = self.calc)
        self.calc_button.grid(row = 10, column = 0)
        
        #Results Text
        self.result = Text(self, width = 40, height = 5, wrap = WORD)
        self.result.grid(row = 11, column = 0, columnspan = 3)
        
        #Notes Label
        Label(self, text = "*Lunch is omitted.").grid(row = 12, column = 6, sticky = W)
        
        #Credits Label
        Label(self, text = "Developed By: Daniel McKeon").grid(row = 12, column = 0, sticky = W)
        

        
    #P1 Multiplier
    def updatemult1(self):
        ''' Multiple P1 Entry by check box selected
        '''
        grade1 = self.p1entry.get()
        global grade1weighted
        grade1weighted = None
        mult1 = 1
        
        if self.p1button1.get():
            mult1 = 1
            grade1weighted = mult1 * int(grade1)
        if self.p1button2.get():
            mult1 = 1.02
            grade1weighted = mult1 * int(grade1)
        if self.p1button3.get():
            mult1 = 1.06
            grade1weighted = mult1 * int(grade1)
        if self.p1button4.get():
            mult1 = 1.09
            grade1weighted = mult1 * int(grade1)
        

    
    #P2 Multiplier
    def updatemult2(self):
        ''' Multiple P2 Entry by check box selected
        '''
        grade2 = self.p2entry.get()
        global grade2weighted
        grade2weighted = None
        mult2 = 1
        
        if self.p2button1.get():
            mult2 = 1
            grade2weighted = mult2 * int(grade2)
        if self.p2button2.get():
            mult2 = 1.02
            grade2weighted = mult2 * int(grade2)
        if self.p2button3.get():
            mult2 = 1.06
            grade2weighted = mult2 * int(grade2)
        if self.p2button4.get():
            mult2 = 1.09
            grade2weighted = mult2 * int(grade2)
        
                
                
    #P3 Multiplier
    def updatemult3(self):
        ''' Multiple P2 Entry by check box selected
        '''
        grade3 = self.p3entry.get()
        global grade3weighted
        grade3weighted = None
        mult3 = 1
        
        if self.p3button1.get():
            mult3 = 1
            grade3weighted = mult3 * int(grade3)
        if self.p3button2.get():
            mult3 = 1.02
            grade3weighted = mult3 * int(grade3)
        if self.p3button3.get():
            mult3 = 1.06
            grade3weighted = mult3 * int(grade3)
        if self.p3button4.get():
            mult3 = 1.09
            grade3weighted = mult3 * int(grade3)
            
       
                 
    #P4 Multiplier
    def updatemult4(self):
        ''' Multiple P4 Entry by check box selected
        '''
        grade4 = self.p4entry.get()
        global grade4weighted
        grade4weighted = None
        mult4 = 1
        
        if self.p4button1.get():
            mult4 = 1
            grade4weighted = mult4 * int(grade4)
        if self.p4button2.get():
            mult4 = 1.02
            grade4weighted = mult4 * int(grade4)
        if self.p4button3.get():
            mult4 = 1.06
            grade4weighted = mult4 * int(grade4)
        if self.p4button4.get():
            mult4 = 1.09
            grade4weighted = mult4 * int(grade4)    
            
            
            
    #P5 Multiplier
    def updatemult5(self):
        ''' Multiple P5 Entry by check box selected
        '''
        grade5 = self.p5entry.get()
        global grade5weighted
        grade5weighted = None
        mult5 = 1
        
        if self.p5button1.get():
            mult5 = 1
            grade5weighted = mult5 * int(grade5)
        if self.p5button2.get():
            mult5 = 1.02
            grade5weighted = mult5 * int(grade5)
        if self.p5button3.get():
            mult5 = 1.06
            grade5weighted = mult5 * int(grade5)
        if self.p5button4.get():
            mult5 = 1.09
            grade5weighted = mult5 * int(grade5)
            
            
            
    #P6 Multiplier
    def updatemult6(self):
        ''' Multiple P6 Entry by check box selected
        '''
        grade6 = self.p6entry.get()
        global grade6weighted
        grade6weighted = None
        mult6 = 1
        
        if self.p6button1.get():
            mult6 = 1
            grade6weighted = mult6 * int(grade6)
        if self.p6button2.get():
            mult6 = 1.02
            grade6weighted = mult6 * int(grade6)
        if self.p6button3.get():
            mult6 = 1.06
            grade6weighted = mult6 * int(grade6)
        if self.p6button4.get():
            mult6 = 1.09
            grade6weighted = mult6 * int(grade6)



    #P7 Multiplier
    def updatemult7(self):
        ''' Multiple P7 Entry by check box selected
        '''
        grade7 = self.p7entry.get()
        global grade7weighted
        grade7weighted = None
        mult7 = 1
        
        if self.p7button1.get():
            mult7 = 1
            grade7weighted = mult7 * int(grade7)
        if self.p7button2.get():
            mult7 = 1.02
            grade7weighted = mult7 * int(grade7)
        if self.p7button3.get():
            mult7 = 1.06
            grade7weighted = mult7 * int(grade7)
        if self.p7button4.get():
            mult7 = 1.09
            grade7weighted = mult7 * int(grade7) 
    
    
    
    #P8 Multiplier
    def updatemult8(self):
        ''' Multiple P8 Entry by check box selected
        '''
        grade8 = self.p8entry.get()
        global grade8weighted
        grade8weighted = None
        mult8 = 1
        
        if self.p8button1.get():
            mult8 = 1
            grade8weighted = mult8 * int(grade8)
        if self.p8button2.get():
            mult8 = 1.02
            grade8weighted = mult8 * int(grade8)
        if self.p8button3.get():
            mult8 = 1.06
            grade8weighted = mult8 * int(grade8)
        if self.p8button4.get():
            mult8 = 1.09
            grade8weighted = mult8 * int(grade8)  
                
                
                                
    #GPA Calculation
    def calc(self):
        ''' The Actual GPA Calculcation
        '''
        total = grade1weighted + grade2weighted + grade3weighted + grade4weighted + grade5weighted + grade6weighted + grade7weighted + grade8weighted
        gpa = total / 8
        gpa4pt = gpa / 25
        self.result.delete(0.0, END)
        self.result.insert(0.0, gpa)
    
    
        
root = Tk()
root.title("VTHS Basic GPA Calculator")

app = Application(root)

root.mainloop()