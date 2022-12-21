import os

class ChangeDir:

    def __init__(self, set_dir):
        self.set_dir = set_dir
        self.first_dir = os.path.abspath(os.curdir)

    def __enter__(self):
        return os.chdir(self.set_dir)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(rf"{self.first_dir}")

with ChangeDir('dir1'):
    print(os.listdir())

with ChangeDir('dir2'):
    print(os.listdir())