from photo_organizer import Photo, PhotoCopier
import unittest
import shutil
import os


class TestPhoto(unittest.TestCase):
    def setUp(self) -> None:
        self.photo = Photo(r'tests\test_input\test_photo.orf')

    def test_year(self):
        self.assertEqual(self.photo.photo_year, 2023)


    def test_day(self):
        self.assertEqual(self.photo.photo_month, 3)

    def test_day(self):
        self.assertEqual(self.photo.photo_day, 3)


class TestPhotoCopier(unittest.TestCase):

    def setUp(self) -> None:
        self.test_input_path = r'tests\test_input'
        self.test_output_path = r'tests\test_output'

        os.mkdir(self.test_output_path)

        self.photo_copier = PhotoCopier(source_dir='test_output', destination_dir=r'test_data_output')

    def tearDown(self) -> None:
        shutil.rmtree(r'tests\test_output')


    def test_destination_hierarchy_folder(self):
        pass

    def test_photos_paths
        pass

    def test_create_dir_if_not_exist
        pass

    def test_run
        pass

