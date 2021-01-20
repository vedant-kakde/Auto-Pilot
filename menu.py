import os
import getpass as gp
import subprocess as sp
def af(number):
    os.system("tput setaf {}".format(number))
def rc(command):
    output=sp.getoutput(command)
    print(output)
rc("clear")
af(3)
print('\t\t\t\t\t WELCOME TO THE MENU DRIVEN PROGRAM')
print('\t\t\t\t\t ----------------------------------\n')
af(6)
password=gp.getpass("Please Enter the Password: ")
print()
if password!="p":
    af(1)
    print("\t\t\t\tAuthentication Failed. Please provide proper credentials")
    af(7)
    exit()
af(2)
input("\t\t\t\tAuthentication successful. Please press Enter to Continue")
print()
af(7)
location=input("Where do you want to execute this program? Local/Remote? : ")
print()
if ( ("local" in location) or ("Local" in location) or ("LOCAL" in location) ):
	rc("clear")
	while True:
		print("Please select your requirements for local execution: ")
		af(2)
		print('''
		[1] Basic Linux Operations        [4] Configure Webserver
		[2] Big Data - Hadoop             [5] DOCKER
		[3] AWS                           [6] ANSIBLE  		       
		''')
		af(7)
		x=input("Please Enter Your Choice: ")
		print(x)
		if int(x)==1:
			rc("clear")
			while True:
				rc("clear")
				af(4)
				print("\n\t\t\t\t\t\t"+48*"-")
				print("\t\t\t\t\t\t\t\tBASIC LINUX OPERATIONS")
				print("\t\t\t\t\t\t"+48*"-")
				af(7)
				af(3)
				print('''
				[1] Check Date\t\t[2] Check Calendar
				[3] Configure Yum\t[4] Install a package
				[5] Run Any Command of Your Choice
				[6] Go Back to Previous Menu
				''')
				af(7)
				ch=input("Enter Your Choice : ")
				if int(ch)==1:
					rc("date")
				if int(ch)==2:
					rc("cal")
				if int(ch)==3:
					rc("if ls /dvd; then command; else mkdir /dvd; fi &> error")
					rc("mount /dev/cdrom /dvd &> error")
					f = open("/etc/yum.repos.d/local.repo","a")
					repo = "[dvd1]\nbaseurl=file:///dvd/AppStream\ngpgcheck=0\n\n[dvd2]\nbaseurl=file:///dvd/BaseOS\ngpgcheck=0\n"
					f.write(repo)
					f.close()
					af(2)
					print("Local Yum Has Been Configured.")
					af(7)
					ip=input("Do you want to List All Repos? (Yes/No) : ")
					if ( ("yes" in ip) or ("Yes" in ip) or ("YES" in ip) ):
						rc("yum repolist")
				if int(ch)==4:
					while True:
						rc("clear")
						af(3)
						print("\t\t\t\t\tInstall a Package\n")
						af(2)
						i=input("Enter the Package's Name : ")
						af(7)
						rc("yum install {} -y".format(i))
						af(1)
						x=input("\nHit Enter to Install Another Package, type exit to go back : ")
						af(7)
						if x=="exit":
							break
							rc("clear")
						else:
							rc("clear")
				if int(ch)==5:
					while True:
						rc("clear")
						af(3)
						print("\t\t\t\t\tRun Any Manual Command")
						af(2)
						cmd=input("\nEnter the Command to Run : ")
						af(7)						
						rc(cmd)
						af(1)
						inp=input("\nHit Enter to Continue, type exit to go back : ")
						af(7)
						if inp=="exit":
							break
							rc("clear")
						else:
							rc("clear")
				if int(ch)==6:
					break
				af(1)
				input("\nPress Enter to Continue ")
				af(7)
				rc("clear")
		elif int(x)==2:
			rc("clear")
			while True:
				rc("clear")
				af(4)
				print("\n\t\t\t\t\t\t"+42*"-")
				print("\t\t\t\t\t\t\t\tHADOOP MENU")
				print("\t\t\t\t\t\t"+42*"-")
				af(7)
				af(3)
				print('''
\t\t[H] Download Hadoop			 [J] Download JDK
\t\t[1] Install Hadoop 			 [2] Install JDK
\t\t[3] Configure Master Node on This System [4] Configure Slave Node on Remote System
\t\t[5] Show All the Running Java Process	 [6] Show the Cluster Report
\t\t[7] Start the Master Node Services	 [8] Stop the Master Node Services
\t\t[9] Start the Data Node Services	 [10] Stop the Data Node Services
\t\t[11] Create an Empty File		 [12] Upload A File
\t\t[13] Read a file from the Cluster 	 [14] Delete A File In the Cluster
\t\t[15] List All The Files in the Cluster	 [16] Go back to previous menu
				''')
				af(7)
				y=input("\nEnter your choice: ")
				print()
				if y=="H":
					af(2)
					rc("cd /root/")
					os.system("yum install python2 -y")
					os.system("pip2 install gdown")
					af(3)
					print("\nDownloading Hadoop...")
					af(4)
					rc("gdown --id 1541gbFeGZZJ5k9Qx65D04lpeNBw87rM5")

				elif y=="J":
					af(2)
					rc("cd /root/")
					os.system("yum install python2 -y")
					os.system("pip2 install gdown")
					af(3)
					print("\nDownloading JDK...")
					af(4)
					rc("gdown --id 17UWQNVdBdGlyualwWX4Cc96KyZhD-lxz")


				elif int(y)==1:
					af(2)
					print("\nInstalling Hadoop.....")
					rc("rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force")
					af(7)

				elif int(y)==2:
					af(2)
					print("\nInstalling JDK...")
					rc("rpm -ivh /root/jdk-8u171-linux-x64.rpm")
					af(7)

				elif int(y)==3:
					af(2)
					directory=input("\nPlease Enter Directory Name for Namenode: ")
					print("\nConfiguring HDFS File... ")
					af(7)
					rc("if ls {0}; then command; else mkdir {0}; fi &> error".format(directory))
					rc("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>{}</value>\n</property>\n</configuration>' > /etc/hadoop/hdfs-site.xml".format(directory))
					af(2)
					ip_core=input("\nPlease Enter Name Node's IP Address : ")
					port_core=input("\nPlease Enter The Port For Name Node Services : ")
					print("\nConfiguring CORE File... ")
					af(7)
					rc("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:{}</value>\n</property>\n</configuration>' > /etc/hadoop/core-site.xml".format(ip_core, port_core))
					rc("hadoop namenode -format -force")

				elif int(y)==4:
					af(2)
					ip=input("\nEnter the Remote Server's IP : ")
					hd=input("\nWould You Like To Download Hadoop on the Remote Server ? (Yes/No) : ")
					if (("yes" in hd) or ("Yes" in hd) or ("YES" in hd)):
						rc("cd /root/")
						os.system("ssh {} yum install python2 -y".format(ip))
						os.system("ssh {} pip2 install gdown".format(ip))
						af(3)
						print("\nDownloading JDK...\n")
						rc("ssh {} gdown --id 1541gbFeGZZJ5k9Qx65D04lpeNBw87rM5".format(ip))
					elif (("no" in hd) or ("No" in hd) or ("NO" in hd)):
						af(1)
						print("\nMake Sure Hadoop is Already Downloaded in the System")
						af(7)
					else:
						af(1)
						print("\nInvalid Choice\nForwarding Without Downloading")
						af(7)

					jd=input("\nWould You Like To Download JDK on the Remote Server ? (Yes/No) : ")
					if (("yes" in jd) or ("Yes" in jd) or ("YES" in jd)):
						rc("cd /root/")
						os.system("ssh {} yum install python2 -y".format(ip))
						os.system("ssh {} pip2 install gdown".format(ip))
						af(3)
						print("\nDownloading JDK...\n")
						rc("ssh {} gdown --id 17UWQNVdBdGlyualwWX4Cc96KyZhD-lxz".format(ip))
					elif (("no" in jd) or ("No" in jd) or ("NO" in jd)):
						af(1)
						print("\nMake Sure JDK is Already Downloaded in the System")
						af(7)
					else:
						af(1)
						print("\nInvalid Choice\nForwarding Without Downloading")
						af(7)
				
					af(2)
					input("\nPress Enter To Continue : ")
					rc("clear")
					
					hi=input("\nWould You Like To INSTALL Hadoop on the Remote Server ? (Yes/No) : ")
					if (("yes" in hi) or ("Yes" in hi) or ("YES" in hi)):
						af(3)
						lh=input("\nPlease Input Hadoop rpm's location : ")
						rc("cd {}".format(lh))
						rc("ssh {} rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force".format(ip))
					elif (("no" in hi) or ("No" in hi) or ("NO" in hi)):
						af(1)
						print("\nMake Sure Hadoop is Already Installed in the System")
						af(7)
					else:
						af(1)
						print("\nInvalid Choice\nForwarding Without Installing")
						af(7)

					ji=input("\nWould You Like To INSTALL JDK on the Remote Server ? (Yes/No) : ")
					if (("yes" in ji) or ("Yes" in ji) or ("YES" in ji)):
						af(3)
						lj=input("\nPlease Input JDK rpm's location : ")
						rc("cd {}".format(lj))
						rc("ssh {} rpm -ivh jdk-8u171-linux-x64.rpm".format(ip))
					elif (("no" in ji) or ("No" in ji) or ("NO" in ji)):
						af(1)
						print("\nMake Sure JDK is Already Installed in the System")
						af(7)
					else:
						af(1)
						print("\nInvalid Choice\nForwarding Without Installing")
						af(7)
					af(2)
					input("\nPress Enter To Continue : ")
					rc("clear")

					remote_directory=input("\nPlease Enter Directory Name for Datanode : ")
					print("\nConfiguring HDFS File... ")
					af(7)
					rc('ssh root@{0} "if ls {1}; then command; else mkdir {1}; fi &> error"'.format(ip,remote_directory))
					rc("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>{0}</value>\n</property>\n</configuration>' > hdfs".format(remote_directory))
					rc("scp hdfs root@{}:/etc/hadoop/hdfs-site.xml".format(ip))
					af(2)
					remote_ip_core=input("\nPlease Enter Name Node's IP Address : ")
					remote_port_core=input("\nPlease Enter The Port For Name Node Services : ")
					print("\nConfiguring CORE File... ")
					af(7)
					rc("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{0}:{1}</value>\n</property>\n</configuration>' > core".format(remote_ip_core,remote_port_core))
					rc("scp core root@{}:/etc/hadoop/core-site.xml".format(ip))
				elif int(y)==5:
					af(4)
					rc("jps")
					af(7)
				elif int(y)==6:
					af(3)
					rc("hadoop dfsadmin -report")
					af(7)
				elif int(y)==7:
					af(2)
					rc("hadoop-daemon.sh start namenode")
					af(7)
				elif int(y)==8:
					af(2)
					rc("hadoop-daemon.sh stop namenode")
					af(7)
				elif int(y)==9:
					af(2)
					data_ip=input("\nEnter The IP of Data Node : ")
					af(7)
					rc("ssh {} hadoop-daemon.sh start datanode".format(data_ip))
				elif int(y)==10:
					af(2)
					data_ip=input("\nEnter The IP of Data Node : ")
					af(7)
					rc("ssh {} hadoop-daemon.sh stop datanode".format(data_ip))
				elif int(y)==11:
					af(2)
					file_name=input("\nEnter the File Name : ")
					af(7)
					rc("hadoop fs -touchz /{}".format(file_name))
				elif int(y)==12:
					af(2)
					put=input("\nEnter the File Name to Upload : ")
					af(7)
					rc("hadoop fs -put {} /".format(put))
				elif int(y)==13:
					af(2)
					read=input("\nEnter the File Name to Read : ")
					af(7)
					rc("hadoop fs -cat {}".format(read))
				elif int(y)==14:
					af(2)
					delete=input("\nEnter the file name to delete : ")
					af(7)
					rc("hadoop fs -rm /{}".format(delete))
				elif int(y)==15:
					af(6)
					rc("hadoop fs -ls /")
					af(7)
				elif int(y)==16:
					break
				af(1)
				input("\nPress Enter to Continue ")	
				rc("clear")
				af(7)
		elif int(x)==3:
			while True:
				rc("clear")
				af(4)
				print("\n\t\t\t\t\t\t"+42*"-")
				print("\t\t\t\t\t\t\t\tAWS MENU")
				print("\t\t\t\t\t\t"+42*"-")
				af(7)
				af(3)
				print("""
				Press  1 : To Login into AWS CLI
				Press  2 : To Launch a instance
				Press  3 : To Start a Instance
				Press  4 : To Stop a Instance 
				Press  5 : To Describe All Instances 
				Press  6 : To Create a Volume
				Press  7 : To Attach volume with instance
				Press  8 : For Partitioning the attached volume
				Press  9 : To configure Web Server
				Press 10 : To Format Partition
				Press 11 : To Mount the Web Server to Volume
				Press 12 : Go To Previous Menu
				""")
				af(2)
				ch=input("\nEnter Your Choice : ")
				af(7)
				if int(ch) == 1:
					os.system("aws configure")
					af(2)
					input("\nHit Enter To Continue : ")
					af(7)
				elif int(ch) == 2:
					print("""
							Press 1:AWS Linux
							Press 2:Redhat Linux
							""")
					print("Enter your Choice :  ",end="")
					img=input()
					if int(img) ==1:
						print("Enter Your Key name: ",end ="")
						key = input()
						os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --subnet-id subnet-ba5b5cd2 --instance-type t2.micro --key-name {} --security-group-ids sg-0c111e5b44f074df9 --count 1".format(key))
					elif int(img) == 2:
						print("Enter Your Key name: ",end ="")
						key = input()
						os.system("aws ec2 run-instances --image-id ami-052c08d70def0ac62 --subnet-id subnet-ba5b5cd2 --instance-type t2.micro --key-name {} --security-group-ids sg-0c111e5b44f074df9 --count 1".format(key))
					af(2)
					input("\nHit Enter To Continue : ")
					af(7)

				elif int(ch) == 3:
					print("Enter Instance Id : ",end = "")
					uid = input()
					os.system(" aws ec2 start-instances --instance-id {}".format(uid))
					af(2)
					input("\nHit Enter To Continue : ")
					af(7)

				elif int(ch) == 4:
					
					print("Enter Instance Id : ",end = "")
					uid = input()
					os.system(" aws ec2 stop-instances --instance-id {}".format(uid))
					af(2)
					input("\nHit Enter To Continue : ")
					af(7)

				elif int(ch) == 5:

					os.system("aws ec2 describe-instances")
					af(2)
					input("\nHit Enter To Continue : ")
					af(7)
					
				elif int(ch) == 6:

					
					print("Enter Size : ",end = "")
					size = input()
					print("Enter availability zone : ",end = "")
					zone = input()
					print("Enter volume type : ",end= "")
					vtype = input()
					os.system(" aws ec2 create-volume  --availability-zone {} --size {} --volume-type {}".format(zone,size,vtype))
					af(2)
					input("\nHit Enter To Continue : ")
					af(7)

				elif int(ch) == 7:


					print("Enter Instance Id : ",end = "")
					uid = input()
					print("\t\t\tVolume Zone & Instance Zone Must be same !!!")
					print("\t\t\t--------------------------------------------")
					print("Enter volume-id : ",end = "")
					vid = input()
					print("Enter instance-id : ",end = "")
					iid = input()
					print("Enter device : /dev/",end= "")
					device = input()
					os.system(" aws ec2 start-instances --instance-id {}".format(uid))
					os.system(" aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/{} ".format(vid,iid,device))
					af(2)
					input("\nHit Enter To Continue : ")
					af(7)

				elif int(ch) == 8:

					print("Enter IP : ",end = "")
					ip = input()
					print("Enter key : ",end = "")
					key = input()
					print("Enter device : /dev/",end= "")
					device = input()
					os.system(" ssh -l ec2-user {} -i {}.pem sudo fdisk /dev/{} ".format(ip,key,device))
					af(2)
					input("\nHit Enter To Continue : ")
					af(7)


				elif int(ch) == 9:

					print("Enter Instance Id : ",end = "")
					uid = input()
					print("\t\t\tHTTPD must be installed...")
					print("\t\t\t--------------------------")
					print("Enter volume-id : ",end = "")
					vid = input()
					print("Enter instance-id : ",end = "")
					iid = input()
					print("Enter device : /dev/",end= "")
					device = input()
					os.system(" aws ec2 start-instances --instance-id {}".format(uid))
					os.system(" aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/{} ".format(vid,iid,device))
					print("Enter IP : ",end = "")
					ip = input()
					print("Enter key : ",end = "")
					key = input()
					os.system(" ssh -l ec2-user {} -i {}.pem sudo systemctl start httpd ".format(ip,key))
					af(2)
					input("\nHit Enter To Continue : ")
					af(7)

				elif int(ch) == 10:

					print("Enter IP : ",end = "")
					ip = input()
					print("Enter key : ",end = "")
					key = input()
					print("Enter Device : /dev/",end="")
					device = input()
					os.system(" ssh -l ec2-user {} -i {}.pem sudo mkfs.ext4 /dev/{} ".format(ip,key,device))
					af(2)
					input("\nHit Enter To Continue : ")
					af(7)

				elif int(ch) == 11:

					print("Enter IP : ",end = "")
					ip = input()
					print("Enter key : ",end = "")
					key = input()
					print("Enter Device : /dev/",end="")
					device = input()
					os.system(" ssh -l ec2-user {} -i {}.pem sudo mount /dev/{} /var/www/html/ ".format(ip,key,device))
					af(2)
					input("\nHit Enter To Continue : ")
					af(7)

				elif int(ch) == 12:
					break					
				else:
					print("You Entered Wrong Choice ...")
					af(2)
					input("\nHit Enter To Continue : ")
					af(7)
				af(2)
				input("\nPress Enter To Continue : ")
				af(7)
		elif int(x)==4:
			rc("clear")
			af(4)
			print("\n\t\t\t\t\t\t"+49*"-")
			print("\t\t\t\t\t\t\t\tWEB SERVER CONFIGURATION")
			print("\t\t\t\t\t\t"+49*"-")
			af(7)
			af(3)
			print("\nInstalling WebServer...")
			af(7)
			os.system("yum install httpd -y")
			af(1)
			input("\nHit Enter to Start the Web Services : ")			
			os.system("systemctl start httpd")
			print("WebServices Started...")
			af(7)
		elif int(x)==5:
			from os import system
			rc("clear")
			while True:
				rc("clear")
				af(4)
				system("tput setaf 2")
				print("\n\t"+42*"-")
				print("\t\t\tDOCKER MENU")
				print("\t"+42*"-")
				system("tput setaf 5")
				print("\n\tPlease select an option: \n")
				system("tput setaf 3")
				print("""
				Press 1  : Install Docker
				Press 2  : Start Docker Service
				Press 3  : Stop Docker Service
				Press 4  : View Docker Info
				Press 5  : View Active containers
				Press 6  : View All containers
				Press 7  : View Downloaded images
				Press 8  : Pull an image
				Press 9  : Launch a container
				Press 10 : Stop a container
				Press 11 : Start a container
				Press 12 : Remove an image
				Press 13 : Remove a container
				Press 14 : Go to Previous menu
				""")
				system("tput setaf 7")
				opt = input("\n\tEnter your choice: ")
				system("tput setaf 7")

				# Install Docker
				if opt == '1':
					system("clear")
					if not system("rpm -q docker-ce"):
						print("\tDocker is already installed. Exiting installation...")
						system("sleep 2")
						
					else:
						print("\tInstalling Docker...")
						
						f = open("/etc/yum.repos.d/docker-ce_install.repo","a")
						dockrepo = "[docker]\nbaseurl=https://download.docker.com/linux/centos/7/x86_64/stable/\ngpgcheck=0\n"
						f.write(dockrepo)
						f.close()
					system("yum install docker-ce --nobest -y")
					system("systemctl start docker")
					system("systemctl enable docker")
					system("sleep 2")
					af(2)
					input("\nPress Enter to Continue")
					af(7)
				# Start docker service
				elif opt == '2':
					system("clear")
					system("systemctl start docker")
					af(2)
					input("\nPress Enter to Continue")
					af(7)

				# Stop docker service
				elif opt == '3':
					system("clear")
					system("systemctl stop docker")
					af(2)
					input("\nPress Enter to Continue")
					af(7)

				# View docker info
				elif opt == '4':
					system("clear")
					cmd = "docker info"
					system(cmd)
					af(2)
					input("\nPress Enter to Continue")
					af(7)
					
				# View active containers
				elif opt == '5':
					system("clear")
					cmd = "docker ps"
					system(cmd)
					af(2)
					input("\nPress Enter to Continue")
					af(7)
					
				# View all containers
				elif opt == '6':
					system("clear")
					cmd = "docker ps -a"
					system(cmd)
					af(2)
					input("\nPress Enter to Continue")
					af(7)
					
				# View downloaded images
				elif opt == '7':
					system("clear")
					cmd = "docker images"
					system(cmd)
					af(2)
					input("\nPress Enter to Continue")
					af(7)
					
				# Pull an image
				elif opt == '8':
					system("clear")
					system("tput setaf 6")
					img = input("\n\tEnter image name: ")
					ver = input("\tEnter image version (optional): ")
					system("tput setaf 7")
					
					if img:
						cmd = f"docker pull {img}:{ver}" if ver != "" else f"docker pull {img}"
						system(cmd)
						system("sleep 2")
						break
					else:
						print("\n\tNo image name entered! Getting back to previous menu...\n")
						system("sleep 2")

				# Launch a container
				elif opt == '9':
					system("clear")
					flags = ""
					system("tput setaf 6")
					img = input("\tEnter image name: ")
					ver = input("\tEnter image version (optional): ")
					interact = input("\tInteractive (y/n): ")
					console = input("\tShell prompt (y/n): ")
					name = input("\tEnter container name (optional): ")
					system("tput setaf 7")
					
					if img:
						if interact or console:
							flags += '-'
							if interact.lower() in ['y','yes']: flags += 'i'
							if console.lower() in ['y','yes']: flags += 't'
						if name: flags += f" --name {name}"
					
						cmd = f"docker run {flags} {img}:{ver}" if ver else f"docker run {flags} {img}"
						system(cmd)
						
					else: print("\tPlease enter an image name!")
					system("sleep 2")
					
				# Stop a container
				elif opt == '10':
					system("clear")
					system("tput setaf 6")
					name_id = input("\tEnter container name or id: ")
					system("tput setaf 7")
					system(f"docker stop {name_id}") if name_id else print("\tPlease enter a container name/ID!")
					system("sleep 2")

				# Start a container
				elif opt == '11':
					system("clear")
					name_id = input("\tEnter container name or ID: ")
					system(f"docker start {name_id}") if name_id else print("\tPlease enter a container name/ID!")
					system("sleep 2")
					
				# Remove an image
				elif opt == '12':
					system("clear")
					flags,img = "",""
					system("tput setaf 6")
					img = input("\tEnter image name: ")
					ver = input("\tEnter image version (optional): ")
					force = input("\tForce remove (y/n): ")
					system("tput setaf 7")
					
					if force.lower() in ['y', 'yes']: flags += "--force"
					if img:
						cmd = (f"docker rmi {img}:{ver} {flags}" if ver != "" else f"docker rmi {img} {flags}")
						system(cmd)
					else:
						system("clear")
						print("\tPlease enter an image name!")
						
					system("sleep 2")
					
				# Remove a container
				elif opt == '13':
					system("clear")
					system("tput setaf 6")
					name_id = input("\tEnter container name or ID: ")
					system("tput setaf 7")
					system(f"docker rm {name_id}") if name_id else print("\tPlease enter a container name/ID!")
					system("sleep 2")

				# Previous menu	
				elif opt == '14':
					system("clear")
					break	
		elif int(x)==6:
			while True:
				rc("clear")
				af(4)
				print("\n\t\t\t\t\t\t"+42*"-")
				print("\t\t\t\t\t\t\t\tANSIBLE MENU")
				print("\t\t\t\t\t\t"+42*"-")
				af(7)
				af(3)
				print('''
				Press 1  : Install Ansible
				Press 2  : Check Ansible Version
				Press 3  : List all Hosts
				Press 4  : Set inventory
				Press 5  : Ansible Configuartion
				Press 6  : Ping All Hosts
				Press 7  : Install httpd in all hosts
				Press 8  : Start httpd service in all hosts
				Press 9  : Go to Previous Menu
				''')
				af(7)
				y=input("\nEnter your choice: ")
				print()
				if int(y)==1:
					print("Installing Ansible.....")
					os.system("pip3 install ansible")
					os.system("clear")
					epel=input("Do you want to install epel-release. Yes or No: ")
					if ( ("yes" in epel) or ("Yes" in epel) or ("YES" in epel) ):
					  os.system("dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm")
					os.system("clear")
					sshpass=input("Do you want to install sshpass. Yes or No: ")
					if ( ("yes" in sshpass) or ("Yes" in sshpass) or ("YES" in sshpass) ):
					  os.system("yum install sshpass")
					af(2)
					input("\nPress Enter to Continue")
					af(7)
				if int(y)==2:
					print("Checking Ansible Version.....")
					rc("ansible --version")
					af(2)
					input("\nPress Enter to Continue")
					af(7)
				if int(y)==3:
					print("Listing all Hosts.....")
					rc("ansible all --list-hosts")
					af(2)
					input("\nPress Enter to Continue")
					af(7)
				if int(y)==4:
					print("Setting inventory.....")
					ip = input("\tEnter IP: ")
					os.system("touch /root/ip.txt")
					f = open("/root/ip.txt","a")
					inventory = f"{ip} ansible_user=root ansible_ssh_pass=redhat ansible_connection=ssh"
					f.write(inventory)
					f.close()
					os.system("ansible all --list-hosts")
					af(2)
					input("\nPress Enter to Continue")
					af(7)
				if int(y)==5:
					print("Configuring Ansible.....")
					rc("if ls /etc/ansible; then command; else mkdir /etc/ansible; fi &> error")
					os.system("touch /etc/ansible/ansible.cfg")
					f = open("/etc/ansible/ansible.cfg","a")
					cfg = "[defaults]\ninventory = /root/ip.txt\nhost_key_checking = false"
					f.write(cfg)
					f.close()
					rc("cat /etc/ansible/ansible.cfg")
					af(2)
					input("\nPress Enter to Continue")
					af(7)
				if int(y)==6:
					print("Pinging All Hosts.....")
					os.system("ansible all -m ping")
					af(2)
					input("\nPress Enter to Continue")
					af(7)
				if int(y)==7:
					print("Installing httpd in all hosts.....")
					os.system("ansible all -m package -a \"name=httpd state=present\"")
					af(2)
					input("\nPress Enter to Continue")
					af(7)
				if int(y)==8:
					print("Starting httpd service in all hosts.....")
					os.system("ansible all -m service -a \"name=httpd state=started\"")
					af(2)
					input("\nPress Enter to Continue")
					af(7)
				if int(y)==9:
					rc("clear")
					break
					af(2)
					input("\nPress Enter to Continue")
					af(7)
#Main x
		input("\nPress Enter to Continue")	
		rc("clear")
elif ( ("remote" in location) or ("Remote" in location) or ("REMOTE" in location) ):
	rc("clear")
	while True:
		print("Please select your requirements for remote execution: ")
		af(2)
		print('''
		[1] Basic Linux Options        [5] DOCKER
		[2] Big Data - Hadoop          [6] ANSIBLE
		[3] AWS                        [7] Machine Learning
		[4] Configure Webserver        [8] DSA
		''')
		af(7)
		x=input("Please Enter Your Choice: ")
		print(x)
		input("Press Enter to Continue")
		rc("clear")
else:
	af(1)
	print("\t\t\t\t\tPlease try again with a proper location")
	af(7)
	print()