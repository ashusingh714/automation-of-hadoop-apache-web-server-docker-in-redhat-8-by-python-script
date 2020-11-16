import os 
import subprocess


def aws():
    while True:
        os.system("clear")
        os.system("tput setaf 10")
        os.system("figlet -t -k aws")
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
                    inter = input("do you want to continue on docker menu [y/N]:\t")
                    if inter != 'y' and inter!= 'Y':
                          exit()

        elif aws_input == 2:
                    name = input("provide name to the aws user:\t")
                    os.system("aws configure --profile  {}".format(name))
                    inter = input("do you want to continue on docker menu [y/N]:\t")
                    if inter != 'y' and inter!= 'Y':
                         exit()

        elif aws_input == 3:
            key_name=input("enter the key name you want:\t")
            os.system("aws ec2 create-key-pair --key-name {} ".format(key_name) )
            inter = input("do you want to continue on docker menu [y/N]:\t")
            if inter != 'y' and inter!= 'Y':
                 exit()

        elif aws_input == 4:
                    securitygrp_name=input("enter the securiy group name:\t")
                    ports = input("which port you want to allow:\t")
                    os.system("aws ec2 create-security-group --description 'allow {}  ports' --group-name {}".format(ports, securitygrp_name ))
                    port_no = input("How many port you want to allow for ingress:\t")
                    for i in range(port_no+1):
                           port = input("Enter the port :\t")
                           os.system("aws ec2 authorize-security-group-ingress --group-name {} --protocol 'tcp' --port {} --cidr '0.0.0.0/0'".format(securitygrp_name, port))
                    inter = input("do you want to continue on docker menu [y/N]:\t")
                    if inter != 'y' and inter!= 'Y':
                          exit()

        elif aws_input == 5:
                    os.system("aws describe instances")
                    inter = input("do you want to continue on docker menu [y/N]:\t")
                    if inter != 'y' and inter!= 'Y':
                          exit()

        elif aws_input == 6:
                  
                    sg_id=input("please give securiy group id :\t")
                    key_name=input("please enter the key name :.\t")
                    print("Please select the image you want to launch\n 1. Amazon Linux AMi\n 2.Redhat Linux\n 3. Windows")
                    image_choice = input("Enter your choice:\t")
                    images_avail = ["ami-0e306788ff2473ccb","ami-052c08d70def0ac62","ami-0b2f6494ff0b07a0e"] 
                    image_launch = image_avail[image_choice-1]
                    cout = input("How many os you want to launch:\t")
                    os.system("aws ec2 run-instances --image-id {} --instance-type t2.micro  --count {} --key-name {} --security-group-ids {}".format(image_launch,cout,key_name,sg_id))
                    inter = input("do you want to continue on docker menu [y/N]:\t")
                    if inter != 'y' and inter!= 'Y':
                          exit()

        elif aws_input == 7:
                    os.system("aws ec2 create-volume --availability-zone ap-south-1b --size 1 --volume-type gp2")
                    inter = input("do you want to continue on docker menu [y/N]:\t")
                    if inter != 'y' and inter!= 'Y':
                          exit()

        elif aws_input == 8:
                    instance_id=input("please give instance id:")
                    vol_id=input("please give volume id :\t")
                    os.system("aws ec2 attach-volume --device /dev/sdh --instance-id {} --volume-id {}".format(instance_id,vol_id))
                    inter = input("do you want to continue on docker menu [y/N]:\t")
                    if inter != 'y' and inter!= 'Y':
                          exit()

        elif aws_input == 9:
            bucket_name=input("please give an identical bucket name:\t")
            os.system("aws s3api create-bucket --bucket {} --region ap-south-1 --acl public-read --create-bucket-configuration LocationConstraint=ap-south-1".format(bucket_name))
            inter = input("do you want to continue on docker menu [y/N]:\t")
            if inter != 'y' and inter!= 'Y':
                 exit() 

        elif aws_input == 10:
            print("Available s3 bucket: " )
            os.system("aws s3 ls")
            bucket_name=input("please give bucket name where you want to upload the object:\t")
            object_name=input("please give the full path of the file which you want to upload:\t")
            os.system("aws s3 cp {} s3://{}/".format(object_name,bucket_name))
            inter = input("do you want to continue on docker menu [y/N]:\t")
            if inter != 'y' and inter!= 'Y':
                 exit()

        elif aws_input == 11:
            bucket_name=input("buket name for cloudfront:\t")
            os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com".format(bucket_name))
            inter = input("do you want to continue on docker menu [y/N]:\t")
            if inter != 'y' and inter!= 'Y':
                 exit()

        elif aws_input == 12:
            exit()


aws()





