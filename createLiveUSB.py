import os
import getpass 

print("Creating a Live USB...")
print("WARNING: Make sure USB is formatted!")
isoFile = input("Enter the path to the ISO file: ")

os.system("diskutil list")
USBnum = input("Enter the number at the end of the USB path: ")

username = getpass.getuser()

os.system("rm /Users/" + username + "/.youCanDeleteThis.dmg")
os.system("hdiutil convert -format UDRW -o ~/.youCanDeleteThis " + isoFile)
os.system("diskutil unmountDisk /dev/disk" + USBnum)
print("WARNING: FLASHING USB. This may take a few minutes. Please be patient!")
os.system("sudo dd if=/Users/" + username + "/.youCanDeleteThis.dmg of=/dev/rdisk" + USBnum + " bs=1m")
