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
    with open(file_path, "r") as original_file:
        content_lines = original_file.readlines()

    with open(f'new_file.ipynb', 'x') as new_file:
        for line in content_lines:
            new_file.writelines("{\n")
            for key, value in line_py_ipynb(line).items():
                new_file.writelines(f'{key}: {value},\n')
            new_file.writelines("},\n")
        



def line_py_ipynb(line):
    if line.startswith("#"):
        cell =  {
            '"cell_type"': '"markdown"',
            '"metadata"': {},
            '"source"': [
                f"{line}"
            ]
        }
    else:
        cell =   {
            '"cell_type"': '"code"',
            '"execution_count"': 1,
            '"metadata"': {},
            '"outputs"': [],
            '"source"': [
                f'{line}'
            ]
        }
    return cell



def handle_ipynb(filename):
    print(filename)

tail =  {
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3 (ipykernel)",
            "language": "python",
            "name": "myenv"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.13.2"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 5}



if __name__ == "__main__":
    main()

