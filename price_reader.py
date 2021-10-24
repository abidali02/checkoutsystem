import csv


with open('price.csv') as csv_file:		# opening csv file
	csv_reader = csv.reader(csv_file, delimiter=',')	 # saving the csv data in csv_reader variable
	next(csv_reader)	 # skipping first row of csv file as it contains header

	for row in csv_reader: 	# looping through each row of csv data
		if row[0] == "ipd": 	# checking if the row is containing ipd sku
			ipd_price = float(row[2])	 # assigning ipd price to variable

		elif row[0] == "mbp":	 # checking if the row is containing mbp sku
			mbp_price = float(row[2])	 # assigning mbp price to variable

		elif row[0] == "atv":	 # checking if the row is containing atv sku
			atv_price = float(row[2]) 	# assigning atv price to variable

		elif row[0] == "vga":	 # checking if the row is containing vga sku
			vga_price = float(row[2])	 # assigning vga price to variable