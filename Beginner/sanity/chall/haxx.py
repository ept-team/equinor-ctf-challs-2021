print("Welcome to Equinor CTF! Enter to get your sanity flag!")
data = input('> ').strip()

flag = open('flag.txt', 'r').read()
print(flag)
