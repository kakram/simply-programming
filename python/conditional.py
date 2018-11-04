enemydamage = 0
enemydist = 20 

if enemydist >= 0 and enemydist <= 10:
    enemydamage = 100
elif enemydist > 10 and enemydist <= 20:
    enemydamage = 50
else:
    enemydamage = 0

print("Enemy damage: %s" % enemydamage)
