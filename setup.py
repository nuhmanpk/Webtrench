import pathlib
import setuptools

file = pathlib.Path(__file__).parent

README = (file / "README.md").read_text()

setuptools.setup(
    name="Webtrench",
    version="0.1.01",
    author="Nuhman Pk",
    author_email="nuhmanpk7@gmail.com",
    long_description = README,
    long_description_content_type = "text/markdown",
    description="A powerful and easy-to-use web scrapper for collecting data from the web. Supports scraping of images, text, videos, meta data, and more. Ideal for machine learning and deep learning engineers. Download and extract data with just one line of code",
    license="MIT",
    url="https://github.com/nuhmanpk/Webtrench",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(include=['Webtrench']),  
    install_requires=[
        'bs4',
        'requests',
    ],
    
    python_requires=">=3.6",
    
)
