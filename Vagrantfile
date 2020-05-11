# -*- mode: ruby -*-
# vi: set ft=ruby :

$provisionning = <<-PROVISIONNING

# Installing tools
sudo yum -y install epel-release
sudo yum install -y curl dos2unix git make mlocate nmap strace tar tee tree unzip vim
sudo updatedb

# Installing Docker
sudo curl -fsSL get.docker.com | bash
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -a -G docker vagrant

# Need python >= 3.5. And gcc is required by some packages installed by pip
sudo yum -y install https://dl.iuscommunity.org/pub/ius/stable/CentOS/7/x86_64/ius-release-1.0-15.ius.centos7.noarch.rpm
sudo yum -y install python36u python36u-pip python36u-devel gcc
sudo pip3.6 install --upgrade pip ansible docker docker-compose molecule

# Disabling SELinux
sudo setenforce 0
sudo sed -i 's;SELINUX=enforcing;SELINUX=disabled;' /etc/selinux/config

echo
echo "All set. Now just do"
echo
echo "    vagrant reload"
echo "    vagrant ssh"
echo "    cd /vagrant"
echo "    molecule test"
echo
echo " "

PROVISIONNING

Vagrant.configure(2) do |config|
  config.vm.box = "centos/7"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
    vb.cpus = "1"
  end

  config.vm.hostname = 'ansible.vagrant'
  if Vagrant.has_plugin?("vagrant-hostmanager")
    config.hostmanager.enabled = true
    config.hostmanager.manage_host = true
    config.hostmanager.manage_guest = true
    config.hostmanager.ignore_private_ip = false
    config.hostmanager.include_offline = true
  end

  config.vm.synced_folder ".", "/vagrant", type: "virtualbox"
  config.vm.provision "shell", inline: $provisionning
end
