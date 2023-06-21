
from RTSPServer import*
from HTTPServer import*
from tkinter import *  
from PIL import ImageTk, Image
import threading

win=Tk()
win.title('Project1') # tên UD
win.geometry('500x500') #Kích thước 
win.resizable(width=False,height=False)
#nền
Load= Image.open(r'C:\Users\dungs\Desktop\project\anhnen.jpg')
render= ImageTk.PhotoImage(Load)
img=Label(win,image=render)
img.place(x=0,y=0) 

#chạy hàm:
t1 = threading.Thread(target=stream_html, )
t2 = threading.Thread(target=rtsp, )
def HTTP():
    thongbao=Label(win,text=' Chạy chương trình HTTPSever ',padx=30,pady=8,font=('Arial',15,'bold'),fg='#FFFFFF',bg='#303030')
    thongbao.place(x=50,y=100)
    try:    
        t1.start()
        t1.join()
    except:
        print("error")
def RTSP():
    thongbao=Label(win,text=' Chạy chương trình RTSPSever ',padx=30,pady=8,font=('Arial',15,'bold'),fg='#FFFFFF',bg='#303030')
    thongbao.place(x=50,y=100)
    try:
        t2.start()
        t2.join()
    except:
        print("error")
but1 = Button(win,text='HTTP Server',font=('Arial',13,'bold'),fg='#FFFFFF',bg='#303030',padx=30,pady=8,command=HTTP)
but1.place(x=25,y=300)
but2 = Button(win,text='RTSP Server',font=('Arial',13,'bold'),fg='#FFFFFF',bg='#303030',padx=30,pady=8,command=RTSP)
but2.place(x=300,y=300)

win.mainloop()