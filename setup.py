from setuptools import setup, find_packages

setup(
    name='ramdisk',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'mmap',
    ],
    author='Alfonso Aguero Villalobos',
    author_email='mx5700.org',
    description='A library for creating and managing a RAM Disk in Python.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Ponchelius/ramdisk',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)