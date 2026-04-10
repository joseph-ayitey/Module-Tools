import argparse

parser = argparse.ArgumentParser(prog="cat", description="Prints the output of a file to the console")
parser.add_argument("-n", "--number", help="Displays the lines along with their number", action="store_true")
parser.add_argument("-b", "--nonblank", help="Displays the lines along with their number skipping the blank lines", action="store_true")
parser.add_argument("path", help="The file path", nargs="+")

args = parser.parse_args()

show_lines = args.number
non_blank = args.nonblank

if show_lines == True and non_blank == True:
    print("Error: Cannot use -n and -b together. Please use only one flag at a time.")
    exit()

text = ""
i = 1

for file in args.path:
    with open(file, 'r') as f:  # Use 'with' for proper file handling
        text += f.read()

text_list = text.split("\n")

if text_list[-1] == "":
    text_list.pop()

if (show_lines == False and non_blank == False):
    print("\n".join(text_list))
    exit()

for line in text_list:
    if non_blank == True and line == "":
        print("")  # Print blank line without number
    else:
        print(f"     {i} {line}")
        i += 1