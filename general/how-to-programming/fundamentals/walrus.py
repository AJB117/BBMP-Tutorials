import random

def disaster_report():
    r = random.randint(0, 1)
    return r

def keep_living():
    print('nothing to see here...')

# update the code below using the walrus operator so you don't need line 11 and 14
disaster_has_struck = disaster_report()
while not disaster_has_struck:
    keep_living()
    disaster_has_struck = disaster_report()

print('Everything is in shambles')
