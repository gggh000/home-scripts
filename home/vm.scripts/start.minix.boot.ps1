$target="minix.boot.2"
$dev="minix.dev.win7.a"
$hdd="d:\hyperv.hdds\fat32.1gb.vhd"
$fdd="d:\hyperv.fdds\fd0.vfd"
$vboxmanage = "C:\Program Files\Oracle\VirtualBox\vboxmanage.exe"
$virtualbox = "C:\Program Files\Oracle\VirtualBox\virtualbox.exe"

write-host "disconnecting FDD from minix development machine..."
Set-VMFloppyDiskDrive -VMName $dev -Path $null
write-host "disconnecting HDD from minix development machine..."
Remove-VMHardDiskDrive -VMName $dev -ControllerType SCSI -ControllerNumber 0 -ControllerLocation 0 

write-host "attaching HDD to vbox $target machine..."
& $vboxmanage storageattach    $target --type hdd --medium $hdd --storagectl SATA --device 0 --port 1 
write-host "attaching FDD to vbox $target machine..."
& $vboxmanage storageattach    $target --type fdd --medium $fdd --storagectl "Floppy" --device 0 --port 0

start-sleep 10
& $virtualbox --startvm $target