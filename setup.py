import os
from setuptools import setup, find_packages
 
version = '0.1'
 
description = "A project generator."
cur_dir = os.path.dirname(__file__)
try:
    long_description = open(os.path.join(cur_dir, 'README.md')).read()
except:
    long_description = description
 
setup(
    name = "slingshot",
    version = version,
    license = 'MIT',
    description = description,
    long_description = long_description,
    author = 'Zachary Carter',
    author_email = 'zack.carter@gmail.com',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
    entry_points="""
[console_scripts]
slingcli = slingshot.generator:main
""",
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ],
)
