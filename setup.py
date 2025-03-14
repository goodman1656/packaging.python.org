from setuptools import setup, find_packages

setup(
    name="dormant_opener",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here
        # Example: 'requests',
    ],
    entry_points={
        'console_scripts': [
            'dormant-opener=app.main:main',
        ],
    },
)

# You can uncomment this if you need to import bitcoin for other purposes
# import bitcoin
