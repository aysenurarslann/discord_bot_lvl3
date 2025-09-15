import sqlite3
import os

# veritabanı dosyası
VERITABANI_ADI = "gorevler.db"

def veritabani_hazirla():
    
    if os.path.exists(VERITABANI_ADI):
        os.remove(VERITABANI_ADI)  # eski dosyayı sil

    baglanti = sqlite3.connect(VERITABANI_ADI)
    imleç = baglanti.cursor()
    
    # görevler tablosu
    imleç.execute('''
        CREATE TABLE gorevler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            aciklama TEXT NOT NULL,
            tamamlandi BOOLEAN NOT NULL DEFAULT 0,
            olusturma_tarihi TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    baglanti.commit()
    baglanti.close()
    print("******Veritabanı hazırlandı******")


def init_db():
    veritabani_hazirla()

def add_task(aciklama):
    
    conn = sqlite3.connect(VERITABANI_ADI)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO gorevler (aciklama) VALUES (?)", (aciklama,))
    gorev_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return gorev_id

def delete_task(gorev_id):
    
    baglanti = sqlite3.connect(VERITABANI_ADI)
    imleç = baglanti.cursor()
    imleç.execute("DELETE FROM gorevler WHERE id = ?", (gorev_id,))
    silindi_mi = imleç.rowcount > 0
    baglanti.commit()
    baglanti.close()
    return silindi_mi

def get_all_tasks():
   
    conn = sqlite3.connect(VERITABANI_ADI)
    cursor = conn.cursor()
    cursor.execute("SELECT id, aciklama, tamamlandi FROM gorevler ORDER BY id")
    gorevler = cursor.fetchall()
    conn.close()
    return gorevler

def complete_task(gorev_id):
    
    baglanti = sqlite3.connect(VERITABANI_ADI)
    imleç = baglanti.cursor()
    imleç.execute("UPDATE gorevler SET tamamlandi = 1 WHERE id = ?", (gorev_id,))
    guncellendi = imleç.rowcount > 0
    baglanti.commit()
    baglanti.close()
    return guncellendi
    