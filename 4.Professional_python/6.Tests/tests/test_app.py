import unittest
import app


class TestApp(unittest.TestCase):

    def setUp(self):
        print('method setUp')

    def tearDown(self):
        print('method tearDown')

    def test_owner_name(self):
        self.assertEqual(app.get_doc_owner_name("11-2"), "Геннадий Покемонов")

    def test_get_doc_owner_name(self):
        self.assertEqual(app.get_doc_owner_name('2207 876234'), 'Василий Гупкин')

    def test_add_new_doc(self):
        self.assertEqual(app.add_new_doc('7311', 'pass', 'Shamil', 2), 2)

    def test_delete_doc(self):
        self.assertTrue(app.delete_doc('10006'))


if __name__ == '__main__':
    unittest.main()