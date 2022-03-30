# assign the content of a file called "um-server-01.txt to variable log_file"
log_file = open("um-server-01.txt")


def generate_sales_reports(log_file):  # define a func to generate sales report
    for line in log_file:  # to iterate through each line in the txt file
        line = line.rstrip()  # to remove space in the line
        # assign a slice from each line starting from index 0 to 3 with day variable.
        day = line[0:3]
        if day == "Mon":  # branching if it's Tuesday, then print line
            print(line)


generate_sales_reports(log_file)  # call the function
