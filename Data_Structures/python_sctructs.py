
# LISTS
lst = [1, 2]
lst2 = ["a","b"]
lst3 = [1,"b"]
lst4 = [i for i in range(0,20)]

#print(lst)
#print(lst2)
#print(lst3)
#print(lst4)

## LIST METHODS
lst.append("a")             # add elemnt
lst.index("a")              # return index
lst.pop(0)                  # remove item at index
lst2 = lst.copy()           # copy form lst to lst2
lst.count("a")              # count specific item
lst.extend(lst2)            # add elemets fo list to the end of the current list
lst.remove("a")             # remove element
lst.reverse()
#lst.sort()
lst.clear()


# DICTIONARIES
dict = {"1":1, "2":2}
dict2 = {"one":1, "two":2}
dict3 = {1:"one", 2:"two"}
dict4 = {1:2,2:3}

#print(dict)
#print(dict2)
#print(dict3)
#print(dict4)

## DICTIONARY METHODS
#dict.values()
#dict.update()
#dict.setdefault()
#dict.popitem()
#dict.pop()
#dict.keys()
#dict.items()
#dict.get()
#dict.fromkeys()
#dict.copy()
#dict.clear()


# TUPLES
tpl = (1,2)
tpl2 = ("a","b")
tpl3 = (1,"b")
tpl4 = (i for i in range(0,20))

#print(tpl)
#print(tpl2)
#print(tpl3)
#print(tpl4)

# SETS
set = {1,2}
set2 = {"a","b"}
set3 = {1,"a"}
set4 = {i for i in range(0,20)}

#print(set)
#print(set2)
#print(set3)
#print(set4)

dict2 = {
    1:1,
    2:5,
    3:4
}
dict = {}
str = "asdasdsafsaffdadfsafsafsafwqjfiqhfiasghbfajfbhsa"
for x in str:
    if x not in dict:
        dict[x] = 1
    else:
        dict[x] += 1
print(dict)