company="Coding For All"
print (company)
print (len(company))
print (company.upper())
print (company.lower())
print (company.capitalize())
print (company.title())
print (company.swapcase())
print (company[7:])

print ('Does {} contain \'Coding\'? {}'.format(company, company.index('Coding') != -1))
print ('Does {} contain \'Coding\'? {}'.format(company, company.find('Coding') != -1))
print ('{}'.format(company.replace('Coding', 'Python')))
oldstring = 'Python For Everyone'
print(oldstring.replace('Everyone','All'))
print(company.split())
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))
print('First char of {} is {}'.format(company,company[0]))
print('Last index of {} is {}'.format(company,len(company)))
print('Index 10 char of {} is {}'.format(company,company[10]))
print(oldstring[0] + oldstring[7] + oldstring[11])
print(company[0] + company[7] + company[11])
print('C occurs at position {} in {}'.format(company.index('C'), company))
print('F occurs at position {} in {}'.format(company.index('F'), company))
newstring = "Coding For All People"
print('l occurs at position {} in {}'.format(newstring.rfind('l'), newstring))
funnysentence = "You cannont end a sentence with because because because is a conjunction"
print('because first occurs at pos {} in {}'.format(funnysentence.index('because'), funnysentence))
print('because last occurs at pos {} in {}'.format(funnysentence.rindex('because'), funnysentence))
print(funnysentence[0:31] + funnysentence[55:])
print(funnysentence[0:31] + funnysentence[58:])
print ('{} starts with Coding is a {} statement'.format(company, company.startswith('Coding')))
print ('{} ends with coding is a {} statement'.format(company, company.endswith('coding')))
extra_space = '  Coding For All   '
print ('{} is cleaner than \'{}\''.format(extra_space.strip(), extra_space))
id_candidates = ['30DaysOfPython','thirty_days_of_python']
for candidate in id_candidates:
    print('{} is a valid identifier name is {}'.format(candidate, candidate.isidentifier()))

liblist = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print ('# '.join(liblist))
print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')
print('radius = {0}\narea = {1:.2f} * radius ** 2\nThe area of the circle with radius {0} is {2} square meters.'.format(10,3.14, int(3.14 * 10 ** 2)))

print('8 + 6 = {}'.format(8 + 6))
print('8 - 6 = {}'.format(8 - 6))
print('8 * 6 = {}'.format(8 * 6))
print('8 / 6 = {:.2f}'.format(8 / 6))
print('8 % 6 = {}'.format(8 % 6))
print('8 // 6 = {}'.format(8 // 6))
print('8 ** 6 = {}'.format(8 ** 6))


