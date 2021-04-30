import os
import shutil

def _convert_bytes(size_in_bytes, unit='MiB'):
    if unit == 'KiB':
        size = round((size_in_bytes/1024), 2)
    elif unit == 'MiB':
        size = round(size_in_bytes/(1024*1024), 2)
    elif unit == 'GiB':
        size = round(size_in_bytes/(1024*1024*1024), 2)
    elif unit == 'TiB':
        size = round(size_in_bytes/(1024*1024*1024*1024), 2)

    return size

def _copy_file(source, destination, not_tree):
    if not_tree:
        shutil.copy(source, destination)

    elif not not_tree:
        tmp_source = source
        if tmp_source.endswith('\\') or tmp_source.endswith('/'):
            tmp_source = tmp_source[:-1]
        if tmp_source.startswith('\\') or tmp_source.startswith('/'):
            tmp_source = tmp_source[1:]

        full_path_destination = os.path.join(destination, os.path.dirname(tmp_source))
        os.makedirs(full_path_destination, exist_ok=True)
        shutil.copy(source , full_path_destination)