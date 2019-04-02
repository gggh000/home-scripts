vboxmanage controlvm minix.boot poweroff

start-sleep 5

#working command for adding sata hdd to vbox machine: PS C:\scripts> vboxmanage storageattach minix.boot --type hdd --medium c:\vbox\minix.boot\minix.boot.fat32.vdi --storagectl SATA --port 1 --device 0

write-host "disconnecting HDD from vbox minix.boot machine..."
vboxmanage storageattach minix.boot --type hdd --medium none --storagectl  SATA --device 0 --port 1 
write-host "disconnecting FDD from vbox minix.dev.boot machine..."
vboxmanage storageattach minix.boot --type fdd --medium none --storagectl Floppy --device 0 --port 0

start-sleep 3
write-host "attaching HDD to vbox minix.dev.machine..."
vboxmanage storageattach minix.dev.win7 --type hdd --medium j:\vbox\minix.boot\minix.boot.fat32.vdi --storagectl  SATA --device 0 --port 1 
#write-host "attaching FDD to vbox minix.dev.machine..."
#vboxmanage storageattach minix.dev.win7 --type fdd --medium j:\hyperv.fdds\fd0.vfd --storagectl Floppy --device 0 --port 0
