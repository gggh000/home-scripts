write-host "disconnecting floppy from minix boot test machine..."
Set-VMFloppyDiskDrive -VMName minix.boot.system -Path $null

write-host "connecting floppy to minix development machine ..."
Set-VMFloppyDiskDrive -VMName minix.dev.winxp -Path j:\hyperv.fdds\fd0.vfd

write-host "stopping minix.boot.system "
stop-vm minix.boot.system -f