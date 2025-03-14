from setuptools import setup, find_packages

setup(
    name='standardizetaxa',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='Apache 2.0',
    description='standardize taxa using API of Global Names Verifier',
    long_description=open('README.md').read(),
    install_requires=['numpy', 'pandas', 'urllib3' , 'json'],
    url='https://github.com/petergpython/standardizeTaxa',
    author='Peter Giovannini',
    author_email='peter.giovannini@croptrust.org'
)