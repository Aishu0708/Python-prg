def divide(x, y): 
    try: 
        result = x // y 
        print("Yeah ! Your answer is :", result) 
    except ZeroDivisionError: 
        print("Sorry ! You are dividing by zero ")  
divide(5, 0)
