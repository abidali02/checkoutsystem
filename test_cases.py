from total_cost import price_calculator


# test case 1:- SKUs Scanned:atv,atv,atv,vga Total expected: $249.00
input_data = "atv,atv,atv,vga"
print("total cost for test case 1:- " + str(price_calculator(input_data)))

# test case 2:- SKUs Scanned:atv,ipd,ipd,atv,ipd,ipd,ipd Total expected: $2718.95
input_data = "atv,ipd,ipd,atv,ipd,ipd,ipd"
print("total cost for test case 2:- " + str(price_calculator(input_data)))


# test case 3:- SKUs Scanned:mbp,vga,ipd Total expected: $1949.98
input_data = "mbp,vga,ipd"
print("total cost for test case 3:- " + str(price_calculator(input_data)))

# test case 4:- passing valid and invalid sku: it will give invalid warning and give the cost of remaining item
input_data = "mbp,vga,ipd,iphone"
print("total cost for test case 4:- " + str(price_calculator(input_data)))


# test case 5:- passing all invalid SKU, It will give warning for invalid sku and total cost at zero
input_data = "monitor,iphone"
print("total cost for test case 5:- " + str(price_calculator(input_data)))