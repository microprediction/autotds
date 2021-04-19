import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="autotds",
    version="0.0.4",
    description="Generate Towards Data Science (TDS) quality articles",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/microprediction/autotds",
    author="microprediction",
    author_email="pcotton@intechinvestments.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["autotds"],
    test_suite='pytest',
    tests_require=['pytest'],
    include_package_data=True,
    install_requires=["wheel", "pathlib", "numpy>=1.19.5", "importlib-metadata>=1.7.0", "getjson"],
    entry_points={
        "console_scripts": [
            "autotds=autotds.__main__:main",
        ]
    },
)
