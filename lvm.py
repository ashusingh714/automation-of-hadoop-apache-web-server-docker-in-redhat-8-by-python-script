#!/usr/bin/python3



import subprocess as sp
import cgi
import os
wl = True
while True:
	os.system("clear")
	os.system("tput setaf 10")
	os.system("figlet -t -k LVM Menu")
	print("""
 Press:-
 1.To know The amount of disk space that is free on file systems.
 2.For formating the hard disk.
 3.For making new directory.
 4.For Creating Physical Volume.
 5.To watch Physical Volume.
 6.To create Volume Group.
 7.To watch Volume Group.
 8.For create Logical Volume.
 9.For watch Logical Volume.
 10.For watch all Logical Volume
 11.For Mount partition.
 12.For extend partition.
 13.For see how much hard disk you have.
 14.To Exit.""")	
	ch=int(input("Enter Your Choice:-"))	
	os.system("tput setaf 7")        
	if ch == 1: 		
		os.system("df -hT")
		inter = input("do you want to continue on LVM  menu  [y/N]:\t")
		if inter != 'y' and inter!= 'Y':
			exit()

	elif ch == 2: 		
		format1=input("Enter your partition name :")
		os.system("mkfs.ext4 "+format1)	
		inter = input("do you want to continue on LVM  menu  [y/N]:\t")
		if inter != 'y' and inter!= 'Y':
			exit()
	
	elif ch == 3: 		
		name=input("name your directory :")
		os.system("mkdir /"+name)
		inter = input("do you want to continue on LVM  menu  [y/N]:\t")
		if inter != 'y' and inter!= 'Y':
			exit()

	elif ch == 4: 		
		name1=input("name your physical volume :")
		os.system("pvcreate "+name1)
		inter = input("do you want to continue on LVM  menu  [y/N]:\t")
		if inter != 'y' and inter!= 'Y':
			exit()

	elif ch == 5: 		
		name2=input("name your physical volume :")
		os.system("pvdisplay "+name2)
		inter = input("do you want to continue on LVM  menu  [y/N]:\t")
		if inter != 'y' and inter!= 'Y':
			exit()

	elif ch == 6:
		j=int(input("how many pv you have : "))
		x=" "
		for i in range(j):
			pvs=input("Enter your P.V. name : ")
			x=x+" "+pvs
		print(x)
		nameofvg=input("Enter Your vg name")
		os.system("vgcreate "+nameofvg+" "+x)
		inter = input("do you want to continue on LVM  menu  [y/N]:\t")
		if inter != 'y' and inter!= 'Y':
			exit()
	
	elif ch == 7:
		name3=input("Enter your vg name : ")
		os.system("vgdisplay "+name3)	
		inter = input("do you want to continue on LVM  menu  [y/N]:\t")
		if inter != 'y' and inter!= 'Y':
			exit()

	elif ch == 8:
		lvname=input("Enter your lv name : ")
		size=input("Enter your size : ")
		vgname=input("Enter your vg name : ")
		os.system("lvcreate --size "+size+" --name "+lvname+" "+vgname)
		inter = input("do you want to continue on LVM  menu  [y/N]:\t")
		if inter != 'y' and inter!= 'Y':
			exit()

	elif ch == 9:
		lvname=input("Enter your vg name : ")
		os.system("lvdisplay "+lvname)
		inter = input("do you want to continue on LVM  menu  [y/N]:\t")
		if inter != 'y' and inter!= 'Y':
			exit()

	elif ch == 10:
		os.system("lvdisplay")
		inter = input("do you want to continue on LVM  menu  [y/N]:\t")
		if inter != 'y' and inter!= 'Y':
			exit()

	elif ch == 11:
		vgname=input("Enter your Volume group name : ")
		lvname=input("Enter your Partition name : ")
		dname=input("Enter your Directory name : ")
		os.system("mount /dev/"+vgname+"/"+lvname+" /"+dname)
		inter = input("do you want to continue on LVM  menu  [y/N]:\t")
		if inter != 'y' and inter!= 'Y':
			exit()

	elif ch == 12:
		vgname=input("Enter your Volume group name : ")
		lvname=input("Enter your Partition name : ")
		size=input("Enter your Extend Size : ")
		os.system("lvextend --size +"+size+" /dev/"+vgname+"/"+lvname)
		inter = input("do you want to continue on LVM  menu  [y/N]:\t")
		if inter != 'y' and inter!= 'Y':
			exit()

	elif ch == 13:
		os.system("fdisk -l")
		inter = input("do you want to continue on LVM  menu  [y/N]:\t")
		if inter != 'y' and inter!= 'Y':
			exit()

	elif ch == 14:
		exit()

