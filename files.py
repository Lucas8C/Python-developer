# open files and read contents in boys 

with open('data/1880-boys.txt') as f:
    boys = f.read()

print(boys) 

with open('data/1880-girls.txt') as f:
    girls = f.read()

# print(girls)
# print('----')
# print(boys)

with open('data/1880-all.txt', "w") as f:
    f.write(boys+"\n"+girls)