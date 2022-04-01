log_file = open("um-server-01.txt")
## opening up data file or handling data with python

def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Monday":
            print(line)


sales_reports(log_file)
### for in loop with the sales report file running thru Monday's sales