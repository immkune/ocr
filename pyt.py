emailist = []

mailist = open(input("List: "))
lime = mailist.read().splitlines()
tot = len(lime)
for line in lime:
    emailist.append(line)
    
print(f'{emailist}')
print(f'{tot}')
