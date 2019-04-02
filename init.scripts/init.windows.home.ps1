$netUseDrvs = "z:", "y:", "x:", "w:", "t:", "s:", "r:", "p:", "o:"
$netUsePaths = "\\netgear-san", "\\10.0.0.27\cdrv", "\\10.0.0.27\a", "\\minix-dev-win7\a", "\\minix-dev-win7\cdrv", "\\hp2012\j", "\\hp2012\c", "\\win7-amd-pc\c", "\\10.0.0.22\linshare"
$netUseUsers = "Administrator", "guyen", "guyen", "guyen", "guyen", "Administrator", "Administrator", "guyen", "root"

echo on

for ($counter=0; $counter -lt $netUseDrvs.length; $counter++)
{
	write-host "----------------"
	write-host $counter ": Settin net share: "$netUseDrvs[$counter] " path:" $netUsePaths[$counter] " user:" $netUseUsers[$counter]
	net use /delete $netUseDrvs[$counter] /y
	$fuckyou=1
	$userInfo="/USER:"+$netUseUsers[$counter]	
	net use $netUseDrvs[$counter] $netUsePaths[$counter] "/PERSISTENT:yes" $userInfo
}

net use 
net user administrator /ACTIVE:yes
dir c:


