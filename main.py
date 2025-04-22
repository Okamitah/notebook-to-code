import argparse as ap
import json
import os

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


def handle_py(file_path):
    print(f"Processing Python file: {file_path}")
    with open(file_path, "r") as original_file:
        content_lines = original_file.readlines()

    cells = []
    current_cell = {"cell_type": "code", "source": [], "metadata": {}, "outputs": []}
    for line in content_lines:
        stripped_line = line.rstrip("\n")  # Remove trailing newline for processing
        if stripped_line.startswith("#"):
            if current_cell["cell_type"] == "code" and current_cell["source"]:
                cells.append(current_cell)
                current_cell = {"cell_type": "markdown", "source": [], "metadata": {}}
            current_cell["source"].append(stripped_line[1:].strip() + "\n")  # Add newline back
        else:
            if current_cell["cell_type"] == "markdown" and current_cell["source"]:
                cells.append(current_cell)
                current_cell = {"cell_type": "code", "source": [], "metadata": {}, "outputs": []}
            current_cell["source"].append(line)  # Preserve newline character

    if current_cell["source"]:
        cells.append(current_cell)

    notebook = {
        "cells": cells,
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
        "nbformat_minor": 5
    }

    output_file = os.path.splitext(file_path)[0] + ".ipynb"
    with open(output_file, "w") as new_file:
        json.dump(notebook, new_file, indent=2)
    print(f"Converted to: {output_file}")


def handle_ipynb(file_path):
    print(f"Processing Jupyter Notebook: {file_path}")
    with open(file_path, "r") as ipynb_file:
        notebook = json.load(ipynb_file)

    py_code = []
    for cell in notebook.get("cells", []):
        if cell["cell_type"] == "code":
            py_code.extend(cell["source"])  # Source already contains \n
            py_code.append("\n")  # Add a blank line between cells
        elif cell["cell_type"] == "markdown":
            py_code.append("# " + "\n# ".join(cell["source"]))  # Convert markdown to comments
            py_code.append("\n")  # Add a blank line after markdown

    output_file = os.path.splitext(file_path)[0] + ".py"
    with open(output_file, "w") as py_file:
        py_file.writelines(py_code)
    print(f"Converted to: {output_file}")


if __name__ == "__main__":
    main()
