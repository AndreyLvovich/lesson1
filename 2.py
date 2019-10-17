

a = 5
b = 6

print('a = ', bin(a))
print('b = ', bin(b))

# логические операции

and1 = bin(a & b)
or1 = bin(a | b)
xor1 = bin(a ^ b)

print(and1)
print(or1)
print(xor1)

print()
# побитовый сдивг

s1 = bin(a >> 2)
s2 = bin(a << 2)

print(s1)
print(s2)
