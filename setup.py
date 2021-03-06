import setuptools


with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

with open("requirements.txt") as fin:
    REQUIRED_PACKAGES = fin.read()

setuptools.setup(
    name="cvds",
    version="0.0.1",
    author="geoyee",
    author_email="geoyee@yeah.net",
    description="Dataset statistical calculation.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/geoyee/datastate",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=REQUIRED_PACKAGES,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)