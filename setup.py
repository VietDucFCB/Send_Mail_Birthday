from setuptools import setup, find_packages

setup(
    name='birthday-email-sender',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'python-dotenv',
        'schedule', # Added schedule based on requirements.txt and planned usage
        # Flask and Flask-Mail are in requirements.txt but not directly used in the core script.
        # Add them here if they are indeed project dependencies.
        # 'Flask',
        # 'Flask-Mail',
    ],
    entry_points={
        'console_scripts': [
            'birthday-email-sender=main:main_cli', # Renaming main function for clarity if we add scheduling
        ],
    },
    python_requires='>=3.6',
)