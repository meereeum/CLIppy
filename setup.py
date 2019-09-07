import setuptools


setuptools.setup(
    name='CLIppy',
    version='0.0.0',
    url='https://github.com/meereeum/CLIppy',

    author='Miriam Shiffman',
    author_email='meereeum@gmail.com',

    description='your friendly Command Line Interface assistant',
    long_description=open('README.md').read(),

    packages=['CLIppy'],

    platforms='any',
    install_requires=[
        'beautifulsoup4>=4.8.0',
        'python-dateutil>=2.8.0',
        'requests>=2.22.0',
        'selenium>=3.141.0'
    ],
)
