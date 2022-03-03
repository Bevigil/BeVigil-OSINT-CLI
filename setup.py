from setuptools import setup , find_packages

setup(
    name = "bevigil-cli" ,
    version = "1.0.0",
    packages = find_packages() ,
    entry_points = {
        "console_scripts" : [
            "bevigil-cli = bevigil.cli:main"
        ]
    }
)