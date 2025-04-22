from setuptools import setup, find_packages

setup(
    name="notpyvert",
    version="1.0.0",
    author="Okamitah",
    author_email="loneokami03@gmail.com",
    description="A tool to convert between Jupyter Notebooks (.ipynb) and Python scripts (.py).",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "notpyvert=notpyvert.main:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
