print(""" ------------------------------------------------------
		WELL COME TO E-COMMERCE SHOPPING PLACE
		------------------------------------------------------------		
	""")
T_shirt = ["yellow_shirt :500$", "blue_shirt: 600$", "red_shirt: 450$", "green_shirt: 350$"]
shirt_price = [500,600,450, 350]
phone = ["samsung A06: 1000$", "apple 17 pro max: 260$", "techono ultra: 200$", "ZTE pro: 490$"]
phone_price = [1000,260,200,490]
chooced_shirt = []
chooced_phone =[]
choooced_price_shirt =[]
choooced_price_phone = []
show_shirt = str(input("do u want to see all T-shirts (yes/ no) :")).lower()
if show_shirt == "yes":
	for shirt in T_shirt:
		print(shirt)
	shirt_choice = str(input("which shirt did you chooce write the number only ex: 1,3 :"))
	index = shirt_choice.split(",")
	for shirts in index:
		n = int(shirts) - 1
		selected_item = T_shirt[n]
		print("you choice : ", selected_item)
		chooced_shirt.append(selected_item)
		selected_item_price = shirt_price[n]
		choooced_price_shirt.append(selected_item_price)
else:
	print("ok cheke out other products")
show_phone = str(input("do u want to see all phones (yes/ no) :")).lower()
if show_phone == "yes":
	for phones in phone:
		print(phones)
	phone_choice = str(input("which phone did you chooce write the number only ex: 1,3 :"))
	index = phone_choice.split(",")
	for phones in index:
		n = int(phones) - 1
		selected_item = phone[n] 
		print("you choice : ", selected_item)
		chooced_phone.append(selected_item)
		selected_item_price = phone_price[n]
		choooced_price_phone.append(selected_item_price)
else:
	print("ok cheke out other products")
print(chooced_shirt,chooced_phone)
print(f"shirt price : {sum(choooced_price_shirt)} \n phone price : {sum(choooced_price_phone)} \n total price : ", sum(choooced_price_phone) + sum(choooced_price_shirt))