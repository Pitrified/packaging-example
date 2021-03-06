import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-pitrified",
    version="0.0.1",
    author="Pitrified",
    author_email="author@example.com",
    description="A small example package, and some tests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pitrified/test-packaging",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
