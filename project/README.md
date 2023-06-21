Bước 1: Cài đặt thư viện.
-	Đối với máy Server: Sau khi đã cài Anaconda, tại Anaconda Prompt, gõ lệnh:
cd Desktop/project   		# đưa đường dẫn tới folder project 
pip install -r requirement.txt
-	Đối với máy Client: Tải phần mềm Mission Planner Hoặc QgroundControl (Trạm điều khiển mặt đất) .
Bước 2: Kiểm tra địa chỉ IP trên máy Server.
Bước 2.1: Nhấn tổ hợp phím “Windows + R” trên bàn phím để hiện ra hộp thoại Run.
Bước 2.2: Gõ “cmd” rồi nhấn ok.
Bước 2.3: Nhập “ipconfig” rồi ấn Enter.

Bước 2.4: Ghi lại địa chỉ IPv4.
Bước 3: Mở folder đã tải xuống bằng Visual Studio Code với môi trường anaconda.
-	Đối với máy Server:
Bước 3.1: Nhập lệnh “code” trong cửa sổ anaconda Prompt.
Bước 3.2: Để mở folder “Project” trên VS code chọn “File”-> “Open folder” rồi tìm tới folder “Project” ->“Select folder”.
-	Đối với máy Client: 
Ta thực hiện mở ứng dụng trạm điều khiển mặt đất Mission Planer đối với giao thức HTTP và QgroundControl với giao thức RTSP.
Bước 4: Chạy trương trình .
-	Đối với máy Server: 
 	Bật phần mềm X- Plane 11 
Chạy trương trình: 
Tại cửa sổ VS code, Chọn “Terminal” -> “New Terminal”.
Nhập lệnh sau trên terminal:
python Project1.py
-	Đối với máy Client: Lưu địa chỉ trang web url “ Localhost:8000/stream.jmpeg “ thay vào chương trình Mission Planner đối vơi dự án HTTP 
-	Lưu địa chỉ URL: “ rtsp://localhost:8554/mystream. ” thay vào chương trình QgroundControl đối với dự án RTSP.


Lưu ý: Phần ‘localhost’ ở máy Server: thay bằng Ipv4 ở bước 2.4.
2.2	Kết quả chạy và giải thích code:
2.2.1: Giải thích code giao thức HTTP: 
- Hàm lấy hình ảnh từ môi trường X - Plane 11 :
. Thêm thư viện lấy hình ảnh: 
. Tạo HTTP Server:
. Chạy hàm: Tạo luồng Server gửi ảnh lên địa chỉ  url : 
 “ Localhost/8000/stream.mjpeg ”.
2.2.2	Giải thích code giao thức RTSP:
-	Tại Server : Chạy chương trình tạo luồng RTSP Server: 
. Thư viện cần dùng cho bài toán:  
. Thêm địa chỉ RTSP Server: 
. Code lấy hình ảnh từ môi trường X- plane 11: 
Định dạng hình ảnh và Đẩy hình ảnh lên trên luồng RTSP Server.
Hàm chạy: Dùng ffmpeg chạy và đẩy các giá trị truyền hình ảnh vào luồng.
HÌNH  2 0 24: HÀM CHẠY CHƯƠNG TRÌNH HIỂN THỊ HÌNH ẢNH LÊN RTSP SERVER.
2.2.3	Chạy phần mềm gửi hình ảnh:
A,Giải thích code:
- Tạo ứng dụng trên windows bằng tkinter python và thư viện cần dùng :
- Chạy hàm: Tạo 2 luồng chạy HTTP và RTSP, Tạo 2 nút nhấn để chọn Giao thức HTTP hoặc Giao thức RTSP.
HÌNH  2-0 26: HIỂN THỊ NÚT NHẤN ĐIỀU CHỈNH CHỌN GIAO THỨC 
