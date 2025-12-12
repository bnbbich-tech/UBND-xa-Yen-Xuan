# UBND xã Yên Xuân - Hệ Thống Quản Lý Quầy Tiếp Nhận

Hệ thống quản lý quầy tiếp nhận dịch vụ công tải UBND xã Yên Xuân, xây dựng bằng Flask Python.

## Giới Thiệu

Hiện tại ứng dụng chạy trên Replit. Dự án này cung cấp hướng dẫn để sáo chép và triển khai trên các nền tảng khác như **Render**, **Railway** hay **VPS công cộng**.

## Các Thư Mục

```
UBND-xa-Yen-Xuan/
├── main.py                 # File chính Flask
├── requirements.txt        # Dependencies Python
├── templates/
│   └── index.html         # Trang gớo diện chính
└── static/                # (chưa thêm) CSS, JS, hình ảnh
```

## Yêu Cầu

- Python >= 3.11
- Flask >= 3.1.1
- pip hoặc Poetry

## Cách Thực Deploy

### 1. Cách 1: Deploy trên **Render**

1. Đăng nhập/Đăng ký tại [render.com](https://render.com)
2. Click **New** → **Web Service**
3. Kết nối GitHub: Chọn repository này
4. Cấu hình:
   - **Environment**: Python 3.11
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn main:app`
5. Click **Deploy**

**URL Sẽ Nhận**: `https://ubnd-xa-yen-xuan.onrender.com`

### 2. Cách 2: Deploy trên **Railway**

1. Đăng ký/đăng nhập tại [railway.app](https://railway.app)
2. Kết nối GitHub account
3. Tạo **New Project** từ repository này
4. Railway sẽ tự động detect `requirements.txt` và deploy

### 3. Cách 3: Chạy trên Máy Tính/VPS

```bash
# Clone repository
git clone https://github.com/bnbbich-tech/UBND-xa-Yen-Xuan.git
cd UBND-xa-Yen-Xuan

# Tạo virtual environment
python -m venv venv
source venv/bin/activate  # trên Linux/Mac
venv\Scripts\activate     # trên Windows

# Cài đặt dependencies
pip install -r requirements.txt

# Chạy ứng dụng
python main.py
```

Sắp năm trên: http://localhost:5000

## Noti của Téch Nhân

- App hiện tại chấp nhận lược lưu trữ trên máy chủ
- Bửa sửa: cần thêm static files (CSS, JS, hình ảnh) vào thư mục `static/`
- Admin page chưa có xác thực

## Hàng Links Hắu ích

- **Replit Original**: https://replit.com/@bnbbich/UBND-xa-Yen-Xuan
- **Render Docs**: https://render.com/docs
- **Railway Docs**: https://docs.railway.app

---

**Cuội cùng cập nhật**: 12/12/2025
