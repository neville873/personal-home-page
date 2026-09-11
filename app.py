from flask import Flask, render_template, request

app = Flask(__name__)

PROFILE = {
    "name": "Neville Venerdi",
    "location": "Jembatan Lima, Jakarta Barat",
    "email": "nevillevenerdi@gmail.com",
    "birth": "Jakarta, 01 Juni 2004",
}

TEXT = {
    "id": {
        "nav_about": "Tentang",
        "nav_experience": "Pengalaman",
        "nav_projects": "Proyek",
        "nav_skills": "Keahlian",
        "nav_contact": "Kontak",
        "talk": "Mari terhubung",
        "hero_eyebrow": "BERANDA PRIBADI · JAKARTA",
        "hero_intro": "Lulusan Teknik Informatika dengan pengalaman pengembangan aplikasi berbasis web, integrasi sistem, REST API, dan pengolahan data.",
        "explore": "Lihat proyek",
        "scroll": "Gulir untuk menjelajah",
        "visual_note": "Perangkat lunak · Web · Solusi digital",
        "about_label": "01 / TENTANG",
        "about_display": "Saya tertarik membangun <em>solusi digital</em> yang rapi, efisien, dan mudah digunakan — dari aplikasi web hingga sistem yang menghubungkan data dan proses bisnis.",
        "about_detail": "Memiliki pengalaman sebagai Software Engineer Intern di LKPP, mengembangkan sistem Whistleblower, tracking status laporan, komunikasi pelapor–admin, integrasi SIMCACM, serta dashboard statistik JDIH.",
        "based_in": "Domisili",
        "focus": "Fokus",
        "focus_value": "Web Development · API · Data",
        "exp_label": "02 / PENGALAMAN",
        "exp_date": "Mei 2025 — Sep 2025",
        "exp_title": "Software Engineer Intern",
        "exp_org": "LKPP · Lembaga Kebijakan Pengadaan Barang/Jasa Pemerintah",
        "contribution": "Kontribusi terpilih",
        "exp_items": [
            "Mengembangkan sistem Whistleblower berbasis web dengan Laravel.",
            "Membangun fitur tracking status laporan secara real-time.",
            "Mengembangkan komunikasi dua arah antara pelapor dan admin.",
            "Mengintegrasikan sistem dengan SIMCACM untuk manajemen kasus.",
            "Mengembangkan dashboard statistik JDIH menggunakan Yii2.",
            "Melakukan debugging, testing, dan peningkatan performa aplikasi.",
        ],
        "projects_label": "03 / PROYEK TERPILIH",
        "projects_title": "Karya yang mengubah<br><em>ide menjadi sistem.</em>",
        "projects_intro": "Empat proyek terpilih dari pengalaman akademik dan magang. Preview ditampilkan langsung agar pengunjung dapat melihat hasilnya tanpa perlu membuka halaman lain.",
        "view_project": "Lihat proyek",
        "visit_website": "Kunjungi website",
        "preview_available": "Preview tersedia",
        "preview_pending": "Preview website",
        "preview_pending_sub": "Tempat preview akan diperbarui",
        "org_label": "04 / ORGANISASI",
        "org_title": "Di luar<br><em>kode.</em>",
        "org_items": [
            ("2024 — 2025", "Ketua Tim Litbang · RIoT", "Memimpin riset dan pengembangan proyek IoT, mengarahkan diskusi teknis, pembagian tugas, pengujian, serta pengembangan prototipe Smart Plant Care System berbasis Arduino."),
            ("2022 — 2023", "Anggota · HIMTI", "Berkontribusi dalam seminar, pelatihan, dan event teknologi serta berkolaborasi dalam persiapan dan pelaksanaan kegiatan."),
            ("2021 — 2022", "HUMAS IT · ROHKRIS", "Membantu koordinasi kegiatan internal dan membuat materi publikasi serta dokumentasi kegiatan."),
        ],
        "skills_label": "05 / KEAHLIAN",
        "skills_title": "Kemampuan<br><em>yang saya gunakan.</em>",
        "skills_note": "Level merupakan gambaran penguasaan berdasarkan pengalaman proyek dan penggunaan teknologi yang tercantum di portofolio.",
        "advanced": "Mahir",
        "intermediate": "Menengah",
        "beginner": "Dasar",
        "soft_label": "Keterampilan Non-Teknis",
        "soft_skills": ["Pemecahan Masalah", "Berpikir Analitis", "Komunikasi & Kerja Sama Tim", "Teliti & Berorientasi pada Detail", "Tanggung Jawab & Integritas"],
        "education_label": "06 / PENDIDIKAN & SERTIFIKASI",
        "education": "Pendidikan",
        "certificates": "Sertifikasi",
        "view_certificate": "Lihat sertifikat",
        "certificate_missing": "Tambahkan gambar sertifikat di folder assets/certificates.",
        "certs": [
            {"name": "Dicoding — Pemrograman Python · 2024", "image": "assets/certificates/sertif-python.png"},
            {"name": "Dicoding — Web Development · 2022", "image": "assets/certificates/sertif-web.png"},
            {"name": "BNSP — Junior Web Programmer · 2026", "image": "assets/certificates/sertif-bnsp.png"},
        ],
        "contact_label": "07 / KONTAK",
        "contact_title": "Mari membangun sesuatu yang<br><em>berarti.</em>",
        "contact_text": "Terbuka untuk peluang dan kolaborasi di bidang software engineering, web development, dan solusi digital.",
        "footer": "NV. · Beranda Pribadi",
    },
    "en": {
        "nav_about": "About",
        "nav_experience": "Experience",
        "nav_projects": "Projects",
        "nav_skills": "Skills",
        "nav_contact": "Contact",
        "talk": "Let's connect",
        "hero_eyebrow": "BERANDA PRIBADI · JAKARTA",
        "hero_intro": "Informatics graduate with experience in web application development, system integration, REST APIs, and data processing.",
        "explore": "Explore work",
        "scroll": "Scroll to explore",
        "visual_note": "Software · Web · Digital solutions",
        "about_label": "01 / ABOUT",
        "about_display": "I enjoy building <em>digital solutions</em> that are thoughtful, efficient, and easy to use — from web applications to systems that connect data and business processes.",
        "about_detail": "Experience as a Software Engineer Intern at LKPP, contributing to the Whistleblower system, report-status tracking, complainant–admin communication, SIMCACM integration, and JDIH statistics dashboard.",
        "based_in": "Based in",
        "focus": "Focus",
        "focus_value": "Web Development · API · Data",
        "exp_label": "02 / EXPERIENCE",
        "exp_date": "May 2025 — Sep 2025",
        "exp_title": "Software Engineer Intern",
        "exp_org": "LKPP · Government Procurement Policy Agency",
        "contribution": "Selected contribution",
        "exp_items": [
            "Developed a web-based Whistleblower system using Laravel.",
            "Built real-time report status tracking features.",
            "Developed two-way communication between complainants and admins.",
            "Integrated the system with SIMCACM for case management.",
            "Developed a JDIH statistics dashboard using Yii2.",
            "Performed debugging, testing, and application performance improvements.",
        ],
        "projects_label": "03 / SELECTED PROJECTS",
        "projects_title": "Work that turns<br><em>ideas into systems.</em>",
        "projects_intro": "Four selected projects from academic and internship experience. Previews are shown directly so visitors can understand the work without opening another page.",
        "view_project": "View project",
        "visit_website": "Visit website",
        "preview_available": "Preview available",
        "preview_pending": "Website preview",
        "preview_pending_sub": "Preview slot ready to be updated",
        "org_label": "04 / ORGANIZATION",
        "org_title": "Beyond<br><em>the code.</em>",
        "org_items": [
            ("2024 — 2025", "Research & Development Lead · RIoT", "Led IoT research and development, guided technical discussions, task allocation, testing, and the Smart Plant Care System prototype built with Arduino."),
            ("2022 — 2023", "Member · HIMTI", "Contributed to seminars, training sessions, and technology events while collaborating on event preparation and execution."),
            ("2021 — 2022", "IT Public Relations · ROHKRIS", "Supported internal activity coordination and prepared publication and documentation materials."),
        ],
        "skills_label": "05 / SKILLS",
        "skills_title": "Capabilities<br><em>I work with.</em>",
        "skills_note": "Levels are an indicative view of proficiency based on the projects and technologies represented in this portfolio.",
        "advanced": "Advanced",
        "intermediate": "Intermediate",
        "beginner": "Beginner",
        "soft_label": "Soft Skills",
        "soft_skills": ["Problem Solving", "Analytical Thinking", "Communication & Teamwork", "Detail-Oriented", "Responsibility & Integrity"],
        "education_label": "06 / EDUCATION & CERTIFICATION",
        "education": "Education",
        "certificates": "Certificates",
        "view_certificate": "View certificate",
        "certificate_missing": "Add the certificate image to the assets/certificates folder.",
        "certs": [
            {"name": "Dicoding — Python Programming · 2024", "image": "assets/certificates/sertif-python.png"},
            {"name": "Dicoding — Web Development · 2022", "image": "assets/certificates/sertif-web.png"},
            {"name": "BNSP — Junior Web Programmer · 2026", "image": "assets/certificates/sertif-bnsp.png"},
        ],
        "contact_label": "07 / CONTACT",
        "contact_title": "Let's build something<br><em>meaningful.</em>",
        "contact_text": "Open to opportunities and collaborations in software engineering, web development, and digital solutions.",
        "footer": "NV. · Personal Homepage",
    },
}

PROJECTS = [
    {
        "number": "01",
        "type": {"id": "Proyek Akademik · Web + AI", "en": "Academic Project · Web + AI"},
        "title": {"id": "Sistem Rekomendasi Konten Video YouTube", "en": "YouTube Video Content Recommendation"},
        "description": {
            "id": "Mengimplementasikan Content-Based Filtering berdasarkan metadata video dan minat pengguna berbasis web menggunakan Flask. Menerapkan NLP dengan model multilingual MiniLM dan membandingkan representasi teks untuk menghasilkan rekomendasi yang relevan.",
            "en": "Implemented Content-Based Filtering using video metadata and user interests in a Flask-based web application. Applied NLP with multilingual MiniLM and compared text representations to produce relevant recommendations.",
        },
        "chips": ["Flask", "Content-Based Filtering", "NLP", "MiniLM"],
        # Tambah/hapus path di bawah untuk menentukan jumlah preview yang tampil.
        "preview_images": [
            "assets/projects/youtube/youtube-1.png",
            "assets/projects/youtube/youtube-2.png",
            "assets/projects/youtube/youtube-3.png",
        ],
        "url": None,
        "external": False,
    },
    {
        "number": "02",
        "type": {"id": "Proyek Akademik · Web", "en": "Academic Project · Web"},
        "title": {"id": "Aplikasi E-Commerce Berbasis Web", "en": "Web-Based E-Commerce Application"},
        "description": {
            "id": "Mengembangkan platform pembelian perkakas dengan Laravel, termasuk transaksi, fitur saldo/top-up, serta alur pengguna dari produk hingga checkout.",
            "en": "Developed a web-based tools purchasing platform with Laravel, including transactions, balance/top-up features, and a user flow from product selection to checkout.",
        },
        "chips": ["Laravel", "MySQL", "Transaction Flow"],
        # Jumlah preview bebas; cukup tambahkan atau hapus path gambar di list ini.
        "preview_images": [
            "assets/projects/ecommerce/ecomm-1.png",
            "assets/projects/ecommerce/ecomm-2.png",
            "assets/projects/ecommerce/ecomm-3.png",
            "assets/projects/ecommerce/ecomm-4.png",
        ],
        "url": None,
        "external": False,
    },
    {
        "number": "03",
        "type": {"id": "Proyek Magang · LKPP", "en": "Internship Project · LKPP"},
        "title": {"id": "Whistleblower System LKPP", "en": "LKPP Whistleblower System"},
        "description": {
            "id": "Pengembangan sistem Whistleblower berbasis web, mencakup tracking status laporan, komunikasi dua arah pelapor–admin, serta integrasi untuk manajemen kasus.",
            "en": "Contributed to a web-based Whistleblower system covering report-status tracking, two-way complainant–admin communication, and integration for case management.",
        },
        "chips": ["Laravel", "System Development", "Case Management"],
        "preview_images": [
            "assets/projects/wbs/wbs-1.png",
            "assets/projects/wbs/wbs-2.png",
            "assets/projects/wbs/wbs-3.png",
            "assets/projects/wbs/wbs-4.png",
        ],
        "url": "https://wbs.lkpp.go.id/home",
        "external": True,
    },
    {
        "number": "04",
        "type": {"id": "Proyek Magang · LKPP", "en": "Internship Project · LKPP"},
        "title": {"id": "JDIH LKPP", "en": "LKPP JDIH"},
        "description": {
            "id": "Pengembangan fitur dan dashboard statistik JDIH untuk membantu penyajian informasi hukum dan rekapitulasi produk hukum.",
            "en": "Contributed to JDIH features and a statistics dashboard for clearer legal-information presentation and product-law reporting.",
        },
        "chips": ["Yii2", "Dashboard", "Data Visualization"],
        "preview_images": [
            "assets/projects/jdih/jdih-1.png",
            "assets/projects/jdih/jdih-2.png",
            "assets/projects/jdih/jdih-3.png",
        ],
        "url": "https://jdih.lkpp.go.id/",
        "external": True,
    },
]

SKILLS = {
    "advanced": ["Python", "PHP", "Laravel", "Flask", "MySQL / MariaDB", "REST API"],
    "intermediate": ["JavaScript", "Django", "Yii2", "React.js", "API Development", "Database Integration", "Git"],
    "beginner": ["Go", "Java"],
}

EDUCATION = [
    ("Institut Teknologi dan Bisnis Swadharma", "S1 Teknik Informatika · 2022 — 2026"),
    ("SMA Negeri 17 Jakarta", "IPA · 2019 — 2022"),
]

@app.route("/")
def home():
    lang = request.args.get("lang", "id").lower()
    if lang not in TEXT:
        lang = "id"
    return render_template(
        "index.html",
        profile=PROFILE,
        projects=PROJECTS,
        skills=SKILLS,
        education=EDUCATION,
        t=TEXT[lang],
        lang=lang,
    )


if __name__ == "__main__":
    app.run(debug=True)
