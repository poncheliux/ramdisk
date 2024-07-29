import mmap
import os

class RamDisk:
    """
    A class to create and manage a RAM Disk using a file mapped into memory.
    
    Attributes:
        size_mb (int): Size of the RAM Disk in megabytes.
        file_name (str): Name of the temporary file used for the RAM Disk.
        mm (mmap.mmap): Memory-mapped file object.
    """

    def __init__(self, size_mb, file_name="memory.tmp"):
        """
        Initializes the RAM Disk.
        
        Parameters:
            size_mb (int): Size of the RAM Disk in megabytes.
            file_name (str): Name of the temporary file used for the RAM Disk.
        """
        self.size_mb = size_mb
        self.file_name = file_name
        self.mm = None
        self._create_memory_file()
        self._map_memory_file()

    def _create_memory_file(self):
        """Creates a temporary file of the specified size for the RAM Disk."""
        with open(self.file_name, "wb") as f:
            f.write(b'\x00' * (self.size_mb * 1024 * 1024))

    def _map_memory_file(self):
        """Maps the temporary file into memory."""
        with open(self.file_name, "r+b") as f:
            self.mm = mmap.mmap(f.fileno(), self.size_mb * 1024 * 1024)

    def write(self, data, offset=0):
        """
        Writes data to the RAM Disk at the specified offset.
        
        Parameters:
            data (bytes): Data to be written to the RAM Disk.
            offset (int): Position in bytes from the start of the RAM Disk where data will be written.
        """
        self.mm[offset:offset + len(data)] = data

    def read(self, size, offset=0):
        """
        Reads data from the RAM Disk starting at the specified offset.
        
        Parameters:
            size (int): Number of bytes to read.
            offset (int): Position in bytes from the start of the RAM Disk where reading will begin.
            
        Returns:
            bytes: The data read from the RAM Disk.
        """
        return self.mm[offset:offset + size]

    def close(self):
        """
        Closes the RAM Disk and removes the temporary file.
        """
        self.mm.close()
        os.remove(self.file_name)