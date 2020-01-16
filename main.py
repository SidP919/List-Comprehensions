names = ["Jennifer", "Susan", "Jane", "Sophie"]

#Example01:
l = []

for person in names:
  l.append(person)
print(l)
print()

#With List comprehensions:-------->
print("With List comprehensions: " + str([person for person in names]))
print()

#Example02:
l=[]
for person in names:
  l.append(person + ' dumped me.')
print(l)


print("With List comprehensions: " + str(
  [person + ' dumped me.' for person in names]
  )
)
print()

#Example03:
movies_and_ratings = {"3 Idiots":9.5, "Sholay":8.5, "Swades":8, "Raone":7}
print(movies_and_ratings)

l = []
for movie in movies_and_ratings:
  if movies_and_ratings[movie]>8:
    l.append(movie)
print(l)
print("With List comprehensions: " + 
  str(
  [movie for movie in movies_and_ratings if movies_and_ratings[movie]>8.5]
  )
)
print()