from setuptools import setup, find_packages

setup(
    name="netanalyzer",
    version="1.0.0",
    author="Aqib Shakeel",
    description="A powerful network traffic analysis tool",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "netanalyzer=cli:main",
        ]
    },
    install_requires=[
        "scapy",
    ],
)
