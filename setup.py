import re
from setuptools import setup, find_packages


def get_version_and_author(package):
    with open(package + '/__init__.py', 'r') as f:
        init_py = f.read()
    version = re.search(r"__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)
    author = re.search(r"__author__ = ['\"]([^'\"]+)['\"]", init_py).group(1)
    return version, author


version, author = get_version_and_author('ml-utils')

setup(
    name='ml-utils',
    version=version,
    packages=find_packages(),
    install_requires=[
        'numpy'
    ],
    url='https://github.com/ygonzal3/ml-utils',
    author=author,
    author_email='ygonzalez112@gmail.com',
    description='ML helper classes',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
