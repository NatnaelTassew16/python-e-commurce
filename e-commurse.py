import json
import sys
import hashlib
with open("data.json", "r") as file:
    data = json.load(file)
stored_hash = "4bbc1ade684238bd8d4d4cad6348aabd48065ac4766fecf345f4a54a656cc0fa"
if len(sys.argv) == 2:
	password = sys.argv[1]
	input_hash = hashlib.sha256(password.encode()).hexdigest()
	if input_hash == stored_hash:
		print("----------------YOU ARE AN ADMIN-----------------")
		catagory = list(data.keys())	
		add_product = input("Do you want add new prodcut on catagory Yes/no: ").lower()
		if add_product == "yes":
			while True:
				for i, products in enumerate(data,1 ):
					print(f"{i}.{products}")
				choice_catagory =int( input("please choice catagory : "))
				shop_data = str(catagory[choice_catagory - 1])
				products_data = data[shop_data]
				product_name = input(f"please write the name of {shop_data} :")
				product_price =int(input("please write the price :"))
				products_data[product_name] = product_price
				with open("data.json", "w") as file:
					json.dump(data, file )
				again = input("do u want to continue adding products yes/no: ")
				if again.lower() != "yes":
					break
	
		remove_data =input("Do you want delete a prodcut yes/no: ").lower()
		if remove_data == "yes":
			while True:
				for i, products in enumerate(data,1 ):
					print(f"{i}.{products}")
				delete_product = input("from which product do you want to delete : ").lower()
				product_data = data[delete_product]
				for i, (name, price) in enumerate(product_data.items(), 1):
						print(f"{i}. {name}: {price}")
				delete_item = input("please write the product name (spelling is sensitive) :")
				if delete_item in data[delete_product]:
						del data[delete_product][delete_item]
						print(f"{delete_item} was deleted")
						with open("data.json", "w") as file:
							json.dump(data,file)
				else:
					print("product was not found")
				again = input("do u want to continue deleting products yes/no: ")
				if again.lower() != "yes":
					break
		add_subprodcut = input("do you want add new sub product yes/no :").lower()
		if add_subprodcut == "yes":
			while True:
				subproduct_name = input("please inter the name of sub product :")
				items_name = input("write items name ex: apple,400,mango,800 :")
				items = items_name.split(",")
				data[subproduct_name] = {}
				for i in range(0, len(items), 2):
					key = items[i].strip()
					value = int(items[i+1])
					data[subproduct_name][key] = value
					with open("data.json", "w") as file:
							json.dump(data,file)
				again = input("do u want to continue deleting products yes/no: ")
				if again.lower() != "yes":
					break
	print("good bye")
	quit()
else:
	print("--------------WELL COME-------------")
choice_product = {}
choice_price = []
catagory = list(data.keys())
while True:
	for i, products in enumerate(data,1 ):
		print(f"{i}.{products}")
	choice_catagory =int( input("please choice catagory : "))
	shop_data = str(catagory[choice_catagory - 1])
	products_data = data[shop_data]
	for i, (name, price) in enumerate(products_data.items(), 1):
		print(f"{i}. {name}: {price}")
	item_choice = str(input(f"which {shop_data} did you chooce write the number only ex: 1,3 :"))
	index = item_choice.split(",")
	for items in index:
		try:
			n = int(items)  - 1
			selected_item = list(products_data.items())[n]
			print("you choice : ", selected_item)
			choice_product.update({selected_item})
			selected_price = list(products_data.values())[n]
			choice_price.append(selected_price)
		except ValueError:
			print("please time only the number like this '1'")
	buy_other = input("Do u want buy other products ? if yes type yes ")
	if buy_other.lower() == "no":
		print(" well we will calculate total price")
		break
print("--------------------TOTAL CHOICE -------------")
for i, (name, price) in enumerate(choice_product.items(), 1):
	    print(f"{i}. {name}: {price}$")

print("-----------------TOTAL PRICE--------------------")
print(f"total price : ", sum(choice_price) )
