#!/usr/bin/python3

import os 
import fileinput
import getpass
import subprocess
import os
import getpass


os.system("tput setaf 11")
os.system("clear")
print("\t\t\tWelcome to the Automation Menu")
print("\t\t\t--------------------------------------")
os.system("\n\t\t\t figlet -t -k Automation Menu\n\n")
os.system("tput setaf 7")
password = getpass.getpass("Enter your password to use this Automation Menu: \t")

if password != "lw":
	print("password incorrect")
	exit()




def lvm():
  while True:
    os.system("clear")
    os.system("tput setaf 11")
    os.system("\t\t\tfiglet -t -k LVM Menu")
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
            break

    elif ch == 2:       
        format1=input("Enter your partition name :")
        os.system("mkfs.ext4 "+format1) 
        inter = input("do you want to continue on LVM  menu  [y/N]:\t")
        if inter != 'y' and inter!= 'Y':
            break
    
    elif ch == 3:       
        name=input("name your directory :")
        os.system("mkdir /"+name)
        inter = input("do you want to continue on LVM  menu  [y/N]:\t")
        if inter != 'y' and inter!= 'Y':
            break

    elif ch == 4:       
        name1=input("name your physical volume :")
        os.system("pvcreate "+name1)
        inter = input("do you want to continue on LVM  menu  [y/N]:\t")
        if inter != 'y' and inter!= 'Y':
            break

    elif ch == 5:       
        name2=input("name your physical volume :")
        os.system("pvdisplay "+name2)
        inter = input("do you want to continue on LVM  menu  [y/N]:\t")
        if inter != 'y' and inter!= 'Y':
            break

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
            break
    
    elif ch == 7:
        name3=input("Enter your vg name : ")
        os.system("vgdisplay "+name3)   
        inter = input("do you want to continue on LVM  menu  [y/N]:\t")
        if inter != 'y' and inter!= 'Y':
            break

    elif ch == 8:
        lvname=input("Enter your lv name : ")
        size=input("Enter your size : ")
        vgname=input("Enter your vg name : ")
        os.system("lvcreate --size "+size+" --name "+lvname+" "+vgname)
        inter = input("do you want to continue on LVM  menu  [y/N]:\t")
        if inter != 'y' and inter!= 'Y':
            break

    elif ch == 9:
        lvname=input("Enter your vg name : ")
        os.system("lvdisplay "+lvname)
        inter = input("do you want to continue on LVM  menu  [y/N]:\t")
        if inter != 'y' and inter!= 'Y':
            break

    elif ch == 10:
        os.system("lvdisplay")
        inter = input("do you want to continue on LVM  menu  [y/N]:\t")
        if inter != 'y' and inter!= 'Y':
            break

    elif ch == 11:
        vgname=input("Enter your Volume group name : ")
        lvname=input("Enter your Partition name : ")
        dname=input("Enter your Directory name : ")
        os.system("mount /dev/"+vgname+"/"+lvname+" /"+dname)
        inter = input("do you want to continue on LVM  menu  [y/N]:\t")
        if inter != 'y' and inter!= 'Y':
            break

    elif ch == 12:
        vgname=input("Enter your Volume group name : ")
        lvname=input("Enter your Partition name : ")
        size=input("Enter your Extend Size : ")
        os.system("lvextend --size +"+size+" /dev/"+vgname+"/"+lvname)
        inter = input("do you want to continue on LVM  menu  [y/N]:\t")
        if inter != 'y' and inter!= 'Y':
            break

    elif ch == 13:
        os.system("fdisk -l")
        inter = input("do you want to continue on LVM  menu  [y/N]:\t")
        if inter != 'y' and inter!= 'Y':
            break

    elif ch == 14:
        break



def aws():
    while True:
        os.system("clear")
        os.system("tput setaf 11")
        os.system("\t\t\tfiglet -t -k aws")
        print("press 1: For installing the aws cli software")
        print("Press 2; For creating user of aws cli by providing aws iam user")
        print("press 3: to create key pair")
        print("press 4: to Create a security group with port 22 and 80  ")
        print("press 5: To describe aws instances")
        print("press 6: to Launch an instance using the created key pair and security group.")
        print("press 7: to Create an EBS volume of 1 GB")
        print("press 8: to attach the above created EBS volume to the instance you created in the previous steps.")
        print("press 9: to create a s3 bucket")
        print("press 10: to upload object to the bucket")
        print("press 11: to Launch a Cloudfront with origin as the s3 bucket")
        print("press 12: To go back to main menu")
        aws_input = int(input("Enter your choise:\t"))
        os.system("tput setaf 7")

        if aws_input == 1:
                    os.system("curl 'https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip' -o 'awscliv2.zip'")
                    os.system("unzip awscliv2.zip")
                    os.system("sudo ./aws/install")
                    os.system("aws --version")
                    inter = input("do you want to continue on aws menu [y/N]:\t")
                    if inter != 'y' and inter!= 'Y':
                          break

        elif aws_input == 2:
                    name = input("provide name to the aws user:\t")
                    os.system("aws configure --profile  {}".format(name))
                    os.system("aws configure list-profiles")
                    inter = input("do you want to continue on aws menu [y/N]:\t")
                    if inter != 'y' and inter!= 'Y':
                         break

        elif aws_input == 3:
            key_name=input("enter the key name you want:\t")
            os.system("aws ec2 create-key-pair --key-name {} ".format(key_name) )
            inter = input("do you want to continue on aws menu [y/N]:\t")
            if inter != 'y' and inter!= 'Y':
                 break

        elif aws_input == 4:
                    securitygrp_name=input("enter the securiy group name:\t")
                    ports = input("which port you want to allow:\t")
                    os.system("aws ec2 create-security-group --description 'allow {}  ports' --group-name {}".format(ports, securitygrp_name ))
                    port_no = int(input("How many port you want to allow for ingress:\t"))
                    for i in range(port_no):
                           port = input("Enter the port :\t")
                           os.system("aws ec2 authorize-security-group-ingress --group-name {} --protocol 'tcp' --port {} --cidr '0.0.0.0/0'".format(securitygrp_name, port))
                    inter = input("do you want to continue on aws menu [y/N]:\t")
                    if inter != 'y' and inter!= 'Y':
                          break

        elif aws_input == 5:
                    os.system("aws ec2  describe-instances")
                    inter = input("do you want to continue on aws menu [y/N]:\t")
                    if inter != 'y' and inter!= 'Y':
                          break

        elif aws_input == 6:
                  
                    sg_id=input("please give securiy group id :\t")
                    key_name=input("please enter the key name :.\t")
                    print("Please select the image you want to launch\n 1. Amazon Linux AMi\n 2.Redhat Linux\n 3. Windows")
                    image_choice = int(input("Enter your choice:\t"))
                    images_avail = ["ami-0e306788ff2473ccb","ami-052c08d70def0ac62","ami-0b2f6494ff0b07a0e"] 
                    image_launch = images_avail[image_choice-1]
                    cout = input("How many os you want to launch:\t")
                    os.system("aws ec2 run-instances --image-id {} --instance-type t2.micro  --count {} --key-name {} --security-group-ids {}".format(image_launch,cout,key_name,sg_id))
                    inter = input("do you want to continue on aws menu [y/N]:\t")
                    if inter != 'y' and inter!= 'Y':
                          break

        elif aws_input == 7:
                    os.system("aws ec2 create-volume --availability-zone ap-south-1b --size 1 --volume-type gp2")
                    inter = input("do you want to continue on aws menu [y/N]:\t")
                    if inter != 'y' and inter!= 'Y':
                          break

        elif aws_input == 8:
                    instance_id=input("please give instance id:")
                    vol_id=input("please give volume id :\t")
                    os.system("aws ec2 attach-volume --device /dev/sdh --instance-id {} --volume-id {}".format(instance_id,vol_id))
                    inter = input("do you want to continue on aws menu [y/N]:\t")
                    if inter != 'y' and inter!= 'Y':
                          break

        elif aws_input == 9:
            bucket_name=input("please give an identical bucket name:\t")
            os.system("aws s3api create-bucket --bucket {} --region ap-south-1 --acl public-read --create-bucket-configuration LocationConstraint=ap-south-1".format(bucket_name))
            inter = input("do you want to continue on aws menu [y/N]:\t")
            if inter != 'y' and inter!= 'Y':
                 break 

        elif aws_input == 10:
            print("Available s3 bucket: " )
            os.system("aws s3 ls")
            bucket_name=input("please give bucket name where you want to upload the object:\t")
            object_name=input("please give the full path of the file which you want to upload:\t")
            os.system("aws s3 cp {} s3://{}/".format(object_name,bucket_name))
            inter = input("do you want to continue on aws menu [y/N]:\t")
            if inter != 'y' and inter!= 'Y':
                 break

        elif aws_input == 11:
            bucket_name=input("buket name for cloudfront:\t")
            os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com".format(bucket_name))
            inter = input("do you want to continue on aws menu [y/N]:\t")
            if inter != 'y' and inter!= 'Y':
                 break

        elif aws_input == 12:
             break



def hadoop():
  while True:
    os.system("clear")
    os.system("tput setaf 11")
    os.system("\t\t\tfiglet -t -k Hadoop  cluster")
    print("""
    1. Installing Hadoop.
    2. Creating Master in hadoop cluster.
    3. Creating Datanode in hadoop cluster.
    4. Creating Client in hadoop cluster.
    5. Limit The Data Node Storage.
    6. Upload data into the hadoop cluster.
    7. Read Data from Hadoop Cluster.
    8. List all the files.
    9. Delete Client Data.
    10. Stop Name Node.
    11. Stop Data Node.
    12. Converting the role of local system in the hadoop cluster.
    13. To go back to the main menu""")
    choice_hadoop = int(input("give your choice:\t"))
    os.system("tput setaf 7")
    if choice_hadoop == 1:
          print("""
press 1: For installing hadoop locally
press 2: For installing hadoop remotely 
""")
          insta = int(input("Enter you choice:\t"))
          if  insta == 1:
              os.system("rpm -ivh /root/jdk-8u171-linux-x64.rpm ")
              os.system("rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm  --force")
              print("\nHadoop Requirements Sucessfully Installed")
          elif insta == 2:
              sip = input("Enter the ip in which you want to install hadoop:\t")
              os.system('scp  /root/jdk-8u171-linux-x64.rpm  {}:/root/'.format(sip))
              os.system('scp  /root/hadoop-1.2.1-1.x86_64.rpm {}:/root/'.format(sip))
              os.system("ssh {} rpm -ivh /root/jdk-8u171-linux-x64.rpm ".format(sip))
              os.system("ssh {} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm  --force".format(sip))
              print("\nHadoop Requirements Sucessfully Installed")
          i = input("do you want to continue on Hadoop menu [y/N]:\t")
          if i != 'y' and i!= 'Y':
                    break


    elif choice_hadoop == 2:
          print("press 1 : For making the local system Namenode")
          print("press 2 : For making Datanode by ssh")
          datan = int(input("Enter your choice:\t"))
          if datan == 1:
                 add_master()
          elif datan == 2:
           sip = input("Enter Name Node IP : \t")
           sshd = input("Enter your Data Node directory name : \t")
           os.system("ssh {} mkdir {}".format(sip,sshd))
           print("Configuring hdfs-site.xml file ............")
           os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/hdfs-site.xml")
           os.system("echo -e '\n<!-- Put site-specific property overrides in this file. -->' >> /root/hdfs-site.xml")
           os.system('echo -e "\n<configuration>" >> /root/hdfs-site.xml')
           os.system('echo -e "\n<property>" >> /root/hdfs-site.xml')
           os.system('echo -e "\n<name>dfs.name.dir</name>" >> /root/hdfs-site.xml')
           os.system('echo -e "\n<value>{}</value>" >> /root/hdfs-site.xml'.format(sshd))
           os.system('echo -e "\n</property>" >> /root/hdfs-site.xml')
           os.system('echo -e "\n</configuration>" >> /root/hdfs-site.xml')
           os.system('scp  /root/hdfs-site.xml  {}:/etc/hadoop/'.format(sip))
           os.system('rm -rf /root/hdfs-site.xml')
           print("\nFormatting the Name Node ..............................")
           os.system('ssh {} hadoop namenode -format'.format(sip))
           nip = input("Enter  IP of which you want to start your hadoop master:")
           print("\t\t\t\tConfiguring core-site.xml file ...........")
           os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/core-site.xml")
           os.system('echo -e "\n<!-- Put site-specific property overrides in this file. -->" >> /root/core-site.xml')
           os.system('echo -e "\n<configuration>" >> /root/core-site.xml')
           os.system('echo -e "\n<property>" >> /root/core-site.xml')
           os.system('echo -e "\n<name>fs.default.name</name>" >> /root/core-site.xml')
           os.system('echo -e "\n<value>hdfs://{}:9001</value>" >> /root/core-site.xml'.format(nip))
           os.system('echo -e "\n</property>" >> /root/core-site.xml')
           os.system('echo -e "\n</configuration>" >> /root/core-site.xml')
           os.system('scp  /root/core-site.xml  {}:/etc/hadoop/'.format(sip))
           os.system('rm -rf /root/core-site.xml')
           os.system("ssh {} hadoop-daemon.sh start namenode".format(sip))
           print("Now the hadoop master servicee start you can check it by jps command")
           print("ssh {} jps".format(sip))
                 
          i = input("do you want to continue on Hadoop menu [y/N]:\t")
          if i != 'y' and i!= 'Y':
                    break

    elif choice_hadoop == 3:
          print("press 1 : For making the local system Datanode")
          print("press 2 : For making Datanode by ssh")
          datan = int(input("Enter your choice:\t"))
          if datan == 1:
                 add_slave()
          elif datan == 2:
           sip = input("Enter Data Node IP : \t")
           sshd = input("Create Data Node directory name remotely : \t")
           os.system("ssh {} mkdir {}".format(sip,sshd))
           print("Configuring hdfs-site.xml file ............")
           os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/hdfs-site.xml")
           os.system("echo -e '\n<!-- Put site-specific property overrides in this file. -->' >> /root/hdfs-site.xml")
           os.system('echo -e "\n<configuration>" >> /root/hdfs-site.xml')
           os.system('echo -e "\n<property>" >> /root/hdfs-site.xml')
           os.system('echo -e "\n<name>dfs.data.dir</name>" >> /root/hdfs-site.xml')
           os.system('echo -e "\n<value>{}</value>" >> /root/hdfs-site.xml'.format(sshd))
           os.system('echo -e "\n</property>" >> /root/hdfs-site.xml')
           os.system('echo -e "\n</configuration>" >> /root/hdfs-site.xml')
           os.system('scp  /root/hdfs-site.xml  {}:/etc/hadoop/'.format(sip))
           os.system('rm -rf /root/hdfs-site.xml')
           nip = input("Enter Name Node IP :")
           print("\t\t\t\tConfiguring core-site.xml file ...........")
           os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/core-site.xml")
           os.system('echo -e "\n<!-- Put site-specific property overrides in this file. -->" >> /root/core-site.xml')
           os.system('echo -e "\n<configuration>" >> /root/core-site.xml')
           os.system('echo -e "\n<property>" >> /root/core-site.xml')
           os.system('echo -e "\n<name>fs.default.name</name>" >> /root/core-site.xml')
           os.system('echo -e "\n<value>hdfs://{}:9001</value>" >> /root/core-site.xml'.format(nip))
           os.system('echo -e "\n</property>" >> /root/core-site.xml')
           os.system('echo -e "\n</configuration>" >> /root/core-site.xml')
           os.system('scp  /root/core-site.xml  {}:/etc/hadoop/'.format(sip))
           os.system('rm -rf /root/core-site.xml')
           os.system("ssh {} hadoop-daemon.sh start datanode".format(sip))
           print("Now the hadoop slave services start you can check it by jps command")
           os.system("ssh {} jps".format(sip))
          i = input("do you want to continue on Hadoop menu [y/N]:\t")
          if i != 'y' and i!= 'Y':
                    break

    elif choice_hadoop == 4:
          print("press 1 : For making the local system Client")
          print("press 2 : For making Client by ssh")
          datan = int(input("Enter your choice:\t"))
          if datan == 1:
                 add_client()
          elif datan == 2:
           sip = input("Enter Client IP : \t")
           nip = input("Enter Name Node IP : ")
           print("\tConfiguring core-site.xml file ...........")
           ip = input("\n\tEnter Client IP : ")
           os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/core-site.xml")
           os.system('echo -e "\n<!-- Put site-specific property overrides in this file. -->" >> /root/core-site.xml')
           os.system('echo -e "\n<configuration>" >> /root/core-site.xml')
           os.system('echo -e "\n<property>" >> /root/core-site.xml')
           os.system('echo -e "\n<name>fs.default.name</name>" >> /root/core-site.xml')
           os.system('echo -e "\n<value>hdfs://{}:9001</value>" >> /root/core-site.xml'.format(nip))
           os.system('echo -e "\n</property>" >> /root/core-site.xml')
           os.system('echo -e "\n</configuration>" >> /root/core-site.xml')
           os.system('scp  /root/core-site.xml  {}:/etc/hadoop'.format(sip))
           print("\tHadoop Client Sucessfully Configured.........")

          i = input("do you want to continue on Hadoop menu [y/N]:\t")
          if i != 'y' and i!= 'Y':
                    break

    elif choice_hadoop == 5:
          print("press 1 : For making the local system Client")
          print("press 2 : For making Client by ssh")
          datan = int(input("Enter your choice:\t"))
          if datan == 1:
           si = input("Do You want to extend/reduce Data Node Storage? : ")
           if si == "extend":
               os.system('df -hT')
               ex = input("How much you want to extend? : ")
               vg = input("Enter Your Volume Group Name : ")
               lv = input("Enter Your Logical Volume Name : ")
               os.system('lvextend --size {} /dev/{}/{}'.format( ex , vg , lv))
               print("\tSucessfully Extended the  Data Node Storage ")
               os.system('resize2fs  /dev/{}/{}'.format( vg ,lv))
               print("--------------------------------------------------")
               os.system('df -hT')
           elif si == "reduce":
               os.system(' df -hT')
               ex = input("How much you want to reduce? : ")
               vg = input("Enter Your Volume Group Name : ")
               lv = input("Enter Your Logical Volume Name : ")
               os.system('lvextend --size {} /dev/{}/{}'.format( ex , vg , lv))
               print("\tSucessfully Reduced Data Node Storage ")
               os.system('resize2fs  /dev/{}/{}'.format( vg ,lv))
               print("--------------------------------------------------")
               os.system('df -hT')
          elif datan == 2:
           ip = input("Enter Data Node IP : \t")
           si = input("\n\tDo You want to extend/reduce Data Node Storage? : \t")
           if si == "extend":
               os.system('ssh {} df -hT'.format(ip))
               ex = input("How much you want to extend? : ")
               vg = input("Enter Your Volume Group Name : ")
               lv = input("Enter Your Logical Volume Name : ")
               os.system('ssh {} lvextend --size {} /dev/{}/{}'.format(ip , ex , vg , lv))
               print("\tSucessfully Extended the  Data Node Storage ")
               os.system('ssh {} resize2fs  /dev/{}/{}'.format(ip , vg ,lv))
               print("--------------------------------------------------")
               os.system('ssh {} df -hT'.format(ip))
           elif si == "reduce":
               os.system('ssh {} df -hT'.format(ip))
               ex = input("How much you want to reduce? : ")
               vg = input("Enter Your Volume Group Name : ")
               lv = input("Enter Your Logical Volume Name : ")
               os.system('ssh {} lvextend --size {} /dev/{}/{}'.format(ip , ex , vg , lv))
               print("\tSucessfully Reduced Data Node Storage ")
               os.system('ssh {} resize2fs  /dev/{}/{}'.format(ip , vg ,lv))
               print("------------------------------------------------------------")
               os.system('ssh {} df -hT'.format(ip))
          i = input("do you want to continue on Hadoop menu [y/N]:\t")
          if i != 'y' and i!= 'Y':
                    break

    elif choice_hadoop == 6:
          print("press 1 : For uploading data to hadoop cluster if the local system is Client ")
          print("press 2 : For uploading data to hadoop cluster if remote system is Client ")
          datan = int(input("Enter your choice:\t"))
          if datan == 1:
                 filez = input("Enter the file name which you want to upload:\t")
                 os.system("hadoop fs -put {} /".format(filez))
          elif datan == 2:
                 sip = input("Enter the ip of the Client:\t")
                 filez = input("Enter the file name which you want to upload:\t")
                 os.system("ssh {} hadoop fs -put {} /".format(sip,filez))
          i = input("do you want to continue on Hadoop menu [y/N]:\t")
          if i != 'y' and i!= 'Y':
                    break

    elif choice_hadoop == 7:
          print("""
                press 1 : For read data to hadoop cluster if local system  is client
                press 2 : For read data to hadoop cluster if remote system is Client """)
          datan = int(input("Enter your choice:\t"))
          if datan == 1:
                 os.system("hadoop fs -ls / ")
                 filez = input("Enter the file name which you want to read:\t")
                 os.system("hadoop fs -cat  /{}".format(filez))
          elif datan == 2:
                 sip = input("Enter the ip of the Client:\t")
                 os.system("ssh {} hadoop fs -ls / ".format(sip))
                 filez = input("Enter the file name which you want to read:\t")
                 os.system("ssh {} hadoop fs -cat /{}".format(sip,filez))
          i = input("do you want to continue on Hadoop menu [y/N]:\t")
          if i != 'y' and i!= 'Y':
                    break

    elif choice_hadoop == 8:
          print("""
                press 1 : For list all data to hadoop cluster in local system 
                press 2 : For list all data to hadoop cluster in remote system  """)
          datan = int(input("Enter your choice:\t"))
          if datan == 1:
                 os.system("hadoop fs -ls / ")

          elif datan == 2:
                 sip = input("Enter the ip of the Client:\t")
                 os.system("ssh {} hadoop fs -ls / ".format(sip))
          i = input("do you want to continue on Hadoop menu [y/N]:\t")
          if i != 'y' and i!= 'Y':
                    break

    elif choice_hadoop == 9:
          print("""
                press 1 : For deleting a file from hadoop cluster in local system 
                press 2 : For deleting a file from hadoop cluster in remote system  """)
          datan = int(input("Enter your choice:\t"))
          if datan == 1:
                 os.system("hadoop fs -ls / ")
                 filez = input("Enter the file which you want to delete:\t")
                 os.system("hadoop fs -rm /{} ".format(filez))

          elif datan == 2:
                 sip = input("Enter the ip of the Client node:\t")
                 os.system("ssh {} hadoop fs -ls / ".format(sip))
                 filez = input("Enter the file which you want to delete:\t")
                 os.system("ssh {} hadoop fs -rm /{} ".format(sip.filez))
          i = input("do you want to continue on Hadoop menu [y/N]:\t")
          if i != 'y' and i!= 'Y':
                    break
    elif choice_hadoop == 10:
          print("""
                press 1 : For stopping Namenode of the hadoop cluster  locally 
                press 2 : For stopping Namenode of the hadoop cluster remotelly  """)
          datan = int(input("Enter your choice:\t"))
          if datan == 1:
                os.system("hadoop-daemon.sh stop namenode")
                os.system("jps")
                print("\t \t Namenode stopped successfully ........")
          elif datan == 2:
                sip = input("Enter the ip of the Namenode:\t")
                os.system("ssh {} hadoop-daemon.sh stop namenode".format(sip))
                os.system("ssh {} jps".format(sip))
                print("\t \t Namenode stopped successfully ........")
          i = input("do you want to continue on Hadoop menu [y/N]:\t")
          if i != 'y' and i!= 'Y':
                    break

    elif choice_hadoop == 11:
          print("""
                press 1 : For stopping Datanode of the hadoop cluster  locally 
                press 2 : For stopping Datanode of the hadoop cluster remotelly  """)
          datan = int(input("Enter your choice:\t"))
          if datan == 1:
                os.system("hadoop-daemon.sh stop datanode")
                os.system("jps")
                print("\t \t Datanode stopped successfully ........")
          elif datan == 2:
                sip = input("Enter the ip of the Datanode:\t")
                os.system("ssh {} hadoop-daemon.sh stop datanode".format(sip))
                os.system("ssh {} jps".format(sip))
                print("\t \t Datanode stopped successfully ........")
          i = input("do you want to continue on Hadoop menu [y/N]:\t")
          if i != 'y' and i!= 'Y':
                    break

    elif choice_hadoop == 12:   
          print("""
    1. Converting local Master node to Datanode
    2. Converting local Master node to client
    3. Converting local Datanode to master
    4. Converting local Datanode to client
    5. Coverting local Client to master node
    6. Converting local Client to datanode""")
          datan = int(input("Enter your choice:\t"))
          if datan == 1:
                add_slave()
                print("\n\t\t Successfully converted master node into Datanode and start the service............")
                i = input("do you want to continue on hadoop menu [y/N]:\t")
                if i != 'y' and i!= 'Y':
                    break

          elif datan == 2:
                add_client()
                print("\n\t\t Successfully converted master node into Client............")
                i = input("do you want to continue on hadoop menu [y/N]:\t")
                if i != 'y' and i!= 'Y':
                    break

          elif datan == 3:
                add_master()
                print("\n\t\t Successfully converted Datanode into Masternode and start the service............")
                i = input("do you want to continue on hadoop menu [y/N]:\t")
                if i != 'y' and i!= 'Y':
                    break
          elif datan == 4:
                add_client()
                print("\n\t\t Successfully converted Datanode into Client............")
                i = input("do you want to continue on hadoop menu [y/N]:\t")
                if i != 'y' and i!= 'Y':
                    break

          elif datan == 5:
                add_master()
                print("\n\t\t Successfully converted Client into Datanode and start the service............")
                i = input("do you want to continue on hadoop menu [y/N]:\t")
                if i != 'y' and i!= 'Y':
                    break
 
          elif datan == 6:
                add_slave()
                print("\n\t\t Successfully converted Client into Datanode and start the service............")
                i = input("do you want to continue on hadoop menu [y/N]:\t")
                if i != 'y' and i!= 'Y':
                    break


    elif choice_hadoop == 13:
          break
          


        
def add_master():
    print("to create a master first you have to make a folder for that")
    fold = input("folder name with directory:\t")
    os.system("mkdir {}".format(fold))
    old = ""
    old1 = ""
    with open("/etc/hadoop/hdfs-site.xml", "r+") as f:
        old = f.read()
        if len(old) < 20:
             print("hadoop is not installed on the system")
             exit()
        jame = old.find("<confi")
        jame1 = old.find("</confi")
        jame2 = old[jame:jame1]
        old = old.replace(jame2, "<configuration>\n <property>\n<name>dfs.name.dir</name>\n<value>{}</value>\n</property>\n".format(fold))
    with open("/etc/hadoop/hdfs-site.xml", "w") as f:
        f.write(old)

    print("You have to set the ip for your master")
    ip = input("provide the ip to the master ;\t")
    with open("/etc/hadoop/core-site.xml", "r+") as f:
        old1  = f.read()
        jam = old1.find("<confi")
        jam1 = old1.find("</confi")
        jam2 = old1[jam:jam1]
        old1 = old1.replace(jam2, "<configuration>\n <property>\n<name>fs.default.name</name>\n <value>hdfs://{}:9001</value>\n</property>\n".format(ip))
    with open("/etc/hadoop/core-site.xml", "w") as f:
        f.write(old1)
    print("Now the hadoop master folder format")
    os.system("hadoop namenode -format")
    os.system("hadoop-daemon.sh start namenode")
    print("Now the hadoop master servicee start you can check it by jps command")
    print("jps")



def add_slave():
    print("to create a slave first you have to make a folder for that")
    fold = input("folder name with directory:\t")
    os.system("mkdir {}".format(fold))
    old = ""
    old1 = ""
    with open("/etc/hadoop/hdfs-site.xml", "r+") as f:
        old = f.read()
        if len(old) < 20 :
             print("hadoop is not installed on the system")
             exit()
        jame = old.find("<confi")
        jame1 = old.find("</confi")
        jame2 = old[jame:jame1]
        old = old.replace(jame2, "<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>{}</value>\n</property>\n".format(fold))
    with open("/etc/hadoop/hdfs-site.xml", "w") as f:
        f.write(old)

    print("You have to provide hadoop master ip to established connection ")
    ip = input("provide the ip of the master ;\t")
    with open("/etc/hadoop/core-site.xml", "r+") as f:
        old1 = f.read()
        jam = old1.find("<confi")
        jam1 = old1.find("</confi")
        jam2 = old1[jam:jam1]
        old1 = old1.replace(jam2, "<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:9001</value>\n</property>\n".format(ip))
    with open("/etc/hadoop/core-site.xml", "w") as f:
        f.write(old1)
    os.system("hadoop-daemon.sh start datanode")
    print("Now the hadoop slave services start you can check it by jps command")
    os.system("jps")


def add_client():
    old = ""
    old1 = ""
    with open("/etc/hadoop/hdfs-site.xml", "r+") as f:
        old = f.read()
        if len(old) < 20:
             print("hadoop is not installed on the system")
             exit()
        jame = old.find("<confi")
        jame1 = old.find("</confi")
        jame2 = old[jame:jame1]
        old = old.replace(jame2, "<configuration>\n")
    with open("/etc/hadoop/hdfs-site.xml", "w") as f:
        f.write(old)

    print("You have to provide hadoop master ip to established connection between client and master")
    ip = input("provide the ip of the master ;\t")
    with open("/etc/hadoop/core-site.xml", "r+") as f:
        old1 = f.read()
        jam = old1.find("<confi")
        jam1 = old1.find("</confi")
        jam2 = old1[jam:jam1]
        old1 = old1.replace(jam2, "<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:9001</value>\n</property>\n".format(ip))
    with open("/etc/hadoop/core-site.xml", "w") as f:
        f.write(old1)
    print("Now the hadoop client services start you can check it by jps command")
    os.system("jps")





def webserver():
   while True:
        os.system("clear")
        os.system("tput setaf 11")
        os.system("\n\t\t\tfiglet -t -k webserver menu for local system\n\n\n")
        print("press 1: For configuring the yum for installing various software")
        print("press 2: For installing the apache webserver")
        print("press 3: For starting the service of webserver")
        print("press 4: For starting the service of webserver permanently" )
        print("press 5: For stopping the firewall")
        print("press 6: For stopping the webserver")
        print("press 7: For uploading a local file into webserver")
        print("press 8: For stopping the webserver permanently")
        print("press 9: To go back to the main menu")
        web_input = int(input("Enter your choise:\t"))
        os.system("tput setaf 7")

        if web_input == 1:
             with open("/etc/yum.repos.d/base2.repo", "w") as f:
                f.write("[cde1]\nbaseurl = file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream\ngpgcheck=0\n\n[cde2]\nbaseurl =file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS\ngpgcheck=0\n")
             print("Now yum has been configured")
             i = input("do you want to continue on webserver menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    break


        elif web_input == 2:
             os.system("yum install httpd -y")
             print("Now the webserver now install you can start the webserver now.")
             i = input("do you want to continue on webserver menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    break


        elif web_input == 3:
             os.system("systemctl start httpd")
             print("Webserver now started on the port no. 80")
             i = input("do you want to continue on webserver menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    break


        elif web_input == 4:
             os.system("systemctl restart httpd")
             os.system("systemctl enable httpd")
             print("Now the webserver started permanently")
             i = input("do you want to continue on webserver menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    break

        elif web_input == 5:
             os.system("systemctl stop firewalld")
             print("Firwall stopped successfully")
             i = input("do you want to continue on webserver menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    break


        elif web_input == 6:
             os.system("systemctl stop httpd")
             print("Webserver stopped successfully")
             i = input("do you want to continue on webserver menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    break


        elif web_input == 7:
             file_name_web = input("Provide the path of the file which would be uploading on the webserver")
             os.system("sudo cp {} /var/www/html ".format(file_name_web))
             print("File uploaded if the path is correct")
             i = input("do you want to continue on webserver menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    break


        elif web_input == 8:
             os.system("systemctl stop firewalld")
             os.system("systemctl disable firewalld")
             i = input("do you want to continue on webserver menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    break


        elif web_input == 9:
             break




def webserver2():
   while True:
        os.system("clear")
        os.system("tput setaf 11")
        os.system("\n\t\t\tfiglet -t -k webserver via ssh ")
        print("press 1: For configuring the yum for installing various software")
        print("press 2: For installing the apache webserver")
        print("press 3: For starting the service of webserver")
        print("press 4: For starting the service of webserver permanently" )
        print("press 5: For stopping the firewall")
        print("press 6: For stopping the webserver")
        print("press 7: For uploading a local file into webserver")
        print("press 8: For stopping the webserver permanently")
        print("press 9: To go back to the main menu")
        web_input = int(input("Enter your choise:\t"))
        os.system("tput setaf 7")

        if web_input == 1:
             sip = input("Enter the ip of the system to connect via ssh for configuring the yum:\t")
             with open("/root/base2.repo", "w") as f:
                f.write("[cde1]\nbaseurl = file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream\ngpgcheck=0\n\n[cde2]\nbaseurl =file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS\ngpgcheck=0\n")
             print("Now yum has been configured")
             os.system("scp  cp /root/base2.repo  {}:/etc/yum.repos.d/ ".format(sip))
             os.system("rm -f /root/base2.repo")
             i = input("do you want to continue on webserver menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    break


        elif web_input == 2:
             sip = input("Enter the ip of the system to connect via ssh for installing webserver:\t")
             os.system("ssh {} yum install httpd -y".format(sip))
             print("Now the webserver now install you can start the webserver now.")
             i = input("do you want to continue on webserver menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    break


        elif web_input == 3:
             sip = input("Enter the ip of the system to connect via ssh for starting webserver:\t")
             os.system("ssh {}  systemctl start httpd".format(sip))
             print("Webserver now started on the port no. 80")
             i = input("do you want to continue on webserver menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    break


        elif web_input == 4:
             sip = input("Enter the ip of the system to connect via ssh for enabling webserver:\t")
             os.system("ssh {}  systemctl restart httpd".format(sip))
             os.system("ssh {}  systemctl enable httpd".format(sip))
             print("Now the webserver started permanently")
             i = input("do you want to continue on webserver menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    break

        elif web_input == 5:
             sip = input("Enter the ip of the system to connect via ssh for stopping firewall:\t")
             os.system("systemctl stop firewalld".format(sip))
             print("Firwall stopped successfully")
             i = input("do you want to continue on webserver menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    break


        elif web_input == 6:
             sip = input("Enter the ip of the system to connect via ssh for stopping webserver:\t")
             os.system("ssh {}  systemctl stop httpd".format(sip))
             print("Webserver stopped successfully")
             i = input("do you want to continue on webserver menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    break


        elif web_input == 7:
             sip = input("Enter the ip of the system to connect via ssh for uploading file into webserver:\t")
             file_name_web = input("Provide the path of the file which would be uploading on the webserver")
             os.system("scp cp {} {}:/var/www/html/ ".format(file_name_web,sip))
             print("File uploaded if the path is correct")
             i = input("do you want to continue on webserver menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    break


        elif web_input == 8:
             sip = input("Enter the ip of the system to connect via ssh for disabling firewall:\t")
             os.system("ssh {}  systemctl stop firewalld".format(sip))
             os.system("ssh {}  systemctl disable firewalld".format(sip))
             i = input("do you want to continue on webserver menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    break

        elif web_input == 9:
             break

def Docker_menu():
     while True:
        os.system("clear")
        os.system("tput setaf 11")
        os.system("\n\t\t\tfiglet -t -k Docker")
        print("press 1: For installing Docker")
        print("press 2: start the service of docker")
        print("Press 3; For Launching an os inside of docker")
        print("press 4: to know all the running docker os" )
        print("press 5: For deleting a OS running on docker")
        print("press 6: For pulling an image for docker")
        print("press 7: To remove all running docker os")
        print("press 8: To go back to main menu")
        docker_input = int(input("Enter your choise:\t"))
        
        os.system("tput setaf 7")
        if docker_input == 1:
               with open("/etc/tum.repos.d/baseforyum.repo", "w") as f:
                     f.write("[cde1]\nbaseurl = file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream\ngpgcheck=0\n\n[cde2]\nbaseurl =file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS\ngpgcheck=0\n")

               os.system("sudo yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm")
               os.system("sudo yum update")
               os.system("yum -y install docker-ce --nobest")
               i = input("do you want to continue on docker menu [y/N]:\t")
               if i != 'y' and i!= 'Y':
                    break
        
        elif docker_input == 2:
               os.system("systemctl start docker")
               os.system("systemctl enable docker")
               i = input("do you want to continue on docker menu [y/N]:\t")
               if i != 'y' and i!= 'Y':
                    break

        elif docker_input == 3:
               image = input("enter the os you want to launch:\t")
               version = input("Enter the version of the image:\t")
               get = subprocess.getoutput("docker images")
               name = input("Give a name to launch os:\t")
               if image not in get:
                       os.system("sudo docker pull {}".format(image))
               os.system("sudo docker run -dit --name {} {}:{}".format(name, image, version))
               print("Docker os is now launched, For entering into the docker use 'docker attach {} '".format( name))
               i = input("do you want to continue on docker menu [y/N]:\t")
               if i != 'y' and i!= 'Y':
                    break

        elif docker_input == 5:
               print("Provide running socker os id or name")
               id_or_name = input("Enter the id or name:\n")
               os.system("docker rm -f {}".format(id_or_name))
               i = input("do you want to continue on docker menu [y/N]:\t")
               if i != 'y' and i!= 'Y':
                    break

        elif docker_input == 4:
               os.system("docker ps ")
               i = input("do you want to continue on docker menu [y/N]:\t")
               if i != 'y' and i!= 'Y':
                    break
 
        elif docker_input == 6:
               docker_im = input("Enter the name of the image to be pulled:\t")
               docker_ver = input("Enter the version of the image:\t") 
               if len(docker_ver) < 1:
                       os.system("docker pull {}:{}".format(docker_im, docker_ver))
               else:
                       os.system("docker pull {}".format(docker_im))
               i = input("do you want to continue on docker menu [y/N]:\t")
               if i != 'y' and i!= 'Y':
                    break

        elif docker_input == 7:
               os.system("docker rm -f `docker ps -q`")
               i = input("do you want to continue on docker menu [y/N]:\t")
               if i != 'y' and i!= 'Y':
                    break

        elif docker_input == 8:
               break



def Docker_menu2():
     while True:
        os.system("clear")
        os.system("tput setaf 11")
        os.system("\n\t\t\tfiglet -t -k Docker via ssh")
        print("press 1: For installing Docker")
        print("press 2: start the service of docker")
        print("Press 3; For Launching an os inside of docker")
        print("press 4: to know all the running docker os" )
        print("press 5: For deleting a OS running on docker")
        print("press 6: For pulling an image for docker")
        print("press 7: To remove all running docker os")
        print("press 8: To go back to main menu")
        docker_input = int(input("Enter your choise:\t"))
        
        os.system("tput setaf 7")
        if docker_input == 1:
               sip = input("Enter the ip of the system to install docker via ssh:\t")


               os.system("ssh {} sudo yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm".format(sip))
               os.system("ssh {} sudo yum update".format(sip))
               os.system("ssh {} yum -y install docker --nobest".format(sip))
               i = input("do you want to continue on docker menu [y/N]:\t")
               if i != 'y' and i!= 'Y':
                    break
        
        elif docker_input == 2:
               sip = input("Enter the ip of the system to start docker via ssh:\t")
               os.system("ssh {} systemctl start docker".format(sip))
               os.system("ssh {} systemctl enable docker".format(sip))
               i = input("do you want to continue on docker menu [y/N]:\t")
               if i != 'y' and i!= 'Y':
                    break

        elif docker_input == 3:
               sip = input("Enter the ip of the system to launch docker container via ssh:\t")
               image = input("enter the os you want to launch:\t")
               version = input("Enter the version of the image:\t")
               get = subprocess.getoutput("ssh {} docker images".format(sip))
               name = input("Give a name to launch os:\t")
               if image not in get:
                       version2 = input("Enter the version of the image:\t")
                       os.system("ssh {} sudo docker pull {}:{}".format(sip,image,version2))
               os.system("ssh {} sudo docker run -dit --name {} {}:{}".format(sip,name, image, version))
               print("Docker os is now launched, For entering into the docker use 'ssh {} sudo docker attach {} '".format(sip, name))
               i = input("do you want to continue on docker menu [y/N]:\t")
               if i != 'y' and i!= 'Y':
                    break

        elif docker_input == 5:
               sip = input("Enter the ip of the system to connect via ssh:\t")
               print("Provide running socker os id or name")
               id_or_name = input("Enter the id or name:\n")
               os.system("ssh {} docker rm -f {}".format(sip, id_or_name))
               i = input("do you want to continue on docker menu [y/N]:\t")
               if i != 'y' and i!= 'Y':
                    break

        elif docker_input == 4:
               sip = input("Enter the ip of the system to connect via ssh:\t")
               os.system("ssh {} docker ps ".format(sip))
               i = input("do you want to continue on docker menu [y/N]:\t")
               if i != 'y' and i!= 'Y':
                    break
 
        elif docker_input == 6:
               sip = input("Enter the ip of the system to connect via ssh:\t")
               docker_im = input("Enter the name of the image to be pulled:\t")
               docker_ver = input("Enter the version of the image:\t") 
               if len(docker_ver) < 1:
                       os.system("ssh {} sudo docker pull {}:{}".format(sip, docker_im, docker_ver))
               else:
                       os.system("ssh {} sudo docker pull {}".format(sip,docker_im))
               i = input("do you want to continue on docker menu [y/N]:\t")
               if i != 'y' and i!= 'Y':
                    break

        elif docker_input == 7:
               sip = input("Enter the ip of the system to connect via ssh:\t")
               os.system("ssh {} sudo docker rm -f `docker ps -q`".format(sip))
               i = input("do you want to continue on docker menu [y/N]:\t")
               if i != 'y' and i!= 'Y':
                    break

        elif docker_input == 8:
               break






while True:
      os.system("tput setaf 11")
      os.system("clear")
      print("\t\t\tWelcome to the Automation Menu")
      print("\t\t\t--------------------------------------")
      os.system("`\n\t\t\t` figlet -t -k Automation Menu\n\n")
      print("\nThis menu provide the various services to run any command or configure ")

      print("""
\n
press 1 : To run date command.
press 2 : Tp run cal command
press 3 : To know ip of the system.
press 4 : LVM
press 5 : AWS cloud
press 6 : Hadoop services
press 7 : To configure and run apache web server
press 8 : Docker
press 9 : Exit
 """)
      choice = int(input("Enter your choice:\t"))
      os.system("tput setaf 7")
      while True:
          if choice ==1:
                r = input("where you want to run your commands ? (local /remote) : ")
                if r == "local":
                    os.system("date")
                elif r == "remote":
                    sip = input("Enter your ip to run command:\t")
                    os.system("ssh {} date".format(sip))
                i = input("do you want to continue on automation menu [y/N]:\t")
                if i != 'y' or i != 'Y':
                    break
               

          elif choice ==2:
                r = input("where you want to run your commands ? (local /remote) : ")
                if r == "local":
                    os.system("cal")
                elif r == "remote":
                    sip = input("Enter your ip to run command:\t")
                    os.system("ssh {} cal".format(sip))
                i = input("do you want to continue on automation menu [y/N]:\t")
                if i != 'y' or i != 'Y':
                    break
                
          elif choice ==3:
                r = input("where you want to run your commands ? (local /remote) : ")
                if r == "local":
                    os.system("ifconfig")
                elif r == "remote":
                    sip = input("Enter your ip to run command:\t")
                    os.system("ssh {} ifconfig".format(sip))
                i = input("do you want to continue on automation menu [y/N]:\t")
                if i != 'y' or i != 'Y':
                    break
                

          elif choice == 4:
                lvm()
                break

          elif choice == 5:
                aws()
                break


          elif choice == 6:
                hadoop()
                break


          elif choice == 7:
                print("press 1 : For making the local system Web Server")
                print("press 2 : For making remote system webserver")
                datan = int(input("Enter your choice:\t"))
                if datan == 1:
                     webserver()
                elif datan == 2:
                     webserver2()
                break



          elif choice == 8:
                print("""press 1: for running docker in local system
press 2 : For running docker in remote system""")
                datan = int(input("enter your choice:\t"))
                if datan ==1:
                      Docker_menu()
                elif datan == 2:
                      Docker_menu2()
                break

          elif choice == 9:
                exit()
