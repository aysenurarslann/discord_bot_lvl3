import unittest
from database import add_task, get_all_tasks

class TestGorevListesi(unittest.TestCase):

    def setUp(self):
        from database import init_db
        init_db()

    def test_bos_liste(self):
        
        gorevler = get_all_tasks()
        self.assertEqual(len(gorevler), 0)
        print(" Boş liste kontrolü")

    def test_dolu_liste(self):
        
        add_task("Kitap oku")
        add_task("Spor yap")
        add_task("Kod yaz")
        
        gorevler = get_all_tasks()
        self.assertEqual(len(gorevler), 3)
        self.assertEqual(gorevler[0][1], "Kitap oku")
        print(f" {len(gorevler)} görev listelendi")

if __name__ == "__main__":
    unittest.main()
