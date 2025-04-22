import argparse as ap
from notpyvert.utils import handle_ipynb, handle_py

def main():
    parser = ap.ArgumentParser(
        prog='notpyvert',
        description='Convert from a Jupyter Notebook to a Python file, and vice versa.',
    )
    parser.add_argument('filename', help='Path to the .py or .ipynb file.')
    args = parser.parse_args()

    if args.filename.endswith(".py"):
        handle_py(args.filename)
    elif args.filename.endswith(".ipynb"):
        handle_ipynb(args.filename)
    else:
        print("Unsupported file format. Please provide a .py or .ipynb file.")




if __name__ == "__main__":
    main()
