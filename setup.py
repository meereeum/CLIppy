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
        'beautifulsoup4==4.6.0',
        'python-dateutil==2.6.1',
        'requests==2.20.0',
        'selenium==3.13.0'
    ],
)
