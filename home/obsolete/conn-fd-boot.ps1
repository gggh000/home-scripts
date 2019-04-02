write-host "disconnecting floppy from minix development machine..."
Set-VMFloppyDiskDrive -VMName minix.dev.winxp -Path $null

write-host "connecting floppy to minix boot test machine..."
Set-VMFloppyDiskDrive -VMName minix.boot.system -Path j:\hyperv.fdds\fd0.vfd

write-host "starting minix.boot.system"
start-vm minix.boot.system
