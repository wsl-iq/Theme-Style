from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="AscallArtCLI",
    version="1.1.1",
    packages=find_packages(),
    include_package_data=True,
    description="Short description here",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Mohammed Al-Baqer",
    url="https://pypi.org/project/AscallArtCLI/",
    license="MIT",   
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)



