contacts={"Ravi":"9876543211","Raju":"1234567890"}
print("original contacts:",contacts)
contacts["sita"]="9988554466"
print("After adding:",contacts)
print("Ravi's phone number:",contacts["Ravi"])
contacts["Ravi"]="9000011111"
print("After upadating:",contacts)
del contacts["Raju"]
print("After deleting:",contacts)
      
