
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

running = True

# Let us find heines adress

print ("heine's adress is:  ", Me ['Heine'])
 
 # I want to del Vlademir from my adress book

del Me ['Vlademir']

# To find everyone in the list without printing it

print("Contact {} at {}".format(len(Me))