echo "Employee Payroll Report"
printf "%-5s %-10s %-10s %-10s %-10s %-10s\n" "ID" "Name" "Salary" "Tax" "Bonus" "NetSalary"
while read id name salary
do
    # Tax Calculation
if [ $salary -le 30000 ]; then
        tax=$((salary * 5 / 100))
elif [ $salary -le 60000 ]; then
        tax=$((salary * 10 / 100))
else
        tax=$((salary * 15 / 100))
fi

    # Bonus Calculation
if [ $salary -le 50000 ]; then
        bonus=2000
else
        bonus=5000
fi

    # Net Salary Calculation
net=$((salary - tax + bonus))
printf "%-5s %-10s %-10d %-10d %-10d %-10d\n" \
    "$id" "$name" "$salary" "$tax" "$bonus" "$net"

done < employees.txt
