#!/usr/bin/env python3
import argparse
import cowsay

def main():
    #get supported animals from cowsay.char_names
    animals = cowsay.char_names

    parser = argparse.ArgumentParser(
        description="Make animals say things"
    )
    parser.add_argument(
        "message",
        nargs="+",
        help="The message to say."
    )
    parser.add_argument(
        "--animal",
        choices=animals,
        default="cow",
        help="The animal to be saying things."
    )
    args = parser.parse_args()

    text = " ".join(args.message)

    # Print using cowsay.get_output_string
    output = cowsay.get_output_string(args.animal, text)
    print(output)

if __name__ == "__main__":
    main()