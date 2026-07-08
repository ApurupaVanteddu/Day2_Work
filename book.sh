#!/bin/bash

FILE="book.txt"

###########################################
# Display all books
###########################################
display_books() {

    echo "=========== All Books ==========="

    cat "$FILE"

}

###########################################
# Search Book
###########################################
search_book() {

    echo "Enter Book Name:"
    read name

    if grep -i "$name" "$FILE"
    then
        echo "Book Found"
    else
        echo "Book Not Found"
    fi

}

###########################################
# Count books - Out of Stock
###########################################
count_books() {

    count=$(grep -c "OutOfStock" "$FILE")

    echo "Absent Employees : $count"

}

###########################################
# Replace OutOfStock with Available
###########################################
update_books() {

    echo "Enter Book ID:"
    read id

    sed -i "/^$id,/ s/OutOfStock/Available/" "$FILE"

    echo "Book Updated Successfully"

}

###########################################
# Total Inventory Value
###########################################
calculate_value() {

    total=$(awk -F',' '$4=="Available" {sum+=$5} END {print sum}' "$FILE")

    echo "Total Inventory value : Rs.$total"

}

###########################################
# Display Book by Category
###########################################
book_category() {

    echo "Enter Category:"
    read dept

    awk -F',' -v dep="$dept" '

    BEGIN{
        print "Employees in Department:",dep
    }

    $3==dep{
        print $0
    }

    ' "$FILE"

}

###########################################
#Costliest Book
###########################################
costliest_book() {

    awk -F',' '

    BEGIN{
        max=0
    }

    {
        if($5>max)
        {
            max=$5
            emp=$2
        }
    }

    END{
        print "Costliest Book:",emp
        print "Book :",max
    }

    ' "$FILE"

}

###########################################
# Menu
###########################################

while true
do

echo
echo "====================================="
echo " Bookstore Management "
echo "====================================="
echo "1.Display all books"
echo "2.Search for a book"
echo "3.Count OutOfStock Employees"
echo "4.Update Stock Status"
echo "5.Total Inventory Value"
echo "6.Display book by category"
echo "7.Costliest book"
echo "8.Exit"

echo "Enter Choice:"
read choice

case $choice in

1)
display_books
;;

2)
search_book
;;

3)
count_books
;;

4)
update_books
;;

5)
calculate_value
;;

6)
book_category
;;

7)
costliest_book
;;

8)
echo "Thank You"
break
;;

*)
echo "Invalid Choice"

esac

done
