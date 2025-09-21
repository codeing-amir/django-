# ✨ README — پروژه‌ی Django (Backend)

**نام پروژه:** rdm-backend (مثال)

**هدف:** این مخزن یک بک‌اند کامل با Django آماده برای استفاده در پروژه‌های وب است. شامل مدل‌ها، API REST، احراز هویت، مستندات، تنظیمات محیطی، داکر، و نکات مربوط به استقرار است.

---

## 🔎 نمای کلی

این پروژه برای سریع‌سازی توسعه‌ی بک‌اند وب با استفاده از Django و Django REST Framework طراحی شده است. هدف فراهم کردن ساختار قابل توسعه، امن و خوانا برای اپلیکیشن‌هایی مانند فروشگاه، سامانه مدیریت محتوا، یا سامانه‌های سرویس‌دهی است.

### ویژگی‌ها

* معماری استاندارد Django (apps جداگانه)
* API REST با Django REST Framework
* احراز هویت JWT (یا Token) و مدیریت کاربران
* صفحه ادمین Django فعال
* تنظیمات چندمحیطی (development / production)
* پیکربندی با فایل `.env`
* Docker + Docker Compose برای توسعه و استقرار محلی
* فایل نمونه برای migrations، fixtures و نمونه‌ی داده
* تست‌های واحد و انتها به انتها (pytest یا Django test)
* مستندات ساده API (Swagger / ReDoc قابل اضافه شدن)

---

## 🧩 ساختار پیشنهادی پروژه

```
rdm-backend/
├── manage.py
├── README.md
├── .env.example
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── rdm_project/                # تنظیمات اصلی پروژه
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── users/                  # احراز هویت و پروفایل
│   ├── core/                   # مدل‌ها و منطق اصلی
│   └── api/                    # serializer ها و viewset ها
├── tests/
└── docs/
```

---

## ⚙️ پیش‌نیازها

* Python 3.10+ (یا 3.9+)
* pip
* virtualenv (یا venv)
* Docker (اختیاری برای توسعه/استقرار)

---

## 🚀 راه‌اندازی محلی (بدون Docker)

1. پروژه را کلون کنید:

```bash
git clone <repository-url> rdm-backend
cd rdm-backend
```

2. محیط مجازی بسازید و فعال کنید:

```bash
python -m venv .venv
source .venv/bin/activate    # macOS / Linux
.venv\Scripts\activate      # Windows
```

3. وابستگی‌ها را نصب کنید:

```bash
pip install -r requirements.txt
```

4. فایل نمونه `.env.example` را کپی و مقداردهی کنید:

```bash
cp .env.example .env
# سپس مقادیر DATABASE_URL, SECRET_KEY, DEBUG و دیگران را ویرایش کنید
```

5. مهاجرت‌ها را اعمال کنید و سوپر یوزر بسازید:

```bash
python manage.py migrate
python manage.py createsuperuser
```

6. سرور توسعه را اجرا کنید:

```bash
python manage.py runserver
```

اکنون اپ روی `http://127.0.0.1:8000/` در دسترس است.

---

## 🐳 راه‌اندازی با Docker (توسعه)

فایل `docker-compose.yml` شامل سرویس‌ها: `web` (Django), `db` (Postgres), `redis` (اختیاری), `nginx` (اختیاری) است.

1. ساخت و اجرای کانتینرها:

```bash
docker-compose up --build
```

2. اجرای مهاجرت‌ها داخل کانتینر:

```bash
docker-compose exec web python manage.py migrate
```

3. ساخت سوپر یوزر:

```bash
docker-compose exec web python manage.py createsuperuser
```

---

## 🔐 پیکربندی محیطی (`.env`)

نمونه متغیرها در `.env.example`:

```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgres://user:password@db:5432/rdm_db
ALLOWED_HOSTS=localhost,127.0.0.1
DJANGO_SETTINGS_MODULE=rdm_project.settings
```

> **نکته امنیتی:** `SECRET_KEY` را در مخزن قرار ندهید؛ در محیط production از متغیر محیطی امن استفاده کنید.

---

## 🗂️ مدل‌ها و API (نمونه)

### مدل‌های نمونه

* `User` (گسترش‌یافته از `AbstractUser` یا `AbstractBaseUser`) — مدیریت کاربران و پروفایل
* `Product` / `Article` / `Order` — نمونه مدل‌های کسب‌وکار

### نمونه endpoints

* `POST /api/auth/login/` — ورود و دریافت JWT
* `POST /api/auth/register/` — ثبت‌نام کاربر
* `GET /api/users/` — لیست کاربران (admin)
* `GET /api/products/` — لیست محصولات
* `POST /api/products/` — ایجاد محصول (auth)

(جزئیات بیشتر در فایل `docs/api.md` یا از طریق Swagger فراهم شود.)

---

## ✅ تست‌ها

* از `pytest` یا `python manage.py test` استفاده کنید.
* مثال اجرای pytest:

```bash
pytest --maxfail=1 -q
```

---

## 📦 مدیریت وابستگی

فایل `requirements.txt` شامل موارد پایه است مثل:

```
Django>=4.2
djangorestframework
psycopg2-binary
python-dotenv
gunicorn
djangorestframework-simplejwt
```

---

## ⚙️ استقرار (نمونه: Linux + Gunicorn + Nginx)

1. در سرور production از `DEBUG=False` استفاده کنید و `ALLOWED_HOSTS` را مشخص کنید.
2. از یک دیتابیس PostgreSQL یا managed DB استفاده کنید.
3. یک سرویس systemd برای Gunicorn تعریف کنید و آن را پشت Nginx قرار دهید.
4. اجرای دستورالعمل‌های امنیتی: HTTPS (Let's Encrypt)، مدیریت فایل‌های استاتیک با `collectstatic`، پیکربندی CORS اگر نیاز است.

نمونه دستورات:

```bash
python manage.py collectstatic --noinput
gunicorn rdm_project.wsgi:application --bind 0.0.0.0:8000
```

---

## 🧰 ابزار پیشنهادی برای توسعه

* `django-debug-toolbar` برای دیباگ
* `drf-yasg` یا `drf-spectacular` برای مستندسازی API
* `celery` + `redis` برای کارهای پس‌زمینه
* `whitenoise` برای سرو کردن static در production (در صورت ساده)

---

## 🤝 مشارکت

اگر علاقه‌مند به مشارکت هستید:

1. فورک کنید
2. شاخه feature بسازید
3. PR بفرستید

لطفاً از قوانین کدنویسی و فرمت commit مشخص استفاده کنید (مثلاً Conventional Commits).

---

## 📝 نمونهٔ دستورات مفید

```bash
# اجرای سرور توسعه
python manage.py runserver

# ساخت و اعمال مهاجرت
python manage.py makemigrations
python manage.py migrate

# نصب وابستگی جدید
pip install <package>
pip freeze > requirements.txt
```

---

## 📄 لایسنس

این پروژه با لایسنس MIT منتشر می‌شود — در صورت نیاز لایسنس مناسب را قرار دهید.

---

