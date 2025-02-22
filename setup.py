from setuptools import setup, find_packages

setup(
    name='loghawk',  # Package name
    version='1.4',  # Version number
    author='Imane Ismail',  
    author_email='imane.fahmy@gmail.com', 
    description='A log analysis tool that detects anomalies in log files.',  # Short description
    long_description=open('README.md').read(),  # Read long description from README.md
    long_description_content_type='text/markdown',  # Markdown format for long description
    url='https://github.com/Imane-Ismail/LogHawk.git',  # Your GitHub repo link
    packages=find_packages(),  # Automatically find all packages
    install_requires=[
        'pyfiglet',  # For fancy ASCII art
        'pandas',  # For structured log analysis
        'colorama',  # For colored output in terminal
        're2',  # For fast regex matching (optional, use 'regex' if needed)
    ],

    entry_points={
        'console_scripts': [
            'loghawk = loghawk.cli:main',  # Links loghawk command to cli.py
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Adjust if using a different license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',  # Minimum Python version required
)
