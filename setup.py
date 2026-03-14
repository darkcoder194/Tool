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
        "pyfiglet",
        "psutil",
        "SpeechRecognition"
    ],
    entry_points={
        "console_scripts": [
            "cybertool=cybertoolkit.cli:start_cli"
        ]
    }
)
