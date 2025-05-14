from setuptools import setup, find_packages

setup(
    name="calculator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pytest>=8.3.5",
        "pytest-cov>=6.1.1",
        "coverage>=7.8.0",
    ],
)
