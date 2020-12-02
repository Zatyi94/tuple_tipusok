# a tuple ugyanúgy elemeket tartalmaz, mint a lista
my_tuple = (4, "szoveg", True, [])

print(my_tuple)
# elemeket kiválasztani uaúgy lehet, mint a listánál...
print(my_tuple[1])

# a tuple elemein nem lehet módosítani, újat hozzáadni, elvenni... stb
# a tuple csak olvasható (read only)
# pl. my_tuple.append(0) << ERROR!
# my_tuple[1] = 'e' << ERROR!

# sokkal hatékonyabb memóriakezelés szempontjából
# hatékonyabban van a memóriában eltárolva
# gyorsabb vele dolgozni
# mert nem lehet módosítani

# át tudjuk alakítani a tuple-t listává:
my_list = list(my_tuple)
print(my_list)