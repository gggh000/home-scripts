if [[ -z $1 ]] ; then
	echo "ERROR: PARAMETER 1  is empty"
	exit 1
fi
START1=`date +%s`
echo Building using the command: $1 $2 $3 $4
$1 $2 $3 $4
time sleep 3
END1=`date +%s`
echo START1 / END1: $START1  / $END1
DURATION=$(($END1 - $START1))
echo Build duration: $DURATION
