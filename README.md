# 📚 Simple LMS - Docker & Django

## 📌 Deskripsi

Project ini merupakan implementasi **Simple Learning Management System (LMS)** menggunakan **Django** sebagai backend, **PostgreSQL** sebagai database, dan **Docker** untuk containerization.

Project ini dibuat untuk memenuhi tugas *Progress 1: Docker & Django Foundation*.

---

## 🚀 Teknologi yang Digunakan

* Python
* Django
* PostgreSQL
* Docker & Docker Compose
* Gunicorn

---

## 📁 Struktur Project

```
simple-lms/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Cara Menjalankan Project

### 1. Clone Repository

```bash
git clone https://github.com/USERNAME/simple-lms.git
cd simple-lms
```

---

### 2. Setup Environment

Copy file `.env.example` menjadi `.env`

```bash
cp .env.example .env
```

---

### 3. Jalankan Docker

```bash
docker compose up --build
```

---

### 4. Migrasi Database

Buka terminal baru, lalu jalankan:

```bash
docker compose exec web python manage.py migrate
```

---

### 5. Buat Superuser (Admin)

```bash
docker compose exec web python manage.py createsuperuser
```

---

### 6. Akses Aplikasi

* 🌐 Website: http://localhost:8000
* 🔐 Admin: http://localhost:8000/admin

---

## 🗄️ Konfigurasi Database

Project menggunakan PostgreSQL yang dijalankan melalui Docker.

Konfigurasi diambil dari file `.env`:

```
POSTGRES_DB=lms_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

---

## ✅ Fitur yang Berhasil

* Setup Django project
* Integrasi PostgreSQL
* Containerization menggunakan Docker
* Migrasi database berhasil
* Admin panel aktif

---

## 📸 Screenshot 

![tampilan awal django](https://github.com/user-attachments/assets/dc178957-da7f-40a1-9b41-82a6b550988c)

---

## ⚠️ Catatan

* File `.env` tidak disertakan demi keamanan
* Gunakan `.env.example` sebagai referensi

---

## 👨‍💻 Author

Nama: **Adi Priyo**
Project: Simple LMS
Tahun: 2026

---

## 🎯 Kesimpulan

Project ini berhasil membangun fondasi aplikasi berbasis Django menggunakan Docker dan PostgreSQL. Sistem telah berjalan dengan baik dan siap dikembangkan ke tahap berikutnya.

---
