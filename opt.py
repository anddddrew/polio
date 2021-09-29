from lib import genome as virus 

virus = virus.get_nuceotideSequence().replace("T", "U")
vaccine = vaccine.replace("Ψ", "U")

# vacine starts at "" with a % chance
vvirus = virus[+len(vaccine)]

print(vvirus)
print(vaccine)
