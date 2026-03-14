from setuptools import setup, find_packages

setup(
    name="cybertoolkit",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "rich",
        "requests",
        "dnspython",
        "python-whois",
        "pyfiglet"
    ],
    entry_points={
        "console_scripts": [
            "cybertool=cybertoolkit.cli:run"
        ]
    }
)
