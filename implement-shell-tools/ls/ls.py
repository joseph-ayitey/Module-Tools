import argparse
from os import listdir, path

parser = argparse.ArgumentParser(prog="ls", description="List directory contents. Ignore files and directories starting with a '.' by default")
parser.add_argument("-1", "--one", dest="one", help="List one file per line.", action="store_true")
parser.add_argument("-a", "--all", dest="all", help="Do not ignore hidden files.", action="store_true")
parser.add_argument("path", help="The directory path (optional).", default=".", nargs="?")

args = parser.parse_args()

path_arg = args.path
show_hidden = args.all
one_per_line = args.one

# Error handling for invalid paths
if not path.exists(path_arg):
    print(f"ls: cannot access '{path_arg}': No such file or directory")
    exit(1)
if not path.isdir(path_arg):
    print(f"ls: cannot access '{path_arg}': Not a directory")
    exit(1)

try:
    contents = listdir(path_arg)
except PermissionError:
    print(f"ls: cannot open directory '{path_arg}': Permission denied")
    exit(1)

# To filter hidden files
if not show_hidden:
    contents = [f for f in contents if not f.startswith(".")]
# If show_hidden is True, keep all files (no filter is needed)

contents.sort()

# Output
if not contents:
    pass  # Print nothing for empty result
elif one_per_line:
    print("\n".join(contents))
else:
    print("  ".join(contents))