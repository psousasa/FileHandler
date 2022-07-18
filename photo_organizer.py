import os
import time
import glob
from shutil import copy2


def photo_date(path: str) -> tuple:
    timestamp = time.gmtime(os.path.getmtime(path))
    return timestamp.tm_year, timestamp.tm_mon, timestamp.tm_mday


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

        photo_year, photo_month, photo_day = photo_date(input_path)

        destination_path = os.path.join(output_path, str(photo_year), f'{photo_month:02}', f'{photo_day:02}')

        if not os.path.isdir(destination_path):
            os.makedirs(destination_path)
        else:
            destination_photo_path = os.path.join(destination_path, os.path.basename(photo_path))
            if os.path.isdir(destination_photo_path):
                continue

        copy2(photo_path, destination_path)


