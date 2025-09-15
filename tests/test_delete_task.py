import unittest
from database import add_task, delete_task, get_all_tasks

class TestGorevSilme(unittest.TestCase):

    def setUp(self):
        from database import init_db
        init_db()
        # test verileri hazırla
        add_task("Silinecek görev")
        add_task("Kalacak görev")

    def test_gorev_silme(self):
        
        gorevler = get_all_tasks()
        silinecek_id = gorevler[0][0]
        
        sonuc = delete_task(silinecek_id)
        kalan_gorevler = get_all_tasks()
        
        self.assertTrue(sonuc)
        self.assertEqual(len(kalan_gorevler), 1)
        print(f" Görev {silinecek_id} silindi")

    def test_olmayan_gorev_silme(self):
        
        sonuc = delete_task(9999)
        self.assertFalse(sonuc)
        print(" Olmayan görev silme testi")

if __name__ == "__main__":
    unittest.main()

