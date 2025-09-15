import unittest
from database import add_task, complete_task, get_all_tasks

class TestGorevTamamlama(unittest.TestCase):

    def setUp(self):
        from database import init_db
        init_db()
        add_task("Python projesi bitir")

    def test_gorev_tamamlama(self):
        
        gorevler = get_all_tasks()
        gorev_id = gorevler[0][0]
        
        sonuc = complete_task(gorev_id)
        guncellenmis = get_all_tasks()
        
        self.assertTrue(sonuc)
        self.assertTrue(guncellenmis[0][2])  # tamamlandı mı?
        print(f" Görev {gorev_id} tamamlandı")

    def test_olmayan_gorev_tamamlama(self):
        
        sonuc = complete_task(777)
        self.assertFalse(sonuc)

if __name__ == "__main__":
    unittest.main()
