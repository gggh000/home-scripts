$netUseDrvs = "z", "y", "x", "w", "t","s","r","p","o","n","m"
$netUsePaths = "\\netgear-san", "\\10.0.0.27\cdrv", "\\10.0.0.27\a", "\\10.0.0.17\a", "\\10.0.0.17\cdrv", "\\hp2012\j", "\\hp2012\c", "\\win7-amd-pc\c", "\\10.0.0.22\linshare"
$netUseUsers = "Administrator", "guyen", "guyen", "guyen", "guyen", "Administrator", "Administrator", "guyen", "guyen", "root"

for ($counter=0; $counter -lt $netUseDrvs.length; $counte++)
{
	write-host $netUseDrvs[$counter] " : " $netUsePaths[$counter] " : " $netUseUsers[$counter]
}

net use delete z:
net use z: \\netgear-san\documents /PERSISTENT:yes /USER:Administrator

net use delete w:
net use w: \\10.0.0.27\cdrv /PERSISTENT:yes

net use delete m:
net use m: \\10.0.0.27\a /PERSISTENT:yes

net use delete n:
net use n: \\10.0.0.17\cdrv /PERSISTENT:yes

net use delete w:
net use w: \\10.0.0.17\cdrv /PERSISTENT:yes


net use delete y:
net use y: \\hp2012\j /PERSISTENT:yes /USER:Administrator

net use delete n:
net use n: \\hp2012\c /PERSISTENT:yes /USER:Administrator

net use delete p:
net use p: \\win7-amd-pc\c /PERSISTENT:yes /USER:Administrator

net use delete r:
net use r: \\10.0.0.22\linshare /PERSISTENT:yes /USER:Administrator

net user administrator /ACTIVE:yes
dir c:

net use
