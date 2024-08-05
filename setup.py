from setuptools import setup, find_packages

setup(
    name="py_thumbpad",
    version="0.1.0",
    author="Kerodekroma",
    author_email="kerodekroma@gmail.com",
    description="",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/kerodekroma/py_thumbpad",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)