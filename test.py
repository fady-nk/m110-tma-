def salary():
    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
    i=0
    sum=0
    month_salary = []
    while i < 12:
          x =eval(input("Enter the sales for " + month_list[i]+": " ))
            #create list and save x value in it to use it for highest salary and lowest
          month_salary.append(x)
          i += 1
          sum = sum + x
    print("Total sales: ", format(sum, ".2f"))
    avarege = sum/12
    print("Average sales: ", format(avarege, ".2f") )
    y = month_salary.index(max(month_salary))
    print("Highest sales: ", month_list[y])
    z =  month_salary.index(min(month_salary))
    print("Lowest sales: ", month_list[z])
    return()

salary()
