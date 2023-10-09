

#Dictionaries

Band = {
"vocals": "Plant",
"guitar": "Page"
}

band2 = dict(vocals = "plant", guitar = "page")

print(Band)
print(band2)

print(type(Band))
print(len(Band))

print(Band["vocals"])
print(Band.get("guitar"))

#list all keys
print(Band.keys())

#list all keys
print(Band.values())

#list of key/value pairs in list
print (Band.items())

#verify a key exist
print("guitar" in Band)
print("Trinagle" in Band)

#change values

Band["vocals"]= "Covardel"
Band.update({"bass" : "JPJ"})

print(Band)

#rmeove iterms

print (Band.pop("bass"))
print (Band)

Band ["drums"] = "Bonhana"
print(Band)

print(Band.popitem())
print (Band)

#delete and clear 
Band ["drums"] = "Bonhana"
del Band ["drums"]
print (Band)

band2.clear()
print(band2)

del band2

#copy dictionaries

#band2 = Band #creates a reference
#print ("Bad copy!")

#print (Band)
#print (band2)

#band2["drums"] = "Dave"
#print (Band)

band2 = Band.copy()

band2["drums"] = "Dave"

print (Band)
print (band2)


#or constructor for dictrionary

band3 = dict(Band)
print (band3)



#nested dictionary

member1 = {"name" : "Plant",
           "intrument" : "vocals"
           }

member2 = {"name" : "Page",
           "intrument" : "guitar"
           }

band = {"member1" : member1,
           "member2" : member2
           }

print (band)
print (band["member1"]["name"])

#Sets

numbs = {1,2,3,4}

numbs2 = set((1,2,3,4))

print(numbs)
print(numbs2)

#no diplicates

numbs = {1,3,3,4}
print(numbs)


numbs = {1, True,2,False,3,4,0}
print (numbs)
print (2 in numbs)


#add a new element

numbs.add(8)
print (numbs)

morenumbs = {5,6,7}
numbs.update(morenumbs)
print(numbs)

one = {1,2,3}
two = {5,6,7}

mynewset = one.union(two)
print (mynewset)



one = {1,2,3}
two = {2,3,7}

one.intersection_update(two)
print(one)


one = {1,2,3}
two = {2,3,7}

one.symmetric_difference_update(two)
print(one)





