import os
import time
import glob
from shutil import copy2


def run(input_path, output_path, file_ext=['ORF', 'JPG']):
    """
    Copy files to destination folder, creating year, month, and day directories if not exist
    :param input_path: where the files are located
    :param output_path: base dir to copy the fiels to
    :param file_ext: list of files ext - default to ['ORF', 'JPG']
    :return: nothing
    """
    # get input photos paths
    photos_paths = [path for path in glob.glob(os.path.join(input_path, '*')) if path[-3:] in file_ext]

    for photo_path in photos_paths:

        photo_year = time.gmtime(os.path.getmtime(photo_path)).tm_year
        photo_month = time.gmtime(os.path.getmtime(photo_path)).tm_mon
        photo_day = time.gmtime(os.path.getmtime(photo_path)).tm_mday

        dest_path = os.path.join(output_path, str(photo_year), f'{photo_month:02}', f'{photo_day:02}')

        print(dest_path, os.path.basename(photo_path))

        if not os.path.isdir(dest_path):
            os.makedirs(dest_path)

        copy2(photo_path, dest_path)

