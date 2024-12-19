import os
from setuptools import setup, find_packages

def parse_requirements(filename):

    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]
    else:
        print(f"Warning: {filename} not found. Using default dependencies.")
        return [
            "numpy>=1.21.0",
            "pandas>=1.3.0",
            "matplotlib>=3.4.0",
            "seaborn>=0.11.0",
        ]


requirements = parse_requirements("requirements.txt")

setup(
    name="carbsimulator",
    version="1.0.0",
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
)
