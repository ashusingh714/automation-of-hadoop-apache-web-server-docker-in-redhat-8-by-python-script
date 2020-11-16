import os 
import subprocess

def hadoop():
  while True:
    os.system("clear")
    os.system("tput setaf 10")
    os.system("figlet -t -k Hadoop  cluster")
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
          print("press 2 : For making Namenode by ssh")
          datan = int(input("Enter your choice:\t"))
          if datan == 1:
                 add_master()
          elif datan == 2:
           sip = input("Enter Name Node IP : \t")
           sshd = input("Enter your Name Node directory name : \t")
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
           os.system('scp  /root/hdfs-site.xml  {}:/etc/hadoop/'.format(dip))
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
           os.system('scp  /root/core-site.xml  {}:/etc/hadoop/'.format(dip))
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
           os.system('scp  /root/hdfs-site.xml  {}:/etc/hadoop/'.format(dip))
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
        old1 = f.read()
        jam = old1.find("<confi")
        jam1 = old1.find("</confi")
        jam2 = old1[jam:jam1]
        old1 = old1.replace(jam2, "<configuration>\n <property>\n<name>fs.default.name</name>\n <value>hdfs://{}:9001</value>\n</property>\n".format(ip))
    with open("/etc/hadoop/core-site.xml", "w") as f:
        f.write(old1)
        print(old1)
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
        jam = old1.find("<confi")
        jam1 = old1.find("</confi")
        jam2 = old1[jam:jam1]
        old1 = old1.replace(jam2, "<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:9001</value>\n</property>\n".format(ip))
    with open("/etc/hadoop/hdfs-site.xml", "w") as f:
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




hadoop()












