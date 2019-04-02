$target="minix.boot.2"
$dev="minix.dev.win7.a"
$hdd="d:\hyperv.hdds\fat32.1gb.vhd"
$fdd="d:\hyperv.fdds\fd0.vfd"
$vboxmanage = "C:\Program Files\Oracle\VirtualBox\vboxmanage.exe"
$virtualbox = "C:\Program Files\Oracle\VirtualBox\virtualbox.exe"

write-host "powering off target." + $target

& $vboxmanage controlvm $target poweroff

start-sleep 5

write-host "disconnecting HDD from vbox $target machine..."
& $vboxmanage storageattach $target --type hdd --medium none --storagectl  SATA --device 0 --port 1 
write-host "disconnecting FDD from vbox minix.dev.boot machine..."
& $vboxmanage storageattach $target --type fdd --medium none --storagectl "Floppy" --device 0 --port 0

write-host "connecting FDD to hyper-v minix development machine..."
Set-VMFloppyDiskDrive -VMName $dev -Path $fdd
write-host "connecting HDD to hyper-v minix development machine..."
Add-VMHardDiskDrive -VMName $dev -Path $hdd -ControllerType SCSI -ControllerNumber 0 -ControllerLocation 0