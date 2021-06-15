# Create your own command-line address-book program using which you can browse, add, modify, 
# delete or search for your contacts such as friends, 
#family and colleagues and their information such as email address and/or phone number. 
#Details must be stored for later retrieval.


# adress book



Me = {
	 
	 "Heine": "Heine@tahmesen.com",
	 "Vimsen": "Vimse@tahmesen.com",
	 "Vlademir": "Vlademir@tahmsen.com"


}



# Let us find heines adress

print ("heine's adress is:  ", Me ['Heine'])
 
 # I want to del Vlademir from my adress book

del Me ['Vlademir']

# To find everyone in the list without printing it
# if using the .format method you need three parantheses because you came with three functions.

print(f'\n There are {len(Me)} contacts in the adress book')


# Let us find heines adress
 
 # I want to del Vlademir from my adress book


# To find everyone in the list without printing it








# I want the adress book to print 5 times
#Me = int(2)

#Sure = input()
#Sure(f'Would you like to see those {Me}?, y/n')
#if Sure == 'y':
	# You have to format it and call it in a dictonary brace/ curly brace.
	#print(f'Contact{Me}')


# To make the list more like a real address book we use this method
# We tell the computer to structere the name address in the ..items()
# then we format it
for name, address in Me.items():
		print('Contact {} at {}'.format(name, address))

Me ['Vim'] = 'Vim@gmail.com'

# The reason we do not use the format method is because wwe never made the list for 'vim'.
if 'Vim' in Me:
	print('\n I added vim to the address book')
	print('Conatact vim at Vim@gmail.com')

print('There are {} contacts in the address book'.format(len(Me)))



















# add  browse