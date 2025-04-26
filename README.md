# Bài Tập Lớn: Trò Chơi Breakout với Tính Năng Mạng Sống
## Thông Tin Dự Án

- Tên dự án: Breakout Game
- Môn học: Lập trình Python 2
- Sinh viên thực hiện: 
    - Phạm Thị Phượng - 2221050063
    - Đinh Thị Thảo Thư - 2221050714
    - Trần Minh Hằng - 2221050777
- Giảng viên hướng dẫn: Nguyễn Văn Thắng

## Mô Tả Dự Án
Dự án này là một trò chơi Breakout cổ điển được phát triển bằng Python sử dụng thư viện Pygame. Người chơi điều khiển một thanh trượt (paddle) để đánh một quả bóng phá các viên gạch (bricks) trên màn hình. Người chơi có 3 cơ hội trước khi trò chơi kết thúc, làm tăng tính hấp dẫn và giảm độ khó cho người mới.
### Mục Tiêu

- Xây dựng một trò chơi 2D hoàn chỉnh với giao diện thân thiện và lối chơi mượt mà.
- Tích hợp tính năng mạng sống để cải thiện trải nghiệm người chơi.
- Áp dụng kiến thức lập trình Python và thư viện Pygame trong phát triển game.
- Đảm bảo mã nguồn rõ ràng, dễ bảo trì và tuân theo các tiêu chuẩn lập trình.


### Thư viện:
- Pygame `pip install pygame`


### Cài Đặt
1. Cài đặt Python

- Tải và cài đặt Python từ python.org.
- Đảm bảo thêm Python vào biến môi trường PATH trong quá trình cài đặt.

2. Cài đặt Pygame
- Mở terminal hoặc command prompt và chạy lệnh: `pip install pygame`



3. Tải mã nguồn

- Tải mã nguồn từ kho lưu trữ hoặc sao chép tệp breakout_with_lives.py vào thư mục làm việc.
- Nếu sử dụng Git: `git clone <URL-kho-lưu-trữ>`
`cd <thư-mục-dự-án>`



### Hướng Dẫn Chạy Game

- Đảm bảo tệp breakout_game.py nằm trong thư mục làm việc.
- Mở terminal hoặc command prompt, di chuyển đến thư mục chứa tệp: `cd <đường-dẫn-thư-mục>`


- Chạy game:`python breakout_game.py`


--> Cửa sổ game sẽ xuất hiện, sẵn sàng để chơi.

## Hướng Dẫn Chơi

- Mục tiêu: Phá hết tất cả các viên gạch bằng cách dùng thanh trượt để đánh bóng.
- Cách điều khiển:
- Phím mũi tên trái: Di chuyển thanh trượt sang trái.
- Phím mũi tên phải: Di chuyển thanh trượt sang phải.
- Phím R: Khởi động lại trò chơi khi Game Over.


### Cơ chế mạng sống:
- Người chơi có 3 mạng sống.
- Mỗi lần bóng rơi xuống dưới màn hình, mất 1 mạng.
- Nếu còn mạng, bóng và thanh trượt được đặt lại.
- Khi hết mạng, màn hình Game Over xuất hiện.



## Tính Năng Chính

Gameplay cổ điển:
- Điều khiển thanh trượt để đánh bóng phá gạch.
- Ghi điểm (10 điểm mỗi gạch).
- Kết thúc trò chơi nếu hết mạng sống.


Tính năng mạng sống:
- Bắt đầu với 3 mạng.
- Mất 1 mạng khi bóng rơi.
- Hiển thị số mạng ở góc trên bên phải.
- Reset mạng về 3 khi khởi động lại.


Giao diện trực quan:
- Màu sắc sinh động: gạch đỏ, thanh trượt xanh, bóng vàng.
- Hiển thị điểm số (góc trên bên trái) và mạng sống (góc trên bên phải).


Hiệu suất:
- Chạy mượt mà ở 60 FPS.
- Xử lý va chạm chính xác giữa bóng, thanh trượt, gạch và tường.



Cấu Trúc Mã Nguồn
- Tệp chính: breakout_game.py
- Các thành phần chính:

Khởi tạo:
- Thiết lập Pygame, cửa sổ game (600x500 pixel).
- Định nghĩa màu sắc, phông chữ, và các đối tượng (paddle, ball, bricks).
- Khởi tạo biến score và lives.


Vòng lặp game:
- Xử lý sự kiện (đóng cửa sổ, nhấn phím).
- Cập nhật vị trí bóng và thanh trượt.
- Kiểm tra va chạm (tường, paddle, bricks).
- Xử lý logic mạng sống khi bóng rơi.


Vẽ đồ họa:
- Vẽ paddle, bóng, gạch, điểm số, và số mạng.
- Cập nhật màn hình mỗi khung hình.


Game Over và Reset:
- Hiển thị màn hình Game Over khi hết mạng.
- Cho phép reset game bằng phím R, đặt lại tất cả trạng thái.



Các biến chính:

- WIDTH, HEIGHT: Kích thước cửa sổ (600x500).
- paddle: Đối tượng pygame.Rect cho thanh trượt.
- ball: Đối tượng pygame.Rect cho bóng.
- bricks: Danh sách các viên gạch (pygame.Rect).
- score: Điểm số người chơi.
- lives: Số mạng sống (mặc định 3).


## Hạn Chế và Hướng Phát Triển
Hạn chế

Thiếu âm thanh và hiệu ứng trực quan (như lấp lánh khi phá gạch).
Chưa có menu chính hoặc màn hình chiến thắng.
Vật lý bóng đơn giản (bật lại cố định, không phụ thuộc góc va chạm).

Hướng phát triển

Thêm âm thanh cho va chạm và sự kiện mất mạng.
Tích hợp các item rơi (ví dụ: kéo dài paddle, tăng mạng).
Thêm hiệu ứng lấp lánh hoặc vòng sáng cho bóng.
Xây dựng menu khởi động và hệ thống cấp độ.
Lưu điểm cao nhất vào tệp.

Hướng Dẫn Đóng Góp

Báo lỗi: Nếu phát hiện lỗi, tạo issue trên kho lưu trữ (nếu có) hoặc liên hệ trực tiếp.
Đề xuất tính năng: Gửi ý tưởng qua email hoặc issue.
Gửi pull request:
Fork kho lưu trữ.
Tạo branch mới (git checkout -b feature/ten-tinh-nang).
Commit thay đổi (git commit -m "Thêm tính năng X").
Push và tạo pull request.



## Tài Liệu Tham Khảo

- Tài liệu Pygame: pygame.org/docs
- Hướng dẫn Python: python.org
- Tài liệu môn học: [Thêm tài liệu môn học nếu có]

