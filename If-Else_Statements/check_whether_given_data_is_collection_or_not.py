# WAP_to_check_whether_given_data_is_collection_or_not.
a = [1,2,3,4]
if type(a) in (int,float,complex,bool):
    print("Not Collection")
else:
    print("Collection")

    # OR
''' 
if type(a) not in (int,float,complex,bool):
    print("Collection")
'''