'''Welcome To THE DUBAI MALL'''


# dictionary to store product("name"), quantity("quant"), price("price") with empty list as their values
a ={"name":[], "quant":[], "price":[]} 

# converting dictionary to list for further updation 
b = list(a.values()) 
  
# variable value from dictionary 'a' 
na = b[0] 
qu = b[1] 
pr = b[2] 

# This loop terminates when user select 2.EXIT option when asked in try it will ask user for an option as an integer (1 or 2) if correct then proceed else continue asking options 
while True: 
    try: 
        ch = int(input("1.ADD \n2.EXIT \n Enter your choice : ")) 
    except ValueError: 
        print("\n ERROR: Choose only digits from the given option") 
        continue
    else:
        if ch == 1:        
   
            # input products name                 
            pn = input("Enter product name : ")  
            # input quantity of product 
            q = input("Enter quantity : ") 
            # input price of the product 
            p = float(input("Enter price of the product : ")) 
            
            # checks if product name already in list 
            if pn in na:   
                # find the index of that product 
                ind = na.index(pn)   
  
                # remove from index of the product 
                qu.remove(qu[ind]) 
                pr.remove(pr[ind])   
  
                # insert new value given by user earlier 
                qu.insert(ind, q)    
                pr.insert(ind, p)
        
            else: 
                    # append value of in "name", "quantity", "price" 
                    na.append(pn)   
   
                    # as na = b[0] it will append all the value in the 
                    # list eg: "name":["rice"] 
                    qu.append(q)    
  
                    # same for quantity and price 
                    pr.append(p)
        
        else:
            break
            
# print final list
for i in range(len(na)):  
    print(na[i], qu[i], pr[i]) 
