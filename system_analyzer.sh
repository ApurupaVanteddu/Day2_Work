info_count=0
error_count=0
warn_count=0

#Function to analyze the log line
analyze_log(){
line=$1

if echo "$line" | grep -q "INFO"
then
((info_count++))
elif echo $line | grep -q "WARNING"
then
((warn_count++))
else
((error_count++))
fi
}

#Function to determine the system status
check_status(){
if [[ $error_count -gt 10 ]]
then
	status="Critical"
elif [[ $error_count -gt 0 ]]
then
	status="Warning"
else
	status="Healthy"
fi
}

#Read Input file
echo "Enter log file: "
read logfile

if [[ ! -f $logfile ]]
then

	echo "File not exist"
	exit
fi


#loop through the file
while read line
do
analyze_log "$line"
done < $logfile

#Determine Status
check_status

#Generate Report
{
echo "System : Log Analyzer report"
echo "============================"
echo "INFO count: $info_count"
echo "WARNING count: $warn_count"
echo "WARNING count: $error_count"
echo
echo "System status: $status"
} > report.txt

echo "Report generated: report.txt"


