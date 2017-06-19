
from setuptools import setup, find_packages
from codecs import open
from os import path

'''
include_package_data
Accept all data files and directories matched by MANIFEST.in.

package_data
Specify additional patterns to match files and directories that may or may not be matched by MANIFEST.in or found in source control.

exclude_package_data
Specify patterns for data files and directories that should not be included when a package is installed, even if they would otherwise have been included due to the use of the preceding options.
'''

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="my-test-flask",
    author="frank",
    author_email="ashengfhs@163.com",
    version="0.1.0",
    description="a simple example use of flask.",
    long_description=long_description,
    packages=find_packages(),
    scripts=[],
    package_data={
        # Include txt file in any packages
        '': ['*.txt'],
        # Include data files under flaskr package
        'app': ['data/*.dat'],
        'app': ['static/*'],
        'app': ['template/*.html'],
        },
    # Exclude any README when install
    exclude_package_data={'': ['README.*']},
    install_requires=['flask>=0.12.2'],
)
