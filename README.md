# Discord Görev Yönetim Botu

Bu Discord botu ekip görevlerini yönetmek için yazıldı. Basit komutlarla görev ekleme, silme ve takip etme imkanı sağlar.

## Özellikler
- Görev ekleme: !add_task <açıklama>
- Görev silme: !delete_task <görev_id>
- Görevleri görüntüleme: !show_tasks
- Görev tamamlama: !complete_task <görev_id>

Tüm görevler SQLite veritabanında saklanır.

## Kurulum ve Başlatma

### Gereksinimler
- Python 3.8 veya üzeri
- Discord bot tokeni

### Adım 1: Bağımlılıkları yükle
```
pip install -r requirements.txt
```

### Adım 2: Bot tokenini ayarla
Windows için:
```
$env:DISCORD_BOT_TOKEN = "tokenin_buraya"
```


### Adım 3: Botu başlat
```
python bot.py
```

## Testleri Çalıştırma
```
python run_tests.py
```

## Bot Token Alma
1. Discord Developer Portal'a git (https://discord.com/developers/applications)
2. New Application butonuna tıkla
3. Bot sekmesine geç
4. Add Bot butonuna tıkla
5. Token kısmından bot tokenini kopyala

## Kullanım
Bot çalıştıktan sonra Discord sunucunuzda aşağıdaki komutları kullanabilirsiniz:

- !add_task Proje sunumunu hazırla
- !show_tasks
- !complete_task 1
- !delete_task 2
