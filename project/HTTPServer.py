import logging
import time
from http import server
from http.server import HTTPServer
from threading import Condition,Thread
import simplejpeg
from windowcapture_fix_ratio import WindowCapture

#địa chỉ
PORT = 8000
HOST = '192.168.1.126'
mjpeg_abort = False
mjpeg_frame = None
mjpeg_condition = Condition()


#Mã hóa hình anh
def mjpeg_encode():
    global mjpeg_frame
    while not mjpeg_abort:
        try:
            wincap = WindowCapture("X-System")#Khai báo hàm lấy hình ảnh
            # img = cv2.imread('BGR1.jpg')
            #rgb = cv2.rotate(rgb, cv2.ROTATE_180)
            # vid = cv2.VideoCapture('emyeu.mp4')
            # vid = cv2.VideoCapture(img)
            while(True):

                # ret, frame = vid.read()
                frame =wincap.get_screenshot()# Lấy hình ảnh
                buf = simplejpeg.encode_jpeg(frame, quality=50, colorspace='BGR', colorsubsampling='420') 
                #Ma hoa hinh anh duoi dang chuoi jpeg :
                # chat luong: 50 (1-100),khong gian mau BGR, He so lay mau 420
                print("Data transmit: ", len(buf))#chieu dai chuoi jpeg
                with mjpeg_condition:
                    mjpeg_frame = buf
                    mjpeg_condition.notify_all()
        except:   
            print("Need to do some clean up")
#tạo Http Server
class projectHTTP(server.BaseHTTPRequestHandler): #BaseHTTPRequestHandler xử lý yêu cầu http
    # yêu cầu gửi lên http
    def do_GET(self):
        if self.path == '/': #kiểm tra yêu cầu
            self.send_response(301)
            self.send_header(HOST, '/stream.mjpg')
            self.end_headers()  
        elif self.path == '/stream.mjpg':
            self.send_response(200) #phàn hồi khi truy cập thành công
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                while True:
                    frame = mjpeg_frame
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(frame)) #len trả về độ dài kí tự
                    self.end_headers()
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
            except Exception as e:
                logging.warning(
                    'Removed streaming client %s: %s',
                    self.client_address, str(e))   
mjpeg_thread = Thread(target=mjpeg_encode, daemon=True)# chạy luông mã hóa hình ảnh
mjpeg_thread.start()

def stream_html():
    address = (HOST, PORT) # dia chi luong
    server = HTTPServer(address, projectHTTP)#tao luong 
    print("Stream Connecting.....")
    print("Connecting MAJ GCS")
    print(time.asctime(), "Start Server - %s:%s"%(HOST,PORT))
    server.serve_forever()#chạy luong lien tuc
        

