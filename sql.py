import sqlite3

# Veritabanı oluştur / bağlan
conn = sqlite3.connect("meslekler.db")
cursor = conn.cursor()

# Tablo oluştur
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasarim_meslekler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    meslek TEXT NOT NULL,
    aciklama TEXT
)
""")
conn.commit()

# Tasarım kategorisinden meslekleri ekle
tasarim = [
    ("Grafik Tasarımcı", "Logolar, afişler, broşürler gibi görsel tasarımlar yapar."),
    ("UX/UI Tasarımcı", "Web ve mobil uygulamalarda kullanıcı deneyimi tasarlar."),
    ("Endüstriyel Tasarımcı", "Ürünlerin ergonomik ve estetik tasarımını yapar."),
    ("Moda Tasarımcısı", "Giyim ve aksesuar tasarımı yapar."),
    ("İç Mimar", "Mekan tasarımı ve dekorasyonu yapar."),
    ("Web Tasarımcı", "Web sitelerinin görsel ve işlevsel tasarımını yapar."),
    ("Animasyon Tasarımcısı", "2D/3D animasyonlar ve görsel efektler üretir."),
    ("Oyun Tasarımcısı", "Oyun dünyası ve karakter tasarımı yapar."),
    ("Endüstriyel Grafik Tasarımcı", "Ürün ambalaj ve reklam tasarımı yapar."),
    ("Tipografi Uzmanı", "Yazı ve font tasarımı üzerine çalışır."),
    ("Sahne ve Set Tasarımcısı", "Tiyatro, sinema ve etkinlikler için set tasarlar."),
    ("Fotoğrafçı", "Profesyonel fotoğraf çekimi ve düzenlemesi yapar."),
    ("Video Editörü", "Videoları kurgular ve görsel efektler ekler."),
    ("3D Modelleme Uzmanı", "3D objeler ve karakterler tasarlar."),
    ("Endüstriyel Ürün Tasarımcısı", "Fiziksel ürünlerin tasarımını yapar."),
    ("Ambalaj Tasarımcısı", "Ürün ambalajlarını tasarlar."),
    ("İllüstratör", "Çizim ve illüstrasyonlar üretir."),
    ("Motion Designer", "Hareketli grafikler ve animasyonlar tasarlar."),
    ("Dijital Sanatçı", "Bilgisayar tabanlı sanat ve konsept tasarımları yapar."),
    ("Serbest Tasarımcı / Freelancer", "Çeşitli tasarım projelerinde çalışır."),
    ("Moda Tasarımcısı", "Giyim ve aksesuar tasarımı yapar."),
]

cursor.execute("""
    CREATE TABLE IF NOT EXISTS programlama_meslekler (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        meslek TEXT NOT NULL,
        aciklama TEXT
    )
""")
conn.commit()

programlama = [
    ("Yazılım Geliştirici", "Uygulama ve yazılım programları geliştirir."),
    ("Web Geliştirici", "Web siteleri ve web uygulamaları oluşturur."),
    ("Mobil Uygulama Geliştirici", "iOS ve Android uygulamaları geliştirir."),
    ("Veri Bilimci", "Büyük veri setlerini analiz eder ve yorumlar."),
    ("Sistem Yöneticisi", "Bilgi teknolojisi altyapısını yönetir."),
    ("Oyun Geliştirici", "Video oyunları tasarlar ve programlar."), 
    ("Yapay Zeka Mühendisi", "AI ve makine öğrenimi modelleri geliştirir."),
    ("Veritabanı Yöneticisi", "Veritabanlarını tasarlar ve yönetir."),
    ("Siber Güvenlik Uzmanı", "Sistemlerin güvenliğini sağlar."),
    ("Bulut Mühendisi", "Bulut tabanlı çözümler geliştirir ve yönetir."),
    ("DevOps Mühendisi", "Yazılım geliştirme ve operasyon süreçlerini otomatikleştirir."),
    ("Full Stack Geliştirici", "Hem ön yüz hem de arka uç geliştirme yapar."),
    ("Front-End Geliştirici", "Kullanıcı arayüzü tasarımı ve geliştirmesi yapar."),
    ("Back-End Geliştirici", "Sunucu tarafı uygulamalarını geliştirir."),
    ("Ağ Mühendisi", "Bilgisayar ağlarını tasarlar ve yönetir."),
    ("Test Mühendisi", "Yazılım test süreçlerini yürütür ve otomatikleştirir."),
    ("ERP Geliştirici", "Kurumsal kaynak planlama sistemleri geliştirir."),
    ("Veri Mühendisi", "Veri altyapısını oluşturur ve yönetir."),
    ("Yazılım Mimarı", "Yazılım projelerinin mimarisini tasarlar."),
    ("Teknik Destek Uzmanı", "Kullanıcılara teknik destek sağlar.")
]

cursor.execute("""
    CREATE TABLE IF NOT EXISTS egitim_ogretim_meslekler (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        meslek TEXT NOT NULL,
        aciklama TEXT
    )
""")
conn.commit()

egitim_ogretim = [
    ("Öğretmen", "Okullarda çeşitli dersleri öğretir."),
    ("Eğitim Danışmanı", "Eğitim programları ve stratejileri geliştirir."),
    ("Rehber Öğretmen", "Öğrencilere rehberlik ve danışmanlık yapar."),
    ("Okul Müdürü", "Okulun yönetiminden sorumludur."), 
    ("Eğitim Teknoloğu", "Eğitimde teknoloji kullanımını optimize eder."),
    ("Dil Eğitmeni", "Yabancı dil öğretimi yapar."),
    ("Özel Eğitim Öğretmeni", "Özel gereksinimli öğrencilere eğitim verir."),
    ("Sınıf Öğretmeni", "İlkokul öğrencilerine temel dersleri öğretir."),
    ("Müzik Öğretmeni", "Müzik eğitimi verir ve öğrencileri yönlendirir."),
    ("Beden Eğitimi Öğretmeni", "Spor ve fiziksel eğitim programları uygular."),
    ("Sanat Öğretmeni", "Görsel sanatlar eğitimi verir."),
    ("Okul Psikoloğu", "Öğrencilerin psikolojik ihtiyaçlarını karşılar."),
    ("Eğitim Yöneticisi", "Eğitim kurumlarının yönetiminde görev alır."),
    ("Kariyer Danışmanı", "Öğrencilere kariyer planlamasında yardımcı olur."),
    ("Eğitim Araştırmacısı", "Eğitim yöntemleri ve politikaları üzerine araştırmalar yapar."),
    ("Çocuk Gelişimi Uzmanı", "Çocukların gelişim süreçlerini inceler ve destekler."),
    ("Dil ve Konuşma Terapisti", "Dil ve konuşma bozuklukları üzerine çalışır."),
    ("Eğitim İçerik Geliştiricisi", "Eğitim materyalleri ve içerikleri hazırlar."),
    ("Yükseköğretim Akademisyeni", "Üniversitelerde ders verir ve araştırma yapar."),
    ("E-Öğrenme Uzmanı", "Çevrimiçi eğitim programları tasarlar ve uygular.")
]

cursor.execute("""
    CREATE TABLE IF NOT EXISTS doktorluk_kategorisinden_meslekler (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        meslek TEXT NOT NULL,
        aciklama TEXT
    )
""")
conn.commit()

doktorluk_kategorisinden_meslekler = [
    ("Pratisyen Doktor", "Hastaların genel sağlık sorunlarını teşhis ve tedavi eder."),
    ("Cerrah", "Ameliyatlar yaparak hastalıkları tedavi eder."),
    ("Pediatrist", "Çocukların sağlık sorunlarıyla ilgilenir."),
    ("Dahiliye Uzmanı", "Yetişkin hastaların iç hastalıklarını tedavi eder."),
    ("Kardiyolog", "Kalp ve dolaşım sistemi hastalıklarını teşhis ve tedavi eder."),
    ("Nörolog", "Sinir sistemi hastalıklarıyla ilgilenir."),
    ("Ortopedist", "Kas-iskelet sistemi hastalıklarını tedavi eder."),
    ("Psikiyatrist", "Zihinsel sağlık sorunlarını teşhis ve tedavi eder."),
    ("Dermatolog", "Cilt hastalıklarıyla ilgilenir."),
    ("Göz Doktoru (Oftalmolog)", "Göz ve görme sorunlarını tedavi eder."),
    ("Kulak Burun Boğaz Uzmanı (KBB)", "Kulak, burun ve boğaz hastalıklarını tedavi eder."),
    ("Radyolog", "Tıbbi görüntüleme teknikleri kullanarak teşhis koyar."),
    ("Anestezi Uzmanı", "Ameliyatlarda anestezi uygular ve yönetir."),
    ("Onkolog", "Kanser hastalıklarının teşhis ve tedavisini yapar."),
    ("Endokrinolog", "Hormon ve bezlerle ilgili hastalıkları tedavi eder."),
    ("Gastroenterolog", "Sindirim sistemi hastalıklarıyla ilgilenir."),
    ("Ürolog", "Üriner sistem ve erkek üreme organları hastalıklarını tedavi eder."),
    ("Fizyoterapist", "Hareket ve fonksiyon bozukluklarını tedavi eder."),
    ("Aile Hekimi", "Bireylerin ve ailelerin genel sağlık ihtiyaçlarını karşılar."),
    ("İmmünolog", "Bağışıklık sistemi hastalıklarıyla ilgilenir.")
]

cursor.execute("""
    CREATE TABLE IF NOT EXISTS muhendislik_kategorisinden_meslekler (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        meslek TEXT NOT NULL,
        aciklama TEXT
    )
""")
conn.commit()

muhendislik_kategorisinden_meslekler = [  
    ("Makine Mühendisi", "Makine ve mekanik sistemlerin tasarımı ve üretimi ile ilgilenir."),
    ("Elektrik Mühendisi", "Elektrik sistemleri ve elektronik cihazların tasarımı ile ilgilenir."),
    ("İnşaat Mühendisi", "Binalar, köprüler ve altyapı projelerinin tasarımı ve inşası ile ilgilenir."),
    ("Bilgisayar Mühendisi", "Bilgisayar donanımı ve yazılımı geliştirme ile ilgilenir."),
    ("Endüstri Mühendisi", "Üretim süreçlerinin optimizasyonu ve verimliliği ile ilgilenir."),
    ("Çevre Mühendisi", "Çevresel sorunların çözümü ve sürdürülebilirlik ile ilgilenir."),
    ("Kimya Mühendisi", "Kimyasal süreçlerin tasarımı ve üretimi ile ilgilenir."),
    ("Havacılık ve Uzay Mühendisi", "Uçak ve uzay araçlarının tasarımı ve geliştirilmesi ile ilgilenir."),
    ("Petrol Mühendisi", "Petrol ve doğal gaz çıkarma süreçleri ile ilgilenir."),
    ("Yazılım Mühendisi", "Yazılım sistemlerinin tasarımı, geliştirilmesi ve bakımı ile ilgilenir."),
    ("Telekomünikasyon Mühendisi", "İletişim sistemleri ve ağlarının tasarımı ile ilgilenir."),
    ("Otomotiv Mühendisi", "Araç tasarımı, üretimi ve performans iyileştirmeleri ile ilgilenir."),
    ("Biyomedikal Mühendisi", "Tıbbi cihazların tasarımı ve geliştirilmesi ile ilgilenir."),
    ("Nükleer Mühendis", "Nükleer enerji üretimi ve güvenliği ile ilgilenir."),
    ("Malzeme Mühendisi", "Yeni malzemelerin geliştirilmesi ve uygulanması ile ilgilenir."),
    ("Robotik Mühendisi", "Robot sistemlerinin tasarımı ve geliştirilmesi ile ilgilenir."),
    ("Enerji Mühendisi", "Enerji üretimi, dağıtımı ve verimliliği ile ilgilenir."),
    ("Yapı Mühendisi", "Yapıların dayanıklılığı ve güvenliği ile ilgilenir."),
    ("Denizcilik Mühendisi", "Gemi tasarımı, inşası ve bakımı ile ilgilenir."),
    ("Jeoteknik Mühendisi", "Toprak ve kaya mekaniği üzerine çalışır.")
]

cursor.execute("""
    CREATE TABLE IF NOT EXISTS sanat_meslekleri (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        meslek TEXT NOT NULL,
        aciklama TEXT
    )
""")
conn.commit()

sanat_meslekleri = [
    ("Resim Sanatçısı", "Çeşitli tekniklerle resimler yapar."),
    ("Heykeltraş", "Farklı malzemelerden heykeller yapar."),
    ("Moda Tasarımcısı", "Giyim ve aksesuar tasarımı yapar."),
    ("Müzisyen", "Müzik besteler ve performans sergiler."),
    ("Tiyatro Sanatçısı", "Tiyatro oyunlarında rol alır ve sahne performansı sergiler."),
    ("Dansçı", "Farklı dans türlerinde performans sergiler."),
    ("Yazar", "Edebiyat eserleri yazar ve yayınlar."),
    ("Film Yönetmeni", "Film projelerini yönetir ve yönlendirir."),
    ("Animatör", "Animasyon filmleri ve görsel efektler üretir."),
    ("Sahne Tasarımcısı", "Tiyatro ve etkinlikler için sahne tasarımı yapar."),
    ("Küratör", "Sanat galerileri ve müzelerde sergiler düzenler."),
    ("Sanat Terapisti", "Sanat yoluyla terapi hizmeti sunar."),
    ("Dijital Sanatçı", "Bilgisayar tabanlı sanat ve konsept tasarımları yapar."),
    ("Seramik Sanatçısı", "Seramik objeler ve sanat eserleri üretir."),
    ("Endüstriyel Tasarımcı", "Ürünlerin ergonomik ve estetik tasarımını yapar."),
    ("Oyuncu", "Film, dizi ve tiyatro projelerinde rol alır."),
]

# Verileri tabloya ekle
cursor.executemany("INSERT INTO tasarim_meslekler (meslek, aciklama) VALUES (?, ?)", tasarim)
cursor.executemany("INSERT INTO programlama_meslekler (meslek, aciklama) VALUES (?, ?)", programlama)
cursor.executemany("INSERT INTO egitim_ogretim_meslekler (meslek, aciklama) VALUES (?, ?)", egitim_ogretim)
cursor.executemany("INSERT INTO doktorluk_kategorisinden_meslekler (meslek, aciklama) VALUES (?, ?)", doktorluk_kategorisinden_meslekler)
cursor.executemany("INSERT INTO muhendislik_kategorisinden_meslekler (meslek, aciklama) VALUES (?, ?)", muhendislik_kategorisinden_meslekler)
cursor.executemany("INSERT INTO sanat_meslekleri (meslek, aciklama) VALUES (?, ?)", sanat_meslekleri)
conn.commit()
# Veritabanını kapat
conn.close()