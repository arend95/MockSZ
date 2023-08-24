import os
import pathlib

from setuptools import setup

setup(
    name='MockSZ',
    license="MIT",
    version='0.0.2',
    author="Arend Moerman",
    install_requires = ["numpy", "matplotlib", "scipy"],
    package_dir = {'': 'src'},
    packages=['MockSZ'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)

