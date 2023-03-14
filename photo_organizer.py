import time
import os
import glob
from shutil import copy2


class Photo:
    def __init__(self, source_path):
        self.path = source_path

    @property
    def photo_year(self):
        return time.gmtime(os.path.getmtime(self.path)).tm_year

    @property
    def photo_month(self):
        return time.gmtime(os.path.getmtime(self.path)).tm_mon

    @property
    def photo_day(self):
        return time.gmtime(os.path.getmtime(self.path)).tm_mday


class PhotoCopier:
    FILE_TYPES = ('ORF', 'JPG')

    def __init__(self, source_dir, destination_dir):
        self.source_dir = source_dir
        self.destination_dir = destination_dir

    def destination_hierarchy_folder(self, photo: Photo):
        return os.path.join(self.destination_dir,
                            str(photo.photo_year),
                            f'{photo.photo_month:02}',
                            f'{photo.photo_day:02}')

    def photos_paths(self):
        return [path for path in glob.glob(os.path.join(self.source_dir, '*')) if path[-3:] in ('ORF', 'JPG')]

    @staticmethod
    def create_dir_if_not_exist(path):
        if not os.path.isdir(path):
            os.makedirs(path)

    def run(self):
        for photo_source_path in self.photos_paths():
            photo = Photo(photo_source_path)
            destination_path = self.destination_hierarchy_folder(photo)

            self.create_dir_if_not_exist(destination_path)

            copy2(photo_source_path, destination_path)


if __name__ == '__main__':
    source_dir = r'E:\DCIM\100OLYMP'
    destination_dir = ''

    photo_copier = PhotoCopier(source_dir, destination_dir)

    photo_copier.run()
