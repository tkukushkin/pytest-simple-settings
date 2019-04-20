import os

from setuptools import find_packages, setup


this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='pytest-simple-settings',
    version='0.1.1',
    author='Timofey Kukushkin',
    author_email='tima@kukushkin.me',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'pytest11': [
            'simple-settings = pytest_simple_settings._plugin',
        ],
    },
    install_requires=[
        'pytest',
        'simple-settings',
        'typing;python_version<"3"',
    ],
    extras_require={
        'test': [
            'pycodestyle',
            'pylint',
            'pytest-cov',
        ],
    },
)
