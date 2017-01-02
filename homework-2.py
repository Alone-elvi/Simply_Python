years_list = [1974, 1975, 1976, 1977, 1978]
print(years_list[3])
print(years_list[-1])

things = ["mozzarella", "cinderella", "salmonella"]

things[1].capitalize()
print(things)
things[0].upper()
print(things)
del things[2]
print(things)

surprise = ['Groucho', 'Chico', 'Harpo']
surprise[-1].lower()
surprise[-1].capitalize()
print(surprise)

e2f = {"dog": "chien", "cat": "chat", "walrus": "morse"}
print(e2f['walrus'])

f2e = {}

for key, var in e2f.items():
    f2e[var] = key

print(f2e['chien'])

for key in e2f.keys():
    print(key)

life = {'animals': {"cats": ["Henri", "Grumpy", "Lucy"]},
        'plants': {},
        'other': {}
        }

print(life.keys())
print(life['animals'])
print(life['animals']['cats'])

