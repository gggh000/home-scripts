write-host "stopping minix.boot machine..."
stop-vm -force -vmname minix.boot.system

write-host "disconnecting FDD from minix boot machine..."
Set-VMFloppyDiskDrive -VMName minix.boot.system -Path $null
write-host "disconnecting HDD from minix boot machine..."
#Set-VMHardDiskDrive --VMName minix.boot.system -Path $null
Remove-VMHardDiskDrive -VMName minix.boot.system -ControllerType IDE -ControllerNumber 0 -ControllerLocation 0

write-host "connecting FDD to minix development machine..."
Set-VMFloppyDiskDrive -VMName minix.dev.win7 -Path J:\hyperv.fdds\fd0.vfd
write-host "connecting HDD to minix development machine..."
Add-VMHardDiskDrive -VMName minix.dev.win7 -Path J:\hyperv.hdds\1gb.vhdx -ControllerType SCSI -ControllerNumber 0 -ControllerLocation 0

