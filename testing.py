ransomNote = "aa"
magazine = "ab"

rhash = dict()
mhash = dict()

for i in range(len(ransomNote)):
    if ransomNote[i] not in rhash:
        rhash[ransomNote[i]] = 1
    else:
        rhash[ransomNote[i]] += 1

for i in range(len(magazine)):
    if magazine[i] not in mhash:
        mhash[magazine[i]] = 1
    else:
        mhash[magazine[i]] += 1

print(rhash, mhash)

for k, v in rhash.items():
    print(k, v)
    print(mhash)
    if (k not in mhash) or (k in mhash and mhash[k] < v):
        print("false")
