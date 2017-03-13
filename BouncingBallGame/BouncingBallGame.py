#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# ---------------- READ ME ---------------------------------------------
# This Script is Created Only For Practise And Educational Purpose Only
# This is an Example Of Tkinter Canvas Graphics
# This Script Is Created For http://bitforestinfo.blogspot.in
# This Script is Written By
#
#
##################################################
######## Please Don't Remove Author Name #########
############### Thanks ###########################
##################################################
#
#
__author__='''

######################################################
                By S.S.B Group                          
######################################################

    Suraj Singh
    Admin
    S.S.B Group
    surajsinghbisht054@gmail.com
    http://bitforestinfo.blogspot.in/

    Note: We Feel Proud To Be Indian
######################################################
'''
print __author__
# ----------- Importing Module --------------------------
try:
    import Tkinter, random, time, sys
except:
    import tkinter as Tkinter,sys ,random, time

# -------- Gaming Display -----------------------------
class GameDisplay:
    def __init__(self, canvas):
        self.canvas=canvas
        self.widthlimit=canvas.winfo_screenwidth()
        self.heightlimit=canvas.winfo_screenheight()
        y2=canvas.winfo_screenheight()-70
        y1=y2-15
        self.bat=Tkinter.Canvas.create_rectangle(canvas, 0, y1,200, y2, fill='steelblue')
        self.ball=Tkinter.Canvas.create_oval(canvas, 0, 0,50,50, fill='lightgreen')
        self.xvelocity=2
        self.yvelocity=2
        
    def update(self, event=None):
        x1,y1,x2,y2=self.canvas.coords(self.ball)
        a,b,c,d=self.canvas.coords(self.bat)
        k=len(self.canvas.find_overlapping(a,b,c,d))
        if x1<=0:
            self.xvelocity=2
            self.canvas.move(self.ball,self.xvelocity,0)
            pass
        elif y2>=self.heightlimit:
            x=self.canvas.winfo_screenwidth()/2
            y=self.canvas.winfo_screenheight()/2
            self.canvas.create_text(x,y, text='Game Over', font=('arial 50 bold'), fill='red')
            self.canvas.master.update()
            self.canvas.master.update_idletasks()
            time.sleep(2)
            self.canvas.master.destroy()
            sys.exit(0)
            pass
        elif x2>=self.widthlimit:
            self.xvelocity=-2
            self.canvas.move(self.ball,self.xvelocity,0)
        elif y1<=0:
            self.yvelocity=2
            self.canvas.move(self.ball, 0, self.yvelocity)
        elif k==2:
            self.yvelocity=-2
            self.canvas.move(self.ball, 0, self.yvelocity)            
        else:
            self.canvas.move(self.ball, self.xvelocity, self.yvelocity)

        pass
        
    def update_bat(self, event=None):
        direction=event.keysym
        x1,x2,y1,y2=self.canvas.coords(self.bat)
        if y1>self.widthlimit:
            if direction=='Left':
                self.canvas.move(self.bat, -20,0)
                pass
        elif x1<0:
            if direction=='Right':
                self.canvas.move(self.bat, 20,0)
                pass
            
        elif direction=='Right':
            self.canvas.move(self.bat, 20,0)
        elif direction=='Left':
            self.canvas.move(self.bat, -20,0)
        else:
            pass        


# --------- Main Window Graphic  ----------------------
class main:
    def __init__(self):
        root=Tkinter.Tk(className='Bouncing Game')
        w, h=root.winfo_screenwidth(), root.winfo_screenheight()
        canvas=Tkinter.Canvas(root, background='grey', width=w, height=h)
        canvas.pack()
        game=GameDisplay(canvas)
        for seq in ['<Any-KeyPress>']:
            root.bind_all(seq,game.update_bat)
        # Creating Transpareny
        root.wait_visibility(canvas)
        root.wm_attributes('-alpha',0.7)
        # Custom Main loop
        while True:
            time.sleep(0.01)
            game.update()
            root.update()
            root.update_idletasks()

# ======= Trigger ==============
if __name__=='__main__':
    main()
