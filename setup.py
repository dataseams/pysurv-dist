"""The package setup script."""
from setuptools import find_packages, setup

import requirements

setup(
    name="pysurv-dist",
    version="0.1",
    description="Logic for the pysurv-dist project.",
    author="Dodd, Jacob; Mourad, Sam",
    author_email="jacobdodd94@gmail.com;mouradhsam@gmail.com",
    python_requires=">=3.10",
    packages=find_packages(exclude=["tests", "docs"]),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Business Users",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    include_package_data=False,
    zip_safe=False,
    install_requires=requirements.get(["#prod"]),
)
