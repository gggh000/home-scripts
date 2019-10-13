ROCM_INSTALLATION_PHASE_FLAG_FILE=/opt/rocm-installation_phase
ROCM_INSTALLATION_PHASE=""

ROCM_INSTALLATION_PHASE=`cat $ROCM_INSTALLATION_PHASE_FLAG_FILE`

if [[ $ROCM_INSTALLATION_PHASE_FLAG -eq "" ]]  ; then
	echo "ROCM installation phase has just started..."
	sleep 5
	sudo apt update
	sudo apt dist-upgrade
	sudo apt install libnuma-dev -y
	echo 1 > $ROCM_INSTALLATION_PHASE_FLAG_FILE
	sudo reboot
elif [[ $ROCM_INSTALLATION_PHASE_FLAG -eq 1 ]] ; then
	echo "ROCM installation phase 1..."
	sleep 5
	wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
	echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list
	sudo apt update
	sudo apt install rocm-dkms -y
	echo groups:
	groups
	sleep 5
	sudo usermod -a -G video $LOGNAME 
	echo 'ADD_EXTRA_GROUPS=1' | sudo tee -a /etc/adduser.conf
	echo 'EXTRA_GROUPS=video' | sudo tee -a /etc/adduser.conf
	echo 2 > $ROCM_INSTALLATION_PHASE_FLAG_FILE
elif  [[ $ROCM_INSTALLATION_PHASE_FLAG -eq 2 ]] 
	echo "ROCM installation phase 2, test installation..."
	/opt/rocm/bin/rocminfo 
	/opt/rocm/opencl/bin/x86_64/clinfo 
	echo 'export PATH=$PATH:/opt/rocm/bin:/opt/rocm/profiler/bin:/opt/rocm/opencl/bin/x86_64' | sudo tee -a /etc/profile.d/rocm.sh
fi




