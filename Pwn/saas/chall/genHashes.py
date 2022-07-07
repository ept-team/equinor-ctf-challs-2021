import hashlib

def hash_string(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()


pwds = [
"HOLLY014",
"shockie1",
"tutifran",
"hopkins07",
"polla2",
"apai",
"vinking1",
"hyearmo",
"mealcreep",
"gazzy-0922",
"suuperlongpassw0rdthatyouwillneverbr3ak_lolkekburasl!"]


for pwd in pwds:

    hash = hash_string(pwd)
    kek =[hash[i:i+2] for i in range(0, len(hash), 2)]
    for k in kek:
        print(f'\\x{k}', end='')
    print()