from setuptools import setup, find_packages


setup(

    name="loghawk",

    version="1.0",

    packages=find_packages(),

    install_requires=[],

    entry_points={

        "console_scripts": [

            "loghawk=loghawk_cli:main",

        ],

    },

    author="Imane Ismail",

    description="LogHawk - A log analysis tool for detecting anomalies",

    long_description=open("README.md").read(),

    long_description_content_type="text/markdown",

    url="https://github.com/Imane-Ismail/loghawk",

    classifiers=[

        "Programming Language :: Python :: 3",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

    ],

    python_requires=">=3.6",

)