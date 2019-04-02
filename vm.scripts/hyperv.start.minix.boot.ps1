write-host "disconnecting FDD from minix development machine..."
Set-VMFloppyDiskDrive -VMName minix.dev.win7 -Path $null
write-host "disconnecting HDD from minix development machine..."
Remove-VMHardDiskDrive -VMName minix.dev.win7 -ControllerType SCSI -ControllerNumber 0 -ControllerLocation 0 

write-host "connecting FDD to minix boot machine..."
Set-VMFloppyDiskDrive -VMName minix.boot.system -Path J:\hyperv.fdds\fd0.vfd
write-host "connecting HDD to minix boot machine..."
Add-VMHardDiskDrive -VMName minix.boot.system -Path J:\hyperv.hdds\1gb.vhdx -ControllerType IDE -ControllerNumber 0 -ControllerLocation 0

write-host "starting minix.boot machine..."
start-vm -vmname minix.boot.system
