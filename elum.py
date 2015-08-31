import sys

from elum.api import complete_me


def main():
    if len(sys.argv) < 4:
        print("Error. Please enter input_filename, output_filename, and your email address as arguments.")
        sys.exit(1)

    input_filename = sys.argv[1].strip()
    output_filename = sys.argv[2].strip()
    email = sys.argv[3].strip()
    with open(input_filename, 'r') as handle:
        contents = handle.readlines()

    complete_me(contents, output_filename, email)


if __name__ == "__main__":
    main()
