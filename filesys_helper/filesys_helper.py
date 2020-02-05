import os


def valid_dir(directory):
    if not os.path.exists(root):
        print(f"Creating {root}")
        os.mkdir(root)
    full_path = root + directory
    if not os.path.exists(full_path):
        print(f"Creating {full_path}")
        os.mkdir(full_path)
    return full_path