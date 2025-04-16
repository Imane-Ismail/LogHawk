from setuptools import setup, find_packages

setup(
    name='loghawk',
    version='1.4',
    author='Imane Ismail',
    author_email='imane.fahmy@gmail.com',
    description='A log analysis tool that detects anomalies in log files.',
    long_description="Lightweight log analysis CLI tool for detecting suspicious activity in system logs.",
    long_description_content_type='text/markdown',
    url='https://github.com/Imane-Ismail/LogHawk.git',
    packages=find_packages(),
    install_requires=[
        'pyfiglet',
        'pandas',
        'colorama',
        'regex',
    ],
    entry_points={
        'console_scripts': [
            'loghawk = loghawk.loghawk_cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
