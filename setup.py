import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyDebug",
    version="0.0.1",
    author="Mat-Frayne",
    description="I'm Learning :)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mat-Frayne/PythonDebugger",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)