import unittest
import sys

# test çalıştırıcı
if __name__ == "__main__":
    print("...Testler başlıyor...")
    
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern='test_*.py')
    runner = unittest.TextTestRunner(verbosity=2)  # ayrıntılı çıktı
    
    result = runner.run(suite)
    
    # sonuçları göster
    print(f"\n Toplam test sayısı: {result.testsRun}")
    
    if result.failures:
        print(f" Başarısız: {len(result.failures)}")
        for test, trace in result.failures:
            print(f"  - {test}")
    
    if result.errors:
        print(f" Hatalı: {len(result.errors)}")
        
    if result.wasSuccessful():
        print(" Tüm testler geçti!!!! ")
        sys.exit(0)
    else:
        print(" Bazı testler başarısız...")
        sys.exit(1)  # hata kodu dndür