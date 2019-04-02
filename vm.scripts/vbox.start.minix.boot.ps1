
write-host "disconnecting HDD from vbox minix.dev.machine..."
vboxmanage storageattach minix.dev.win7 --type hdd --medium none --storagectl SAS --device 0 --port 1 
#write-host "disconnecting FDD from vbox minix.dev.machine..."
#vboxmanage storageattach minix.dev.win7 --type fdd --medium none --storagectl Floppy --device 0 --port 0

write-host "attaching HDD to vbox minix.boot machine..."
vboxmanage storageattach    minix.boot --type hdd --medium j:\vbox\minix.boot\minix.boot.fat32.vdi --storagectl SATA --device 0 --port 1 
write-host "attaching FDD to vbox minix.boot machine..."
vboxmanage storageattach    minix.boot --type fdd --medium j:\hyperv.fdds\fd0.vfd --storagectl Floppy --device 0 --port 0

start-sleep 10
vboxmanage startvm minix.boot
