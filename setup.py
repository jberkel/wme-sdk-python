from setuptools import setup, find_packages

setup(
    name="wme-sdk-python",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "python-dotenv==1.0.1",
        "requests==2.32.3",
    ],
    extras_require={
        "dev": ["pytest"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)
