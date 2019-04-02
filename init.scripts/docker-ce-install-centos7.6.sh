yum-config-manager enable extras
yum install -y yum-utils   device-mapper-persistent-data   lvm2
yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
yum-config-manager --enable docker-ce-test
yum-config-manager --enable docker-ce-nightly
yum install docker-ce docker-ce-cli containerd.io
systemctl start docker
chkconfig docker on
docker run hello-world
