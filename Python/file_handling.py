from importlib.resources import path
import pathlib

home=pathlib.Path.home()
current_dir=pathlib.Path.cwd()
path=pathlib.Path("C:\Python Practice\File Handling")
p=home / "abc.txt"
# print(p)
# print(list(current_dir.parents))
for dir in current_dir.parents:
    print(dir)