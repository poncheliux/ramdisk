# ramdisk
RamDisk is a library for creating and managing a RAM Disk in Python. It provides a simple interface for creating, writing, reading, and deleting data from a RAM Disk.

## Installation
To use the RamDisk library, you need to install it from the source files. Follow these steps:

1 - Download the Source Files: Ensure you have the source files for the RamDisk library on your local machine. You can download them from your GitHub repository.

2 - Navigate to the Project Directory: Open your terminal or command prompt and navigate to the directory where the source files are located. This directory should contain the setup.py file.
```python
cd path/to/your/project
```
3 -Install the Library: Run the following command to install the library using pip. This command tells pip to install the package defined in the current directory (denoted by .).

```python
pip install
```
This will install the RamDisk library so you can import and use it in your Python projects.

### Clone the Repository
1 - If your project is hosted on GitHub, you can clone it using git.
```python
git clone https://github.com/your_username/ramdisk.git
cd ramdisk
```
2 - Run the Installation Command: Once you are in the project directory, run:
```python
pip install
```

## Usage
### <img alt="Static Badge" src="https://img.shields.io/badge/-Importing_the_Lybrary-blue">
```python
# Import the RamDisk class from the core module
from ramdisk.core import RamDisk
```

### <img alt="Static Badge" src="https://img.shields.io/badge/-Creating_a_100_MB_RAM_Disk-blue">
```python
# Create a 100 MB RAM Disk
# The number 100 indicates the size of the RAM Disk in megabytes.
rd = RamDisk(100)
```

### <img alt="Static Badge" src="https://img.shields.io/badge/-Writing_Data-blue">
```python
# Write data to the RAM Disk
# b"Hello World" is the data to be written.
# 0 is the offset (position) in the RAM Disk where the data will be written.
rd.write(b"Hello World", 0)
```

### <img alt="Static Badge" src="https://img.shields.io/badge/-Reading_Data-blue">
```python
# Read data from the RAM Disk
# 11 is the number of bytes to read.
# 0 is the offset (position) in the RAM Disk from where to start reading.
print(rd.read(11, 0))  # Output: b'Hello World'
```

### <img alt="Static Badge" src="https://img.shields.io/badge/-Modifying_Data-blue">
```python
# Modify data in the RAM Disk
# b"Python" is the new data to be written.
# 6 is the offset (position) in the RAM Disk where the new data will be written,
# replacing part of the original data starting at the 6th byte.
rd.write(b"Python", 6)
print(rd.read(11, 0))  # Output: b'Hello Python'
```

### <img alt="Static Badge" src="https://img.shields.io/badge/-Deleting_Data-blue">
```python
# Delete data by overwriting with zeros (or other methods)
# b'\x00' * 11 creates a sequence of 11 zero bytes to overwrite the data.
# 0 is the offset (position) in the RAM Disk where the zero bytes will be written.
rd.write(b'\x00' * 11, 0)
print(rd.read(11, 0))  # Output: b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
```

### <img alt="Static Badge" src="https://img.shields.io/badge/-Closing_the_RAM_Disk-blue">
```python
# Close the RAM Disk to free up resources
rd.close()
```

## Contributing
Please read the CONTRIBUTING.md file for details on our code of conduct, and the process for submitting pull requests to us.

## Contact
If you have any questions or suggestions, you can contact me at ponchodx@gmail.com

## License
This project is licensed under the MIT License.
