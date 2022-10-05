import argparse
from os.path import exists

def validate_args(parser: argparse.ArgumentParser):
    parser.description = "A helper tool for pad, crop and convert media files." 
    parser.add_argument("-i", dest="input_file", type=str, required=True,
            help=r"Input file. e.g. 'C:\media\movie.mp4'.")
    parser.add_argument("-a", dest="action", choices=["crop", "pad"],
            required=True,
            help="Action. 'crop' or 'pad'.")
    
    args = parser.parse_args()
    assert exists(args.input_file), f"File not found! file='{args.file}'"
    return args


def pad():
    pass


def crop():
    pass


def main():
    parser = argparse.ArgumentParser()
    args = validate_args(parser)

    print(args.input_file)
    print(args.action)

if __name__ == "__main__":
    main()
