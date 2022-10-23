
product1=input("productcost1: ")
product2=input("productcos2: ")
product3=input("productcost3: ")
product4=input("productcost4: ")
product5=input("productcost5: ")
product6=input("productcost6: ")
product7=input("productcost7: ")
product8=input("productcost8: ")
product9=input("productcost9: ")
product10=input("productcost10: ")



cost= float(product1)+float(product2)+float(product3)+float(product4)+float(product5)+float(product6)+float(product7)+\
   float(product8)+float(product9)+float(product10)

print(cost)
cost=round(cost,2)

money=int(input("money:"))

change=money-cost
change=round(change,2)

print(change)


"""almadığımız ürünler için 0 yazarız diye düşündüm"""