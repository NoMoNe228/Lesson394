from cho import salary,hello_who

#print(hello_who('Max'))

if salary != 20:
    print('ERROR')
if hello_who('Max') != 'Hello,Max':
    print('LOX')
else:
    print('NICE')
if hello_who('Leo') != 'Hello,Leo':
    print('FAILED')
else:
    print('GOOD')

assert hello_who('Max') == 'Hello, Max', 'Hello who error'
assert hello_who('Leo') == 'Hello, Leo', 'Hello who error'
assert hello_who('Nikita') == 'Hello, Nikita', 'Hello who error'
assert salary(2,1) == 4
assert salary(2, 2) == 8