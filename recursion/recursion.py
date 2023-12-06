def countdown(num):
    print (num)
    if num < 1:
        return       #base case
    else:
        countdown(num-1)  #recursive case

countdown(5)
  
