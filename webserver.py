import os
import subprocess

def webserver():
   while True:
        os.system("clear")
        os.system("tput setaf 10")
        os.system("figlet -t -k webserver")
        print("press 1: For configuring the yum for installing various software")
        print("press 2: For installing the apache webserver")
        print("press 3: For starting the service of webserver")
        print("press 4: For starting the service of webserver permanently" )
        print("press 5: For stopping the firewall")
        print("press 6: For stopping the webserver")
        print("press 7: For uploading a local file into webserver")
        print("press 8: For stopping the webserver permanently")
        print("press 9: To go back to the main menu")
        web_input = int(input("Enter your choise"))
        os.system("tput setaf 7")

        if web_input == 1:
             with open("/etc/yum.repos.d/base2.repo", "w") as f:
                f.write("[cde1]\nbaseurl = file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream\ngpgcheck=0\n\n[cde2]\nbaseurl =file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS\ngpgcheck=0\n")
             print("Now yum has been configured")
             i = input("do you want to continue on docker menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    exit()


        elif web_input == 2:
             os.system("yum install httpd -y")
             print("Now the webserver now install you can start the webserver now.")
             i = input("do you want to continue on docker menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    exit()


        elif web_input == 3:
             os.system("systemctl start httpd")
             print("Webserver now started on the port no. 80")
             i = input("do you want to continue on docker menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    exit()


        elif web_input == 4:
             os.system("systemctl restart httpd")
             os.system("systemctl enable httpd")
             print("Now the webserver started permanently")
             i = input("do you want to continue on docker menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    exit()

        elif web_input == 5:
             os.system("systemctl stop firewalld")
             print("Firwall stopped successfully")
             i = input("do you want to continue on docker menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    exit()


        elif web_input == 6:
             os.system("systemctl stop httpd")
             print("Webserver stopped successfully")
             i = input("do you want to continue on docker menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    exit()


        elif web_input == 7:
             file_name_web = input("Provide the path of the file which would be uploading on the webserver")
             os.system("sudo cp {} /var/www/html ".format(file_name_web))
             print("File uploaded if the path is correct")
             i = input("do you want to continue on docker menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    exit()


        elif web_input == 8:
             os.system("systemctl stop firewalld")
             os.system("systemctl disable firewalld")
             i = input("do you want to continue on docker menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    exit()


        elif web_input == 9:
             exit()




def webserver2():
   while True:
        os.system("clear")
        os.system("tput setaf 10")
        os.system("figlet -t -k webserver")
        print("press 1: For configuring the yum for installing various software")
        print("press 2: For installing the apache webserver")
        print("press 3: For starting the service of webserver")
        print("press 4: For starting the service of webserver permanently" )
        print("press 5: For stopping the firewall")
        print("press 6: For stopping the webserver")
        print("press 7: For uploading a local file into webserver")
        print("press 8: For stopping the webserver permanently")
        print("press 9: To go back to the main menu")
        web_input = int(input("Enter your choise"))
        os.system("tput setaf 7")

        if web_input == 1:
             with open("/etc/yum.repos.d/base2.repo", "w") as f:
                f.write("[cde1]\nbaseurl = file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream\ngpgcheck=0\n\n[cde2]\nbaseurl =file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS\ngpgcheck=0\n")
             print("Now yum has been configured")
             os.system("scp {} cp /etc/yum.repos.d/base.repo   /etc/yum.repos.d/base.repo ")
             i = input("do you want to continue on docker menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    exit()


        elif web_input == 2:
             os.system("ssh {} yum install httpd -y".format(ip))
             print("Now the webserver now install you can start the webserver now.")
             i = input("do you want to continue on docker menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    exit()


        elif web_input == 3:
             os.system("ssh {}  systemctl start httpd".format(ip))
             print("Webserver now started on the port no. 80")
             i = input("do you want to continue on docker menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    exit()


        elif web_input == 4:
             os.system("ssh {}  systemctl restart httpd".format(ip))
             os.system("ssh {}  systemctl enable httpd".format(ip))
             print("Now the webserver started permanently")
             i = input("do you want to continue on docker menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    exit()

        elif web_input == 5:
             os.system("systemctl stop firewalld".format(ip))
             print("Firwall stopped successfully")
             i = input("do you want to continue on docker menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    exit()


        elif web_input == 6:
             os.system("ssh {}  systemctl stop httpd".format(ip))
             print("Webserver stopped successfully")
             i = input("do you want to continue on docker menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    exit()


        elif web_input == 7:
             file_name_web = input("Provide the path of the file which would be uploading on the webserver")
             os.system("scp {} cp {} /var/www/html/ ".format(ip,file_name_web))
             print("File uploaded if the path is correct")
             i = input("do you want to continue on docker menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    exit()


        elif web_input == 8:
             os.system("ssh {}  systemctl stop firewalld".format(ip))
             os.system("ssh {}  systemctl disable firewalld".format(ip))
             i = input("do you want to continue on docker menu [y/N]:\t")
             if i != 'y' and i!= 'Y':
                    exit()

        elif web_input == 9:
             exit()



aws()
