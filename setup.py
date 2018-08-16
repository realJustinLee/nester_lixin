import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nester-lixin",
    version="1.0.7",
    author="Li Xin",
    author_email="JustinDellAadm@Live.com",
    description="A simple printer of nested lists",
    license="MIT License",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Great-Li-Xin/nester_lixin",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/Great-Li-Xin/nester_lixin/issues',
        'Source': 'https://github.com/Great-Li-Xin/nester_lixin',
    },
)
