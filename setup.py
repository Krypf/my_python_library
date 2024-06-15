from setuptools import setup, find_packages

setup(
    name="my_python_library",
    version="0.1",
    packages=find_packages(),
    install_requires=[],  # Add any dependencies here
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple example Python library",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/my_python_library",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
