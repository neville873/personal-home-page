import os

from flask import Flask, render_template

app = Flask(__name__)

PROFILE = {
    "name": "Neville Venerdi",
    "location": "Jembatan Lima, Jakarta Barat",
    "email": "nevillevenerdi@gmail.com",
    "birth": "Jakarta, 01 Juni 2004",
}

# Project URLs are kept here so you can change destinations without
# rewriting the homepage template. Set the two first URLs after you
# deploy your Flask and Laravel projects.
PROJECTS = [
    {
        "number": "01",
        "type": "Academic Project · Web + AI",
        "title": "Sistem Rekomendasi Konten Video YouTube",
        "description": (
            "Mengimplementasikan Content-Based Filtering berdasarkan metadata video "
            "dan minat pengguna berbasis web menggunakan Flask. Menerapkan NLP dengan "
            "model multilingual MiniLM dan membandingkan representasi teks untuk "
            "menghasilkan rekomendasi yang relevan."
        ),
        "chips": ["Flask", "Content-Based Filtering", "NLP", "MiniLM"],
        "label": "Live Demo",
        "url": os.getenv("YOUTUBE_PROJECT_URL", ""),
        "external": True,
    },
    {
        "number": "02",
        "type": "Academic Project · Web",
        "title": "Aplikasi E-Commerce Berbasis Web",
        "description": (
            "Mengembangkan platform pembelian perkakas dengan Laravel, termasuk "
            "transaksi, fitur saldo/top-up, serta alur pengguna dari produk hingga checkout."
        ),
        "chips": ["Laravel", "MySQL", "Transaction Flow"],
        "label": "Live Demo",
        "url": os.getenv("ECOMMERCE_PROJECT_URL", ""),
        "external": True,
    },
    {
        "number": "03",
        "type": "Internship Project · LKPP",
        "title": "Whistleblower System LKPP",
        "description": (
            "Pengembangan sistem Whistleblower berbasis web, mencakup tracking status "
            "laporan, komunikasi dua arah pelapor–admin, serta integrasi untuk manajemen kasus."
        ),
        "chips": ["Laravel", "System Development", "Case Management"],
        "label": "Visit WBS",
        "url": "https://wbs.lkpp.go.id/home",
        "external": True,
    },
    {
        "number": "04",
        "type": "Internship Project · LKPP",
        "title": "JDIH LKPP",
        "description": (
            "Pengembangan fitur dan dashboard statistik JDIH untuk membantu penyajian "
            "informasi hukum dan rekapitulasi produk hukum."
        ),
        "chips": ["Yii2", "Dashboard", "Data Visualization"],
        "label": "Visit JDIH",
        "url": "https://jdih.lkpp.go.id/statistic/index",
        "external": True,
    },
]

@app.route("/")
def home():
    return render_template("index.html", profile=PROFILE, projects=PROJECTS)

if __name__ == "__main__":
    app.run(debug=True)
