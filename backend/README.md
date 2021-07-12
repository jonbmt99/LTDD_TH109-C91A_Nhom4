OU book store management website
*******************************************
Website quản lý thư viện, nhà sách của trường Đại học Mở TPHCM, Việt Nam
Mô tả:
    Là 1 chương trình website dùng để quản lý thư viện cũng như thư quán của một trường đại học với các chức năng cơ bản cần có, được xây dựng dựa trên các công nghệ Angular(Front-end), Flask-Python(Back-end), Mysql(Database).
Các chức năng cơ bản: 
    - Quản lý các đối tượng sách, nhân viên, khách hàng, tài khoản, nhà cung cấp, tác giả.....
    - Mượn trả sách của thư viện
    - Thanh toán đơn hàng thông qua nhiều hình thức như paypal, momo...
    - Chăm sóc khách hàng, chatbox, 
    - Upload ảnh với api của Cloudinary
    - Xác thực với JWT
    - Login bằng Google
    - Gửi tin nhắn Telegram
Yêu cầu tiên quyết:
    - Nodejs "https://nodejs.org/en/download/"
    - Angular "https://angular.io/guide/setup-local"
    - Mysql "https://www.mysql.com/downloads/"
    
Hướng dẫn cài đặt: (Theo thứ tự)
    --------------------Database------------------------
    - Tạo 1 database có tên "bookstoredb"
    - Tạo user: 
        username = "root"
        password = "Password123@"
        port  = 3306
        hostname = localhost
    -------------------Backend-------------------------
    - Mở folder /python-flask bằng IDE của Python(Pycharm)
    - Nhập và sử dụng lệnh "pip install -r requirements.txt" để cài đặt môi trường ảo trên máy
    - Cài đặt lại các config trong file config.py cho hợp lý
    - Mở và run file ./once/init_database.py, nhằm khởi tạo các dữ liệu cần thiết cho hệ thống như khởi tạo database, thêm roles, admin....
    - Mở và run file /main.py để chạy chương trình.
    ------------------Front-end-------------------------
    - Mở folder /angular2+
    - Open in terminal, sử dụng lệnh "npm install" để cài đặt các dependencies
    - Nhập và sử dụng lệnh "npm run start" để chạy chương trình trên "localhost:4200"

Hướng dẫn:
    - Tài khoản admin mặc định của của hệ thống:
        username: admin
        password: 123456789
    - Đăng nhập tài khoản tại trang /admin/login để truy cập trang quản lý.
    - Truy cập trang /book-store/home để truy cập trang chủ bán hàng.


