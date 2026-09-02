# Neville Venerdi — Personal Homepage

Personal homepage / online CV berbasis Flask dengan desain editorial, lembut, minimal, dan responsif.

## Menjalankan secara lokal

```bash
python -m venv .venv
```

Windows:

```bash
.venv\\Scripts\\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependency:

```bash
pip install -r requirements.txt
```

Jalankan:

```bash
python app.py
```

Buka: http://127.0.0.1:5000

## Menambahkan foto profil

Taruh foto di:

`static/assets/profile.jpg`

Kemudian pada `templates/index.html`, ganti blok `.portrait-placeholder` dengan:

```html
<img src="{{ url_for('static', filename='assets/profile.jpg') }}" alt="Neville Venerdi">
```

Tambahkan styling `object-fit: cover; width:100%; height:100%;` pada gambar.

## Struktur

```text
neville-personal-homepage/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── main.js
    └── assets/
```


## Project links

URL project dikelola dari `app.py` melalui environment variable agar mudah diganti saat project sudah di-deploy.

Windows PowerShell:

```powershell
$env:YOUTUBE_PROJECT_URL = "https://alamat-flask-kamu.example"
$env:ECOMMERCE_PROJECT_URL = "https://alamat-laravel-kamu.example"
python app.py
```

WBS dan JDIH sudah diarahkan ke sumber resmi:

- WBS LKPP: https://wbs.lkpp.go.id/home
- JDIH LKPP: https://jdih.lkpp.go.id/

Jadi folder aplikasi YouTube Recommendation dan E-Commerce **tidak perlu dimasukkan ke dalam folder homepage**. Homepage cukup menyimpan URL publik masing-masing project.
