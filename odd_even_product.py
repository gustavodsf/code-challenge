def odd_even_product( list_of_numbers ) :
	acumulator = 1
	result = 0
	for elem in list_of_numbers:
		acumulator = acumulator * elem
		result  = result + elem
	if acumulator % 2 == 0:
		return result
	return 0