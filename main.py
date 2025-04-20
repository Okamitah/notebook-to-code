import argparse as ap

def main():
    parser = ap.ArgumentParser(
        prog='notpyvert',
        description='Convert from a Jupyter Noterbook to a python file, and viceversa',
    )
    parser.add_argument('filename')
    args = parser.parse_args()
    print(args.filename)

    if args.filename.endswith(".py"):
        handle_py(args.filename)
    elif args.filename.endswith(".ipynb"):
        handle_ipynb(args.filename)
    else:
        print("Unsupported file format. Please provide a .py or .ipynb file.")



def handle_py(file_path):
    print(f"Processing Python file: {file_path}")
    with open(file_path, "r") as file:
        content = file.readlines()

        print(content)


def handle_ipynb(filename):
    print(filename)

if __name__ == "__main__":
    main()

