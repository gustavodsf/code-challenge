def highest_revenue_item( data ) :
	count_dict = {}
	price_dict = {}
	
	row_data = data.split('\n')
	for row in row_data:
		txn = row.split(',')
		product_id = txn[0]
		price = txn[1]
		
		if product_id in count_dict:
			count_dict[product_id] += 1
		else:
			count_dict[product_id] = 1
			price_dict[product_id] = int(price)
	

	most_common_item = '0'
	most_revenue = 0
	
	for product in count_dict:
		product_revenue = price_dict[product] * count_dict[product]
		if product_revenue > most_revenue:
			most_revenue = product_revenue
			most_common_item = product
		
	if most_revenue != 0:
		return int(most_common_item)