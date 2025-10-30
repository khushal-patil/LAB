import os

# Clear the terminal screen
os.system("clear")

# Print welcome messages
os.system("echo File Recovery Script")
os.system("echo For Programming Wonders")

# List available storage devices
os.system("echo The list of devices is")
os.system("lsblk")  # List block devices to identify which one to use

# Prompt user to enter the device to be used for recovery
os.system("echo Enter the device to be used (e.g., /dev/sda1)")
devname = input("")  # Store the device name entered by the user

# Prompt user to enter the image name for storing the data from the device
imgname = input("Enter the image name \n")  # e.g., "recovery.img"

# Create a disk image of the specified device using the `dd` command
os.system("dd if=" + devname + " of=" + imgname + " bs=512")

# Show the inode numbers of files from the disk image using `fls`
os.system("echo Showing inode number of files")
os.system("fls " + imgname)

# Prompt user to enter the inode number of the deleted file for recovery
inodeno = input("Enter the inode of the deleted file: ")

# Display detailed information about the inode using `istat`
os.system("istat " + imgname + " " + inodeno)

# Print the contents of the recovered file using `icat`
os.system("echo The contents of the recovered file are")
os.system("icat " + imgname + " " + inodeno)

# Prompt user to enter the name of the file where the recovered data should be stored
os.system("echo Enter the name of the file where data will be stored (with extension)")
newfile = input("")  # Store the new file name

# Recover the file content and store it in the specified new file
os.system("icat " + imgname + " " + inodeno + " > " + newfile)

# Display the contents of the newly created file to verify recovery
os.system("echo The contents of the file are")
os.system("cat " + newfile)