first=[1,3,-5,8,-4]
second=[7,-4,2,3,8,-6,5]
print("A:",first)
print("B:",second)
print("A ∧ B:",set(first) & set(second))
print("A ∧ B:",set(first) | set(second))
print("A \ B:",set(first) - (set(first) & set(second)) )
