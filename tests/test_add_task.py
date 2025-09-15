import unittest
from database import add_task, get_all_tasks

class TestGorevEkleme(unittest.TestCase):

    def setUp(self):
        from database import init_db
        init_db()

    def test_normal_gorev_ekleme(self):
        
        aciklama = "Market alışverişi"
        gorev_id = add_task(aciklama)
        gorevler = get_all_tasks()
        
        self.assertIsNotNone(gorev_id)
        self.assertEqual(len(gorevler), 1)
        self.assertEqual(gorevler[0][1], aciklama)
        self.assertFalse(gorevler[0][2])  # tamamlanmamış olmalı
        print(f"✓ Görev eklendi: ID {gorev_id}")

    def test_bos_gorev(self):
        
        gorev_id = add_task("")
        gorevler = get_all_tasks()
        
        self.assertEqual(len(gorevler), 1)
        self.assertEqual(gorevler[0][1], "")
        print(" Boş görev test edildi")

    def test_coklu_gorev(self):
       
        add_task("İlk görev")
        add_task("İkinci görev")
        gorevler = get_all_tasks()
        
        self.assertEqual(len(gorevler), 2)
        print(f" {len(gorevler)} görev eklendi")

if __name__ == "__main__":
    unittest.main() 
