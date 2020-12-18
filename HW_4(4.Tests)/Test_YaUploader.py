from YaUploader import YaUploader
import unittest

TOKEN = ''


class TestYaUploader(unittest.TestCase):

    def setUp(self):
        self.user = YaUploader(TOKEN)
        self.user.del_dir('test/')

    def test_200_mk_dir(self):
        self.user.mk_dir('test/')
        self.assertEqual(self.user.check_dir('test/'), 200)

    def test_400_mk_dir(self):
        self.assertEqual(self.user.mk_dir(''), 400)

    def test_404_check_dir(self):
        self.assertEqual(self.user.check_dir('test/'), 404)

    def tearDown(self):
        self.user.del_dir('test/')


if __name__ == '__main__':

    unittest.main()
