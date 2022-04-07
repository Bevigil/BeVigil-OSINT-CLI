import setuptools
import pathlib

HERE = pathlib.Path(__file__).parent
VERSION = "1.0.4"
PACKAGE_NAME = "bevigil-cli"
AUTHOR = "Bevigil"
AUTHOR_EMAIL = "bevigil@cloudsek.com"
URL = "https://osint.bevigil.com/"

LICENSE = "Apache License 2.0"
DESCRIPTION = "OSINT cli"
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

with open("requirements.txt") as f:
    INSTALL_REQUIRES = [line.rstrip() for line in f]

setuptools.setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "bevigil-cli = bevigil.cli:main"
        ]
    }
)
