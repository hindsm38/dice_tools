import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dice_tools",
    version="1.0.0",
    author="Matthew Hinds",
    author_email="hinds.matt38@gmail.com",
    description="Tools for use with Lea in order to simulate dice rolls in tabletop games.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hindsm38/dice_tools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
