# lop
DNT

<div align="center">

```
██████╗ ███╗   ██╗████████╗    ██╗    ██╗███████╗██████╗ 
██╔══██╗████╗  ██║╚══██╔══╝    ██║    ██║██╔════╝██╔══██╗
██║  ██║██╔██╗ ██║   ██║       ██║ █╗ ██║█████╗  ██████╔╝
██║  ██║██║╚██╗██║   ██║       ██║███╗██║██╔══╝  ██╔══██╗
██████╔╝██║ ╚████║   ██║       ╚███╔███╔╝███████╗██████╔╝
╚═════╝ ╚═╝  ╚═══╝   ╚═╝        ╚══╝╚══╝ ╚══════╝╚═════╝ 
```

# 🌐 MyWeb — Python Flask App

> **Website hiện đại, nhanh chóng, dễ mở rộng — được xây dựng bằng Python & Flask**

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Railway](https://img.shields.io/badge/Deploy-Railway-0B0D0E?style=for-the-badge&logo=railway&logoColor=white)](https://railway.app)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Live%20🟢-brightgreen?style=for-the-badge)]()

<br/>

[🚀 Demo Live](#) · [🐛 Báo lỗi](../../issues) · [✨ Yêu cầu tính năng](../../issues)

</div>

-----

## ✨ Tính năng

|Tính năng       |Mô tả                                            |
|----------------|-------------------------------------------------|
|🏠 **Trang chủ** |Giao diện đẹp với hero section và cards          |
|👤 **Giới thiệu**|Thông tin về dự án và công nghệ sử dụng          |
|📬 **Liên hệ**   |Form gửi tin nhắn với AJAX (không reload trang)  |
|📱 **Responsive**|Tương thích mọi thiết bị: desktop, tablet, mobile|
|⚡ **Nhanh**     |Tối ưu hiệu suất với Flask backend               |

-----

## 🗂️ Cấu trúc project

```
myproject/
│
├── 📄 app.py                  # File chính — Flask app
├── 📄 requirements.txt        # Danh sách thư viện
├── 📄 Procfile                # Cấu hình deploy Railway
├── 📄 .gitignore              # Loại bỏ file rác
│
└── 📁 templates/
    ├── 🌐 base.html           # Layout chung (navbar, footer)
    ├── 🏠 index.html          # Trang chủ
    ├── 👤 about.html          # Giới thiệu
    └── 📬 contact.html        # Liên hệ
```

-----

## ⚙️ Cài đặt & Chạy local

### Yêu cầu

- Python **3.11+**
- pip

### Các bước

```bash
# 1️⃣ Clone repo
git clone https://github.com/username/myproject.git
cd myproject

# 2️⃣ Tạo môi trường ảo
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# 3️⃣ Cài thư viện
pip install -r requirements.txt

# 4️⃣ Chạy app
python app.py
```

Mở trình duyệt và vào: **http://localhost:5000** 🎉

-----

## 🚀 Deploy lên Railway

### Bước 1 — Đảm bảo có đủ 3 file này

```
✅ app.py
✅ requirements.txt
✅ Procfile  →  nội dung: web: gunicorn app:app
```

### Bước 2 — Push lên GitHub

```bash
git add .
git commit -m "🚀 deploy: ready for Railway"
git push origin main
```

### Bước 3 — Deploy

1. Vào [railway.app](https://railway.app) → **New Project**
1. Chọn **Deploy from GitHub repo**
1. Chọn repo → Railway tự động build & deploy
1. Vào **Settings → Networking → Generate Domain** để lấy link public

-----

## 🛠️ Công nghệ sử dụng

<div align="center">

|Layer              |Công nghệ             |
|-------------------|----------------------|
|**Backend**        |Python 3.11, Flask 3.0|
|**Template**       |Jinja2, HTML5         |
|**Styling**        |CSS3 (Flexbox, Grid)  |
|**Server**         |Gunicorn              |
|**Hosting**        |Railway.app           |
|**Version Control**|Git, GitHub           |

</div>

-----

## 🐛 Lỗi thường gặp & cách fix

<details>
<summary><b>❌ Lỗi 502/504 sau khi deploy</b></summary>

```python
# ❌ Sai
app.run(debug=True)

# ✅ Đúng
import os
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
```

</details>

<details>
<summary><b>❌ ModuleNotFoundError</b></summary>

```bash
# Xuất lại requirements.txt đúng cách
pip freeze > requirements.txt
```

</details>

<details>
<summary><b>❌ TemplateNotFound</b></summary>

```python
# ❌ Sai
app = Flask("app")

# ✅ Đúng
app = Flask(__name__)
```

</details>

<details>
<summary><b>❌ Build Failed trên Railway</b></summary>

Kiểm tra `Procfile` — phải đặt đúng tên, không có đuôi file, nội dung:

```
web: gunicorn app:app
```

</details>

-----

## 📝 License

Dự án này sử dụng giấy phép **MIT** — xem file <LICENSE> để biết thêm chi tiết.

-----

<div align="center">

Made with ❤️ by **[HKHQN](https://github.com/HKHQN)**

⭐ Nếu project hữu ích, hãy cho một **Star** nhé!

</div>
