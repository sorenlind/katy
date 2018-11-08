"""Setup script for package."""
import re
from setuptools import setup, find_packages

VERSION = re.search(r'^VERSION\s*=\s*"(.*)"', open("katy/version.py").read(), re.M).group(1)
with open("README.md", "rb") as f:
    LONG_DESCRIPTION = f.read().decode("utf-8")

setup(
    name="katy",
    version=VERSION,
    description="Simple tool for language detection using TextCat algorithm.",
    long_description=LONG_DESCRIPTION,
    author="Soren Lind Kristiansen",
    author_email="sorenlind@mac.com",
    url="https://github.com/sorenlind/katy/",
    packages=find_packages(),
    install_requires=['regex', 'cleanliness'],
    extras_require={
        'dev': ['pycodestyle', 'pydocstyle', 'pylint', 'yapf', 'rope', 'mypy'],
        'notebooks': ['jupyter', 'tqdm'],
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    classifiers=[
        'Development Status :: 3 - Alpha', 'Intended Audience :: Developers', 'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License', 'Natural Language :: Danish', 'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing :: Linguistic'
    ])
