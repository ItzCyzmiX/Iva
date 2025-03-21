from setuptools import setup, find_packages
from pathlib import Path

# Read README with proper encoding
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="iva-generator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "langchain",
        "langchain-community",
        "langchain-groq",
        "python-dotenv",
        "pydantic",
        "rich"
    ],
    entry_points={
        "console_scripts": [
            "iva=src.cli:main",
        ],
    },
    author="ItzCyzmiX",
    author_email="itzmedigamingx@gmail.com",
    description="AI Code Assistant",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ItzCyzmiX/Iva",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)