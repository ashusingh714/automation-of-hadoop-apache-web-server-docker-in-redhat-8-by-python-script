import os 
import subprocess




def Docker_menu():
     while True:
        os.system("clear")
        os.system("tput setaf 10")
        os.system("figlet -t -k aws")
        print("press 1: For installing Docker")
        print("press 2: start the service of docker")
        print("Press 3; For Launching an os inside of docker")
        print("press 4: to know all the running docker os" )
        print("press 5: For deleting a OS running on docker")
        print("press 6: For pulling an image for docker")
        print("press 7: To remove all running docker os")
        print("press 7: To go back to main menu")
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
                    exit()
        
        elif docker_input == 2:
               os.system("systemctl start docker")
               os.system("systemctl enable docker")
               i = input("do you want to continue on docker menu [y/N]:\t")
               if i != 'y' and i!= 'Y':
                    exit()

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
                    exit()

        elif docker_input == 5:
               print("Provide running socker os id or name")
               id_or_name = input("Enter the id or name:\n")
               os.system("docker rm -f ".format(id_or_name))
               i = input("do you want to continue on docker menu [y/N]:\t")
               if i != 'y' and i!= 'Y':
                    exit()

        elif docker_input == 5:
               os.system("docker ps ")
               i = input("do you want to continue on docker menu [y/N]:\t")
               if i != 'y' and i!= 'Y':
                    exit()
 
        elif docker_input == 6:
               docker_im = input("Enter the name of the image to be pulled:\t")
               docker_ver = input("Enter the version of the image:\t") 
               if len(docker_ver) < 1:
                       os.system("docker pull {}:{}".format(docker_im, docker_ver))
               else:
                       os.system("docker pull {}".format(docker_im))
               i = input("do you want to continue on docker menu [y/N]:\t")
               if i != 'y' and i!= 'Y':
                    exit()

        elif docker_input == 7:
               os.system("docker rm -f `docker ps -q`")
               i = input("do you want to continue on docker menu [y/N]:\t")
               if i != 'y' and i!= 'Y':
                    exit()

        elif docker_input == 8:
               exit()

Docker_menu()

