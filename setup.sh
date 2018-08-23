
# install ansible, update apt 
sudo apt-get update
sudo apt-get install software-properties-common
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update
sudo apt-get install ansible
sudo apt-get install openssh-client

# install necessary libraries
sudo apt-get install python-pip
pip2 install jinja2 — upgrade
sudo apt-get install python-netaddr

# install networking utils/conf networking
sudo apt-get install ufw
sudo sysctl -w net.ipv4.ip_forward=1
sudo ufw disable

# create agenda folders for temp storage
sudo mkdir /usr/local/agenda
sudo mkdir /usr/local/agenda/temp

# cd into agenda folder to dl kubespray
cd /usr/local/agenda
git clone https://github.com/kubernetes-incubator/kubespray.git
