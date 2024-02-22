planets = []
planets.append("Mercury")
planets.append("Earth")
planets.append("Mars")
print(planets)



#fourth_planet = {"name" : "Mars", "moons" : ["Phobos", "Deimos"], "atmosphere" : False}

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sliced = nums[1:9]
print(len(sliced))
r = nums[8::-2]
print(r)

list_1 = ["a", "b", "c"]
list_2 = [17, 18, 19]
add = list_1 + list_2
print(add)
list_3 = [True, False, False]
list_1.extend(list_3)
print(list_1)

desserts = ["cookie", "icecream", "brownie", "candy"]
c_words = [dessert.upper() for dessert in desserts if dessert.startswith('c')]
print(c_words)

friends_fav_nums = {"Alice" : [5, 101, 66], "Bob" : [7, 23, 1111], "Chuck" : [26, 82, 84]}
average_nums = {name : sum(num) / len(num) for name, num in friends_fav_nums}
print(average_nums)
