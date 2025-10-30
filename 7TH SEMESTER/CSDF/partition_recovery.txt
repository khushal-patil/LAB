import os

# Print script information
print("Partition Recovery Script")

# List the devices attached to the system using 'lsblk'
print("List of devices attached to the system:")
os.system("lsblk")

# Prompt user to enter the device name
devname = input("Enter the device name (e.g., sda):\n")

# Show the list of partitions using 'fdisk' command
# The 'p' option in 'fdisk' prints the partition table, and 'q' quits without making changes
commandline = 'echo -e "p\nq\n" | sudo fdisk /dev/' + devname
print("Showing partition table:")
os.system(commandline)

# Prompt user to enter the partition number to recover
pno = input("Enter the partition number to recover:\n")

# Use 'fdisk' to delete the selected partition
# 'n' creates a new partition, 'pno' specifies the partition number, and 'w' writes the changes
commandline = 'echo -e "n\n\n' + pno + '\n\n\nw\n" | sudo fdisk /dev/' + devname
os.system(commandline)

# Confirm partition recovery process is complete
print("Partition recovery complete.")