from lib import genome as virus 

virus = virus.get_nuceotideSequence().replace("T", "U")
vaccine = vaccine.replace("Ψ", "U")

# We got to find the start of the vaccine and the spike of the protein and a percentage match.
# vacine starts at "" with a % chance
vvirus = virus[+len(vaccine)]

print(vvirus)
print(vaccine)