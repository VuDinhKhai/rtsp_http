#brew install ffmpeg
import cv2
import subprocess as sp
import numpy
rtsp_server = 'rtsp://192.168.1.126:8554/mystream'
# def RTSPServer():
#Chạy chương trình ffmpeg 
def rtsp():
    command = ['ffmpeg',
                '-re',#doc dau vao toc do khung hinh
                '-s','1280x720', #Kich thuoc khung hinh
                '-framerate', '0', 
                '-r', str(25),  # rtsp fps (from input server)
                '-f','gdigrab', #dinh dang cho title
                '-i', 'title=X-System',#input du lieu
                # You can change ffmpeg parameter after this item.
                '-pix_fmt', 'yuv420p',# dinh dang pixel ho tro
                '-r', '25',  # output fps
                '-g', '12', #kich thuoc nhom anh(mac dinh)
                '-c:v', 'libx264', #ma hoa luong video bang libx264
                #-aspect 16:9 thay đổi ti le khung hinh
                '-b:v', '2M',# tốc độ bit của video 
                '-bufsize', '64M',#kích thước bộ đệm
                '-maxrate', "4M",# Đặt dung sai tốc độ bit tối đa
                '-preset', 'veryfast',#toc do ma hoa
                '-rtsp_transport', 'tcp',
                '-segment_times', '5',
                '-f', 'rtsp',# xuất video ra rtsp
                rtsp_server]

    process = sp.Popen(command, stdin=sp.PIPE)
