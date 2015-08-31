import sys

from elum.api import complete_me


def main():
    if len(sys.argv) < 3:
        print("Error. Please enter filename an your email address as arguments.")
        sys.exit(1)

    filename = sys.argv[1].strip()
    email = sys.argv[2].strip()
    with open(filename, 'r') as handle:
        contents = handle.readlines()

    result_string = complete_me(contents, email)
    print(result_string)


if __name__ == "__main__":
    main()
