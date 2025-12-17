import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
from io import BytesIO

LANGUAGES = {
    "en": {
        "page_title": "WELCOME TO MATRIX TRANSFORMATION",
        "home": "Home",
        "features": "Features",
        "about_us": "About Us",
        "continue": "➤ ➤ ➤ Continue",
        "platform_title": "🚀 Digital visualization of matrix transformation",
        "platform_desc": "A Digital Platform for Learning Matrix Transformations",
        
        "intro_title": "INTRODUCTION OF MATRIX TRANSFORMATIONS & CONVOLUTION",
        "app_desc": "Description of What the Application Does",
        "app_desc_text": "The application is a multi-page Streamlit web platform that demonstrates fundamental image processing operations using matrix transformations and convolution techniques. Users can upload an image and apply various geometric transformations—such as translation, rotation, scaling, shearing, and reflection—implemented through matrix multiplication. In addition, the application provides convolution-based filters, including blurring, sharpening, edge detection, and noise reduction, using predefined kernels.",
        "matrix_title": "Matrix Transformations and Visual Examples",
        "matrix_desc": "Matrix transformations are mathematical operations that use matrices to change the position, size, orientation, or shape of objects in space. They are fundamental in linear algebra and widely applied in fields such as computer graphics, image processing, robotics, physics, and engineering. Matrix transformations work by multiplying a matrix with a vector or another matrix. The vector typically represents a point or an object in space, while the matrix defines how that point or object is transformed. For example, a point in 2D space can be represented as a vector (x, y), and a tranformation matrix determines how that point is moved or altered.",
        "translation": "Translation",
        "scaling": "Scaling",
        "rotation": "Rotation",
        "shearing": "Shearing",
        "reflection": "Reflection",
        "translation_vector": "Translation moves an object from one position to another withour changing its shape or size. In practice, translation is often implemented using homogeneous coordinate so it can be expressed as matrix multiplication. For example:",
        "scaling_matrix": "Scaling changes the size of an object. A scaling matrix can enlarge or shrink an object along the x-axis, y-axis, or both. For example:",
        "rotation_matrix": "Rotation turns an object around a fixed point (usually the origin). Rotation matrices are defined using trigonometric functions (sine and cosine) and depend on the angle of rotation. For example:",
        "shear_matrix": "Shearing skews the shape of an object, shifting one axis in proportion to another. This transformation changes angles but may preserve area in some cases. For example:",
        "reflection_matrix": "Reflection flips an object across a line (in 2D) or a plane (in 3D), such as reflecting across the x-axis or y-axis. For example:",
        "choose_reflection": "Choose reflection type:",
        "reflect_x": "Reflect over X-axis",
        "reflect_y": "Reflect over Y-axis",
        "reflect_origin": "Reflect over Origin",
        "success_transform": "Matrix transformation generated successfully!",
        "back_home": "Back to home",
        
        "image_tools": "Image Processing Tools",
        "image_tools_desc": "Upload an image and apply various transformations and filters to see the results in real-time.",
        "geo_transform": "🔄 Geometric Transformations",
        "image_filter": "🎭 Image Filtering",
        "bg_removal": "✂️ Background Removal",
        "upload_image": "Upload an image",
        "select_transform": "Select Transformation Type:",
        "original_image": "Original Image",
        "preview": "Preview",
        "translate_x": "Translate X",
        "translate_y": "Translate Y",
        "scale_x": "Scale X",
        "scale_y": "Scale Y",
        "rotation_angle": "Rotation Angle (degrees)",
        "shear_x": "Shear X",
        "shear_y": "Shear Y",
        "reflection_axis": "Reflection Axis:",
        "download_result": "Download Result",
        "please_upload": "👆 Please upload an image to start",
        "select_filter": "Select Filter Type:",
        "blur": "Blur",
        "sharpen": "Sharpen",
        "kernel_size": "Size",
        "sharpen_strength": "Sharpen Strength",
        "color_adjust": "🎨 Color Adjustments:",
        "brightness": "Brightness",
        "contrast": "Contrast",
        "saturation": "Saturation",
        "hue_shift": "Hue Shift",
        "adjust_hsv": "Adjust HSV Range to Remove Background:",
        "hue_min": "Hue Min",
        "hue_max": "Hue Max",
        "sat_min": "Saturation Min",
        "sat_max": "Saturation Max",
        "val_min": "Value Min",
        "val_max": "Value Max",
        "result_success": "Result generated successfully!✅",
        
        "how_works": "How the App Works",
        "how_works_text": """This Matrix Transformation application demonstrates fundamental image processing through an interactive interface:
        
1. **Upload Your Image:** Upload images in JPG, JPEG, or PNG format
2. **Select Transformation:** Choose from geometric transformations or image filtering operations
3. **Adjust Parameters:** Use interactive sliders to fine-tune transformations in real-time
4. **View Results:** See original and transformed images side-by-side with mathematical matrices
5. **Download Results:** Save your processed image with one click

The application uses matrix multiplication for geometric transformations and convolution for filtering.""",
        "team_members": "Our Team Members",
        "leader": "Project Leader & System Coordinator",
        "backend": "Backend Developer",
        "frontend": "Fronted Developer",
        "docs": "Documentation & Content Specialist",
        "contrib_1": "Led the project development process and ensured that all components of the web application functional cohesively & met project objectives.",
        "contrib_2": "Developed core image processing functions including geometric transformations and convolution operations using OpenCV and NumPy.",
        "contrib_3": "Implemented Streamlit interface, created interactive controls, and integrated real-time preview functionality.",
        "contrib_4": "Prepared comprehensive documentation, created mathematical explanations, and developed educational content for the Home page.",
    },
    "id": {
        "page_title": "SELAMAT DATANG DI TRANSFORMASI MATRIKS",
        "home": "Beranda",
        "features": "Fitur",
        "about_us": "Tentang Kami",
        "continue": "➤ ➤ ➤ Lanjutkan",
        "platform_title": "🚀 Visualisasi transformasi matriks secara digital",
        "platform_desc": "Platform Digital untuk Belajar Transformasi Matriks",
        
        "intro_title": "PENGENALAN TRANSFORMASI MATRIKS & KONVOLUSI",
        "app_desc": "Deskripsi Fungsi Aplikasi",
        "app_desc_text": "Aplikasi ini adalah platform web Streamlit multi-halaman yang mendemonstrasikan operasi pemrosesan gambar fundamental menggunakan teknik transformasi matriks dan konvolusi. Pengguna dapat mengunggah gambar dan menerapkan berbagai transformasi geometrik—seperti translasi, rotasi, penskalaan, shearing, dan refleksi—yang diimplementasikan melalui perkalian matriks. Selain itu, aplikasi ini menyediakan filter berbasis konvolusi, termasuk blur, sharpen, deteksi tepi, dan pengurangan noise, menggunakan kernel yang telah ditentukan.",
        "matrix_title": "Transformasi Matriks dan Contoh Visual",
        "matrix_desc": "Transformasi matriks adalah operasi matematika yang menggunakan matriks untuk mengubah posisi, ukuran, orientasi, atau bentuk suatu objek didalam ruang. Transformasi ini merupakan konsep fundamental dalam aljabar linear dan banyak diterapkan pada berbagai bidang sperti grafika komputer, pemrosesan citra, robotika, fisika, dan teknik. Transformasi matriks bekerja dengan cara mengalikan sebuah matriks dengan sebuah vector atau matriks lainnya. Vector biasanya merepresentasikan suatu titik atau objek didalam ruang, sedangkan matriks menentukan bagaimana titik atau objek tersebut di transformasikan. Contohnya, sebuah titik dalam ruang dua dimensi dapat direpresentasikan sebagai vektor (x, y), dan sebuah matriks tranformasi menentukan bagaimana titik tersebut dipindahkan atau diubah.",
        "translation": "Translasi",
        "scaling": "Penskalaan",
        "rotation": "Rotasi",
        "shearing": "Shearing",
        "reflection": "Refleksi",
        "translation_vector": "Translasi memindahkan suatu objek dari satu posisi ke posisi lainnya tanpa mengubah bentuk atau ukurannya. Dalam praktiknya, translasi sering diimplementasikan menggunakan koordinat homogen sehingga dapat dipresentasikan dalam bentuk perkalian  matriks. Sebagai contoh:",
        "scaling_matrix": "Penskalaan mengubah ukuran suatu objek. Matriks penskalaan dapat memperbesar atau memperkecil objek sepanjang sumbu x, sumbu y, atau keduanya. Sebagai contoh:",
        "rotation_matrix": "Rotasi memutar suatu objek terhadap titik tetap tertentu, biasanya titik pusat (origin). Matriks rotasi didefenisikan menggunakan fungsi trigonometeri, yaitu sinus dan konsinus, dan bergantung pada besar sudut rotasi. Sebagai contoh:",
        "shear_matrix": "Shearing mengubah bentuk objek dengan cara menggeser satu sumbu secara proporsional terhadap sumbu lainnya. Transformasi ini mengubah besar sudut pada objek, namun dalam beberapa kasus dapat mempertahankan luas objek. Sebagai contoh:",
        "reflection_matrix": "Refleksi membalik suatu objek terhadap suatu garis (pada ruang dua dimensi) atau bidang (pada ruang tiga dimensi), misalnya refleksi terhadap sumbu x atau sumbu y. Sebagai contoh:",
        "choose_reflection": "Pilih jenis refleksi:",
        "reflect_x": "Refleksi terhadap sumbu-X",
        "reflect_y": "Refleksi terhadap sumbu-Y",
        "reflect_origin": "Refleksi terhadap Origin",
        "success_transform": "Transformasi matriks berhasil dibuat!",
        "back_home": "Kembali ke beranda",
        
        "image_tools": "Alat Pemrosesan Gambar",
        "image_tools_desc": "Unggah gambar dan terapkan berbagai transformasi dan filter untuk melihat hasilnya secara real-time.",
        "geo_transform": "🔄 Transformasi Geometrik",
        "image_filter": "🎭 Filter Gambar",
        "bg_removal": "✂️ Penghapusan Latar Belakang",
        "upload_image": "Unggah gambar",
        "select_transform": "Pilih Jenis Transformasi:",
        "original_image": "Gambar Asli",
        "preview": "Pratinjau",
        "translate_x": "Translasi X",
        "translate_y": "Translasi Y",
        "scale_x": "Skala X",
        "scale_y": "Skala Y",
        "rotation_angle": "Sudut Rotasi (derajat)",
        "shear_x": "Shear X",
        "shear_y": "Shear Y",
        "reflection_axis": "Sumbu Refleksi:",
        "download_result": "Unduh Hasil",
        "please_upload": "👆 Silakan unggah gambar untuk memulai",
        "select_filter": "Pilih Jenis Filter:",
        "blur": "Blur",
        "sharpen": "Sharpen",
        "kernel_size": "Ukuran",
        "sharpen_strength": "Kekuatan Sharpen",
        "color_adjust": "🎨 Penyesuaian Warna:",
        "brightness": "Kecerahan",
        "contrast": "Kontras",
        "saturation": "Saturasi",
        "hue_shift": "Pergeseran Hue",
        "adjust_hsv": "Sesuaikan Rentang HSV untuk Menghapus Latar Belakang:",
        "hue_min": "Hue Minimum",
        "hue_max": "Hue Maksimum",
        "sat_min": "Saturasi Minimum",
        "sat_max": "Saturasi Maksimum",
        "val_min": "Value Minimum",
        "val_max": "Value Maksimum",
        "result_success": "Hasil berhasil dibuat!✅",
        
        "how_works": "Cara Kerja Aplikasi",
        "how_works_text": """Aplikasi Transformasi Matriks ini mendemonstrasikan pemrosesan gambar fundamental melalui antarmuka interaktif:

1. **Unggah Gambar Anda:** Unggah gambar dalam format JPG, JPEG, atau PNG
2. **Pilih Transformasi:** Pilih dari transformasi geometrik atau operasi filter gambar
3. **Sesuaikan Parameter:** Gunakan slider interaktif untuk menyesuaikan transformasi secara real-time
4. **Lihat Hasil:** Lihat gambar asli dan hasil transformasi secara berdampingan dengan matriks matematis
5. **Unduh Hasil:** Simpan gambar yang telah diproses dengan satu klik

Aplikasi ini menggunakan perkalian matriks untuk transformasi geometrik dan konvolusi untuk filtering.""",
        "team_members": "Anggota Tim Kami",
        "leader": "Pemimpin Proyek & Koordinator Sistem",
        "backend": "Pengembang Backend",
        "frontend": "Pengembang Frontend",
        "docs": "Spesialis Dokumentasi",
        "contrib_1": "Memimpin proses pengembangan dan memastikan seluruh komponen aplikasi web berjalan secara terpadu serta sesuai dengan tujuan proyek.",
        "contrib_2": "Mengembangkan fungsi pemrosesan gambar inti termasuk transformasi geometrik dan operasi konvolusi menggunakan OpenCV dan NumPy.",
        "contrib_3": "Mengimplementasikan antarmuka Streamlit, membuat kontrol interaktif, dan mengintegrasikan fungsi pratinjau real-time.",
        "contrib_4": "Menyiapkan dokumentasi komprehensif, membuat penjelasan matematis, dan mengembangkan konten edukatif untuk halaman Beranda.",
    }
}

st.set_page_config(
    page_title="Matrix Transformation",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if 'language' not in st.session_state:
    st.session_state.language = "en"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:wght@600;700;800&family=Outfit:wght@300;400;500;600;700&display=swap');
    
    /* Background dan tema utama - Warna lebih soft */
    .stApp {
        background: linear-gradient(135deg, #fef5f7 0%, #cbd8ec 50%, #cbd8ec 100%);
        font-family: 'Inter', 'Outfit', sans-serif;
        color: #000000;
    }
    
    .language-selector {
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 10000;
        background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%);
        padding: 10px 20px;
        border-radius: 25px;
        border: 2px solid rgba(236, 169, 194, 0.4);
        box-shadow: 0 4px 16px rgba(216, 27, 96, 0.2);
        display: flex;
        gap: 10px;
        align-items: center;
    }
    
    .lang-btn {
        background: linear-gradient(135deg, #d81b60, #ec407a);
        color: white;
        border: none;
        padding: 8px 16px;
        border-radius: 15px;
        cursor: pointer;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 2px 8px rgba(216, 27, 96, 0.3);
    }
    
    .lang-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(216, 27, 96, 0.4);
    }
    
    .lang-btn.active {
        background: linear-gradient(135deg, #880e4f, #c2185b);
        box-shadow: 0 4px 12px rgba(136, 14, 79, 0.5);
    }
    
    .main-header {
        text-align: center;
        padding: 3.5rem 2rem;
        margin-bottom: 3rem;
        background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%);
        border-radius: 25px;
        border: 2px solid rgba(236, 169, 194, 0.4);
        box-shadow: 0 8px 32px rgba(233, 158, 188, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(
            45deg,
            transparent,
            rgba(255, 240, 245, 0.5),
            transparent
        );
        animation: rotate 6s linear infinite;
    }
    
    @keyframes rotate {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .matrix-title {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #d81b60, #ec407a, #f06292, #f48fb1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 2px 2px 4px rgba(216, 27, 96, 0.1);
        letter-spacing: 2px;
        animation: glow 3s ease-in-out infinite alternate;
        position: relative;
        z-index: 1;
        margin: 0;
        padding: 0;
    }
    
    @keyframes glow {
        from { filter: drop-shadow(0 0 8px rgba(236, 64, 122, 0.3)); }
        to { filter: drop-shadow(0 0 16px rgba(216, 27, 96, 0.5)); }
    }
    
    .nav-card {
        background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%);
        border-radius: 20px;
        padding: 2.5rem 2rem;
        text-align: center;
        border: 2px solid rgba(236, 169, 194, 0.3);
        box-shadow: 0 6px 24px rgba(216, 27, 96, 0.15);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        margin: 1rem 0;
        cursor: pointer;
        height: 280px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    .nav-card:hover {
        transform: translateY(-12px) scale(1.02);
        border-color: rgba(216, 27, 96, 0.5);
        box-shadow: 0 12px 40px rgba(216, 27, 96, 0.25);
        background: linear-gradient(135deg, #fce4ec 0%, #f48fb1 100%);
    }
    
    .card-icon {
        font-size: 5rem;
        margin-bottom: 1rem;
        filter: drop-shadow(0 4px 8px rgba(216, 27, 96, 0.2));
    }
    
    .card-title {
        color: #880e4f;
        font-size: 2rem;
        font-weight: 600;
        margin-top: 1rem;
        font-family: 'Poppins', times new roman;
    }
    
    .card-desc {
        color: #ad1457;
        font-size: 1rem;
        margin-top: 0.5rem;
    }
    
    .content-section {
        background: linear-gradient(135deg, rgba(252, 228, 236, 0.5) 0%, rgba(248, 187, 208, 0.3) 100%);
        border-radius: 20px;
        padding: 2.5rem;
        margin: 2rem 0;
        border: 1px solid rgba(236, 169, 194, 0.3);
        box-shadow: 0 4px 16px rgba(216, 27, 96, 0.08);
        backdrop-filter: blur(10px);
    }
    
    h1 {
        color: #c2185b;
        font-family: 'Playfair Display', serif;
        font-weight: 700;
    }
    
    h2, h3 {
        color: #d81b60;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
    }
    
    p {
        color: #000000;
        line-height: 1.8;
        font-weight: 400;
    }
    
    li {
        color: #4a1942;
    }
    
    .content-text {
        color: #5d1049;
        font-size: 1.05rem;
        line-height: 1.9;
    }
    
    div[data-testid="column"] > div > div > div > button {
        opacity: 0;
        height: 0;
        padding: 0;
        margin: 0;
        position: absolute;
        pointer-events: none;
    }
    
    div[data-testid="column"] > div:last-child button,
    div:not([data-testid="column"]) button {
        opacity: 1 !important;
        height: auto !important;
        padding: 0.75rem 2.5rem !important;
        position: relative !important;
        pointer-events: auto !important;
        background: linear-gradient(135deg, #d81b60, #ec407a) !important;
        color: #ffffff !important;
        font-weight: 600 !important;
        font-family: 'Poppins', times new roman !important;
        border-radius: 12px !important;
        border: none !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 12px rgba(216, 27, 96, 0.3) !important;
    }
    
    div:not([data-testid="column"]) button:hover {
        transform: translateY(-2px) scale(1.05) !important;
        box-shadow: 0 6px 20px rgba(216, 27, 96, 0.4) !important;
        background: linear-gradient(135deg, #c2185b, #d81b60) !important;
    }
    
    [data-testid="stMetricValue"] {
        color: #880e4f;
        font-size: 2rem;
        font-weight: 600;
    }
    
    [data-testid="stMetricLabel"] {
        color: #ad1457;
        font-weight: 500;
    }
    
    .stMarkdown, .stText {
        color: #4a1942;
    }
    
    /* Table text */
    table {
        color: #00000;
    }
    
    /* Input labels */
    label {
        color: #880e4f;
        font-weight: 500;
    }
    
    /* Success/Info/Warning messages */
    .stSuccess {
        background-color: rgba(248, 187, 208, 0.2);
        color: #880e4f;
        border-left: 4px solid #d81b60;
    }
    
    .stInfo {
        background-color: rgba(252, 228, 236, 0.3);
        color: #ad1457;
        border-left: 4px solid #ec407a;
    }
    
    .stWarning, .stError {
        color: #4a1942;
    }
    
    .falling-hearts {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 9999;
        overflow: hidden;
    }
    
    .heart {
        position: absolute;
        top: -50px;
        font-size: 20px;
        animation: fall linear infinite;
        opacity: 0.6;
    }
    
    @keyframes fall {
        to {
            top: 100vh;
            transform: translateX(100px) rotate(360deg);
        }
    }
    
    .heart:nth-child(1) { left: 10%; animation-duration: 9s; animation-delay: 0s; }
    .heart:nth-child(2) { left: 20%; animation-duration: 11s; animation-delay: 2s; }
    .heart:nth-child(3) { left: 30%; animation-duration: 8s; animation-delay: 4s; }
    .heart:nth-child(4) { left: 40%; animation-duration: 10s; animation-delay: 1s; }
    .heart:nth-child(5) { left: 50%; animation-duration: 12s; animation-delay: 3s; }
    .heart:nth-child(6) { left: 60%; animation-duration: 9s; animation-delay: 5s; }
    .heart:nth-child(7) { left: 70%; animation-duration: 11s; animation-delay: 2s; }
    .heart:nth-child(8) { left: 80%; animation-duration: 10s; animation-delay: 4s; }
    .heart:nth-child(9) { left: 90%; animation-duration: 8s; animation-delay: 1s; }
    .heart:nth-child(10) { left: 15%; animation-duration: 13s; animation-delay: 0s; }
    
    .member-photo-container {
        display: flex;
        justify-content: center;
        margin-bottom: 1.5rem;
    }
    
    .member-photo-circle {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        object-fit: cover;
        border: 4px solid #d81b60;
        box-shadow: 0 6px 20px rgba(216, 27, 96, 0.3);
        transition: all 0.3s ease;
    }
    
    .member-photo-circle:hover {
        transform: scale(1.08);
        box-shadow: 0 8px 28px rgba(216, 27, 96, 0.4);
    }
    
    .member-emoji-circle {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 4rem;
        border: 4px solid #d81b60;
        box-shadow: 0 6px 20px rgba(216, 27, 96, 0.3);
        transition: all 0.3s ease;
    }
    
    .member-emoji-circle:hover {
        transform: scale(1.08);
        box-shadow: 0 8px 28px rgba(216, 27, 96, 0.4);
    }
    
    .member-card {
        background: linear-gradient(135deg, rgba(252, 228, 236, 0.8) 0%, rgba(248, 187, 208, 0.6) 100%);
        padding: 2rem;
        border-radius: 20px;
        border: 2px solid rgba(236, 169, 194, 0.4);
        box-shadow: 0 6px 24px rgba(216, 27, 96, 0.15);
        text-align: center;
        margin-bottom: 2rem;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }
    
    .member-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 32px rgba(216, 27, 96, 0.25);
    }
    
    .member-name {
        color: #c2185b;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        font-family: 'Poppins', sans-serif;
    }
    
    .member-role {
        color: #d81b60;
        font-weight: 600;
        margin-bottom: 1rem;
        font-size: 1.05rem;
    }
    
    .member-contribution {
        color: #5d1049;
        line-height: 1.7;
        font-size: 0.95rem;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(252, 228, 236, 0.5);
        color: #ad1457;
        border-radius: 8px;
        font-weight: 500;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #d81b60;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

def render_language_selector():
    col1, col2, col3 = st.columns([6, 1, 1])
    with col2:
        if st.button("ENG", use_container_width=True, key="lang_en"):
            st.session_state.language = "en"
            st.rerun()
    with col3:
        if st.button("ID", use_container_width=True, key="lang_id"):
            st.session_state.language = "id"
            st.rerun()

def t(key):
    return LANGUAGES[st.session_state.language][key]

st.markdown("""
<div class="falling-hearts">
    <div class="heart">🎀</div>
    <div class="heart">🌸</div>
    <div class="heart">💕</div>
    <div class="heart">🌷</div>
    <div class="heart">💗</div>
    <div class="heart">🎀</div>
    <div class="heart">🌸</div>
    <div class="heart">💕</div>
    <div class="heart">🌷</div>
    <div class="heart">🦩</div>
</div>
""", unsafe_allow_html=True)

def plot_transformation(original, transformed, title):
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.grid(True, alpha=0.3)
    ax.axhline(0, color='#d81b60', linewidth=0.5)
    ax.axvline(0, color="#1192dd", linewidth=0.5)

    ax.plot(original[:, 0], original[:, 1], marker='o', label='Original', color='#1192dd', linewidth=2)
    ax.plot(transformed[:, 0], transformed[:, 1], marker='o', label='Transformed', color='#d81b60', linewidth=2)

    ax.set_title(title, fontsize=12, fontweight='bold', color='#880e4f')
    ax.legend()
    ax.set_xlim(-7, 7)
    ax.set_ylim(-7, 7)

    st.pyplot(fig)


def apply_translation(image, tx, ty):
    rows, cols = image.shape[:2]
    M = np.float32([[1, 0, tx], [0, 1, ty]])
    translated = cv2.warpAffine(image, M, (cols, rows))
    return translated

def apply_scaling(image, sx, sy):
    rows, cols = image.shape[:2]
    M = np.float32([[sx, 0, 0], [0, sy, 0]])
    scaled = cv2.warpAffine(image, M, (int(cols * sx), int(rows * sy)))
    return scaled

def apply_rotation(image, angle):
    rows, cols = image.shape[:2]
    center = (cols / 2, rows / 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (cols, rows))
    return rotated

def apply_shearing(image, shear_x, shear_y):
    rows, cols = image.shape[:2]
    M = np.float32([[1, shear_x, 0], [shear_y, 1, 0]])
    sheared = cv2.warpAffine(image, M, (cols + int(rows * abs(shear_x)), rows + int(cols * abs(shear_y))))
    return sheared

def apply_reflection(image, axis):
    if "X" in axis or "sumbu-X" in axis:
        reflected = cv2.flip(image, 0)
    elif "Y" in axis or "sumbu-Y" in axis:
        reflected = cv2.flip(image, 1)
    else:
        reflected = cv2.flip(cv2.flip(image, 0), 1)
    return reflected

def apply_convolution(image, kernel):
    if len(image.shape) == 3:
        channels = cv2.split(image)
        result_channels = []
        for channel in channels:
            filtered = cv2.filter2D(channel, -1, kernel)
            result_channels.append(filtered)
        result = cv2.merge(result_channels)
    else:
        result = cv2.filter2D(image, -1, kernel)
    return result

def adjust_color(image, brightness=0, contrast=1.0, saturation=1.0, hue_shift=0):
    adjusted = cv2.convertScaleAbs(image, alpha=contrast, beta=brightness)
    
    if len(adjusted.shape) == 3:
        hsv = cv2.cvtColor(adjusted, cv2.COLOR_RGB2HSV).astype(np.float32)
        hsv[:, :, 1] = np.clip(hsv[:, :, 1] * saturation, 0, 255)
        hsv[:, :, 0] = (hsv[:, :, 0] + hue_shift) % 180
        hsv = hsv.astype(np.uint8)
        result = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
    else:
        result = adjusted
    
    return result

def remove_background_color(image, lower_hsv, upper_hsv):
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    mask_inv = cv2.bitwise_not(mask)
    
    result = cv2.bitwise_and(image, image, mask=mask_inv)
    
    white_bg = np.ones_like(image) * 255
    bg = cv2.bitwise_and(white_bg, white_bg, mask=mask)
    result = cv2.add(result, bg)
    
    return result

def convert_image_to_bytes(image_array):
    if image_array.dtype != np.uint8:
        image_array = np.clip(image_array, 0, 255).astype(np.uint8)
    
    img = Image.fromarray(image_array)
    buf = BytesIO()
    img.save(buf, format='PNG')
    byte_im = buf.getvalue()
    return byte_im


def landing_page():
    render_language_selector()
    
    st.markdown('<div class="main-header">', unsafe_allow_html=True)
    st.markdown(f'<h1 class="matrix-title">{t("page_title")}</h1>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1], gap="large")
    
    with col1:
        st.markdown(f"""
        <div class="nav-card" onclick="document.getElementById('home_btn').click()">
            <div class="card-icon">🏠</div>
            <div class="card-title">{t("home")}</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(t("continue"), key="home_btn", use_container_width=True):
            st.session_state.page = "Home"
            st.rerun()
    
    with col2:
        st.markdown(f"""
        <div class="nav-card" onclick="document.getElementById('features_btn').click()">
            <div class="card-icon">✨</div>
            <div class="card-title">{t("features")}</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(t("continue"), key="features_btn", use_container_width=True):
            st.session_state.page = "Features"
            st.rerun()
    
    with col3:
        st.markdown(f"""
        <div class="nav-card" onclick="document.getElementById('about_btn').click()">
            <div class="card-icon">👥</div>
            <div class="card-title">{t("about_us")}</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(t("continue"), key="about_btn", use_container_width=True):
            st.session_state.page = "About Us"
            st.rerun()
    
    st.markdown("---")
    st.markdown(f"""
    <div style='text-align: center; padding: 2rem;'>
        <h3 style='color: #d81b60; font-family: Playfair Display, serif;'>{t("platform_title")}</h3>
        <p style='color: #5d1049; font-size: 1.1rem;'>{t("platform_desc")}</p>
    </div>
    """, unsafe_allow_html=True)


def home_page():
    render_language_selector()
    
    st.markdown(f'<h1 class="matrix-title" style="text-align: center;">🏠 {t("home").upper()}</h1>', unsafe_allow_html=True)
    st.markdown(f'<h1 class="matrix-title">{t("intro_title")}</h1>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.markdown(f"### 📝 {t('app_desc')}")
    
    st.markdown(f"""
    <div class="content-text">
    {t('app_desc_text')}
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.markdown(f"### 🔢 {t('matrix_title')}")
    
    st.markdown(f"""
    <div class="content-text">
    {t('matrix_desc')}
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    shape = np.array([[1, 1], [1, 3], [3, 3], [3, 1], [1, 1]])
    
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.markdown(f"#### 1. {t('translation')} 📐")
    translation_vector = np.array([2, -1])
    translated = shape + translation_vector
    st.write(f"**{t('translation_vector')}**")
    st.write(translation_vector)
    plot_transformation(shape, translated, f"{t('translation')} Example")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.markdown(f"#### 2. {t('scaling')} 📏")
    scale_matrix = np.array([[2, 0], [0, 1.5]])
    scaled = shape @ scale_matrix.T
    st.write(f"**{t('scaling_matrix')}**")
    st.write(scale_matrix)
    plot_transformation(shape, scaled, f"{t('scaling')} Example")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.markdown(f"#### 3. {t('rotation')} 🔄")
    theta = np.radians(45)
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    rotated = shape @ rotation_matrix.T
    st.write(f"**{t('rotation_matrix')}**")
    st.write(rotation_matrix)
    plot_transformation(shape, rotated, f"{t('rotation')} Example")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.markdown(f"#### 4. {t('shearing')} 🔀")
    shear_matrix = np.array([[1, 1], [0, 1]])
    sheared = shape @ shear_matrix.T
    st.write(f"**{t('shear_matrix')}**")
    st.write(shear_matrix)
    plot_transformation(shape, sheared, f"{t('shearing')} Example")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.markdown(f"#### 5. {t('reflection')} 👤")
    
    reflection_options = [t("reflect_x"), t("reflect_y"), t("reflect_origin")]
    option = st.selectbox(t("choose_reflection"), reflection_options)
    
    reflect_x = np.array([[1, 0], [0, -1]])
    reflect_y = np.array([[-1, 0], [0, 1]])
    reflect_origin = np.array([[-1, 0], [0, -1]])
    
    if option == reflection_options[0]:
        matrix = reflect_x
        reflected = shape @ matrix.T
    elif option == reflection_options[1]:
        matrix = reflect_y
        reflected = shape @ matrix.T
    else:
        matrix = reflect_origin
        reflected = shape @ matrix.T
    
    st.write(f"**{t('reflection_matrix')}**")
    st.write(matrix)
    plot_transformation(shape, reflected, f"{option} Example")
    st.success(t("success_transform"))
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button(t("back_home"), use_container_width=False):
        st.session_state.page = "Landing"
        st.rerun()


def features_page():
    render_language_selector()
    
    st.markdown(f'<h1 class="matrix-title" style="text-align: center;">✨ {t("features").upper()}</h1>', unsafe_allow_html=True)
    
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.markdown(f"### 🎨 {t('image_tools')}")
    st.markdown(f"""
    <div class="content-text">
    {t('image_tools_desc')}
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs([t("geo_transform"), t("image_filter"), t("bg_removal")])
    
    with tab1:
        st.markdown(f"### {t('geo_transform')}")
        uploaded_file = st.file_uploader(t("upload_image"), type=["jpg", "jpeg", "png"], key="geo_upload")
        
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            image_array = np.array(image)
            
            transform_options = [t("translation"), t("scaling"), t("rotation"), t("shearing"), t("reflection")]
            transform_type = st.selectbox(t("select_transform"), transform_options)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"**{t('original_image')}**")
                st.image(image, use_container_width=True)
            
            with col2:
                st.markdown(f"**{t('preview')}**")
                
                if transform_type == transform_options[0]:  
                    tx = st.slider(t("translate_x"), -200, 200, 0)
                    ty = st.slider(t("translate_y"), -200, 200, 0)
                    result = apply_translation(image_array, tx, ty)
                    st.image(result, use_container_width=True)
                    st.download_button(t("download_result"), convert_image_to_bytes(result), "translated_image.png", "image/png")
                
                elif transform_type == transform_options[1]:  
                    sx = st.slider(t("scale_x"), 0.1, 3.0, 1.0, 0.1)
                    sy = st.slider(t("scale_y"), 0.1, 3.0, 1.0, 0.1)
                    result = apply_scaling(image_array, sx, sy)
                    st.image(result, use_container_width=True)
                    st.download_button(t("download_result"), convert_image_to_bytes(result), "scaled_image.png", "image/png")
                
                elif transform_type == transform_options[2]: 
                    angle = st.slider(t("rotation_angle"), -180, 180, 0)
                    result = apply_rotation(image_array, angle)
                    st.image(result, use_container_width=True)
                    st.download_button(t("download_result"), convert_image_to_bytes(result), "rotated_image.png", "image/png")
                
                elif transform_type == transform_options[3]:  
                    shear_x = st.slider(t("shear_x"), -1.0, 1.0, 0.0, 0.1)
                    shear_y = st.slider(t("shear_y"), -1.0, 1.0, 0.0, 0.1)
                    result = apply_shearing(image_array, shear_x, shear_y)
                    st.image(result, use_container_width=True)
                    st.download_button(t("download_result"), convert_image_to_bytes(result), "sheared_image.png", "image/png")
                
                elif transform_type == transform_options[4]: 
                    axis_options = [t("reflect_x"), t("reflect_y"), t("reflect_origin")]
                    axis = st.radio(t("reflection_axis"), axis_options)
                    result = apply_reflection(image_array, axis)
                    st.image(result, use_container_width=True)
                    st.download_button(t("download_result"), convert_image_to_bytes(result), "reflected_image.png", "image/png")
        else:
            st.info(t("please_upload"))
    
    with tab2:
        st.markdown(f"### {t('image_filter')}")
        uploaded_file2 = st.file_uploader(t("upload_image"), type=["jpg", "jpeg", "png"], key="filter_upload")
        
        if uploaded_file2 is not None:
            image = Image.open(uploaded_file2)
            image_array = np.array(image)
            
            filter_options = [t("blur"), t("sharpen")]
            filter_type = st.selectbox(t("select_filter"), filter_options)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"**{t('original_image')}**")
                st.image(image, use_container_width=True)
            
            with col2:
                st.markdown(f"**{t('preview')}**")
                
                if filter_type == filter_options[0]:  
                    kernel_size = st.slider(t("kernel_size"), 3, 20, 5, 2)
                    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)
                    result = apply_convolution(image_array, kernel)
                    st.image(result, use_container_width=True)
                    st.markdown("**Average:**")
                    st.code(f"{kernel_size}x{kernel_size}")
                    st.download_button(t("download_result"), convert_image_to_bytes(result), "blurred_image.png", "image/png")
                
                elif filter_type == filter_options[1]:  
                    strength = st.slider(t("sharpen_strength"), 1, 5, 1)
                    kernel = np.array([[0, -1, 0], [-1, 4 + strength, -1], [0, -1, 0]], dtype=np.float32)
                    result = apply_convolution(image_array, kernel)
                    
                    st.markdown("---")
                    st.markdown(f"**{t('color_adjust')}**")
                    brightness = st.slider(t("brightness"), -100, 100, 0)
                    contrast = st.slider(t("contrast"), 0.5, 3.0, 1.0, 0.1)
                    saturation = st.slider(t("saturation"), 0.0, 2.0, 1.0, 0.1)
                    hue_shift = st.slider(t("hue_shift"), -180, 180, 0)
                    
                    result = adjust_color(result, brightness, contrast, saturation, hue_shift)
                    st.image(result, use_container_width=True)
                    st.markdown(f"**{t('sharpen')} Kernels:**")
                    st.code(str(kernel))
                    st.download_button(t("download_result"), convert_image_to_bytes(result), "sharpened_image.png", "image/png")
        else:
            st.info(t("please_upload"))
    
    with tab3:
        st.markdown(f"### {t('bg_removal')}")
        uploaded_file3 = st.file_uploader(t("upload_image"), type=["jpg", "jpeg", "png"], key="bg_upload")
        
        if uploaded_file3 is not None:
            image = Image.open(uploaded_file3)
            image_array = np.array(image)
            
            st.markdown(f"**{t('adjust_hsv')}**")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                h_min = st.slider(t("hue_min"), 0, 179, 0)
                s_min = st.slider(t("sat_min"), 0, 255, 0)
                v_min = st.slider(t("val_min"), 0, 255, 0)
            
            with col2:
                h_max = st.slider(t("hue_max"), 0, 179, 179)
                s_max = st.slider(t("sat_max"), 0, 255, 255)
                v_max = st.slider(t("val_max"), 0, 255, 255)
            
            lower_hsv = np.array([h_min, s_min, v_min])
            upper_hsv = np.array([h_max, s_max, v_max])
            result = remove_background_color(image_array, lower_hsv, upper_hsv)
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**{t('original_image')}**")
                st.image(image, use_container_width=True)
            
            with col2:
                st.markdown(f"**{t('preview')}**")
                st.image(result, use_container_width=True)
            
            st.download_button(t("download_result"), convert_image_to_bytes(result), "background_removed.png", "image/png", use_container_width=True)
            st.success(t("result_success"))
        else:
            st.info(t("please_upload"))
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button(t("back_home"), use_container_width=False):
        st.session_state.page = "Landing"
        st.rerun()


def about_page():
    render_language_selector()
    
    st.markdown(f'<h1 class="matrix-title" style="text-align: center;">👥 {t("about_us").upper()}</h1>', unsafe_allow_html=True)
    
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.markdown(f"### 🔍 {t('how_works')}")
    st.markdown(f"""
    <div class="content-text">
    {t('how_works_text')}
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.markdown(f"### 👨‍💻 {t('team_members')}")
    
    team_members = [
        {
            "name": "Sarah Aulya Fitri Ritonga",
            "role": t("leader"),
            "contribution": t("contrib_1"),
            "photo": "https://i.imgur.com/DanpIap.jpg",
            "photo_type": "url"
        },
        {
            "name": "Hevita Zhofany Putri",
            "role": t("backend"),
            "contribution": t("contrib_2"),
            "photo": "https://i.imgur.com/h0x8beF.jpg",
            "photo_type": "url"
        },
        {
            "name": "Mika Lusia Panjaitan",
            "role": t("frontend"),
            "contribution": t("contrib_3"),
            "photo": "https://i.imgur.com/eN7vaxi.jpg",
            "photo_type": "url"
        },
        {
            "name": "Ristia Angelina Purba",
            "role": t("docs"),
            "contribution": t("contrib_4"),
            "photo": "https://i.imgur.com/KarCzgS.jpg",
            "photo_type": "url"
        }
    ] 
    
    for i in range(0, len(team_members), 2):
        cols = st.columns(2)
        for j in range(2):
            if i + j < len(team_members):
                member = team_members[i + j]
                with cols[j]:
                    st.markdown('<div class="member-card">', unsafe_allow_html=True)
                    
                    if member['photo_type'] == "emoji":
                        st.markdown(f'<div class="member-photo-container"><div class="member-emoji-circle">{member["photo"]}</div></div>', unsafe_allow_html=True)
                    elif member['photo_type'] == "url":
                        st.markdown(f'<div class="member-photo-container"><img src="{member["photo"]}" class="member-photo-circle"></div>', unsafe_allow_html=True)
                    elif member['photo_type'] == "local":
                        try:
                            img = Image.open(member['photo'])
                            st.markdown('<div class="member-photo-container">', unsafe_allow_html=True)
                            st.image(img, width=150)
                            st.markdown('</div>', unsafe_allow_html=True)
                        except:
                            st.markdown('<div class="member-photo-container"><div class="member-emoji-circle">👤</div></div>', unsafe_allow_html=True)
                    
                    st.markdown(f"""
                        <h3 class="member-name">{member['name']}</h3>
                        <p class="member-role">{member['role']}</p>
                        <p class="member-contribution">{member['contribution']}</p>
                    </div>
                    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button(t("back_home"), use_container_width=False):
        st.session_state.page = "Landing"
        st.rerun()


if 'page' not in st.session_state:
    st.session_state.page = "Landing"

if st.session_state.page == "Landing":
    landing_page()
elif st.session_state.page == "Home":
    home_page()
elif st.session_state.page == "Features":
    features_page()
elif st.session_state.page == "About Us":
    about_page()
