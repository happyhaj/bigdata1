
import os
import pandas as pd
import numpy as np
from sodapy import Socrata
import sys
from sys import argv
import json
from src.write_json import write_json
from src.print_line_by_line import print_line_by_line


if __name__ == '__main__':
	key = os.environ.get('APP_KEY')
	domain = 'data.cityofnewyork.us'
	id_ = 'nc67-uf89'

	print(f'\nArguments entered: {argv[1:]}\n')

	if len(argv) < 2: #no argv entered
		print(f'\nPlease rerun the program: \n{argv[0]} --page_size(required)\
 --num_pages(optional) --ouput_file_name(optional)\n')
		sys.exit()

	if len(argv) > 1: 
		page_size = int(argv[1])

	if len(argv) > 2:
		num_pages = int(argv[2])
	else: #only page_size entered
		num_pages = np.ceil(48771165/float(argv[1]) ).astype(int) #np.ceil(48771165 / page_size)
		print ('num_pages: ', num_pages)	
	
	client = Socrata(domain, key)
	result = []
	for i in range(num_pages):
		r = client.get(id_,limit=page_size,offset=(i)*page_size,content_type='json')
		if len(argv) < 4: 
			print(f'page{i+1}: \n')
			print_line_by_line(r)
		result.append(r)

	if len(argv) >= 4:
		output_file_name = argv[3]
		write_json(result,output_file_name)
		print(output_file_name, 'has been sucessfully created.')

#testing..................................


		'''for k in r:
			#print(k, '')
			print(type(k))'''


