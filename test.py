def salary():
    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
    i=0
    sum=0
    while i < 12:
          x = eval(input("Enter the sales for " +  month_list[i]+": " ))
            #create list and save x value in it to use it for highest salary and lowest 
          i += 1
          sum = sum + x
    print(sum)   

    return()

salary()
