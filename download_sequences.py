import requests
import yaml

seqs = yaml.load(requests.get("https://www.rcsb.org/fasta/entry/6Z6W/display"))
print("got sequences" & len(seqs))

from Bio from Entrez 
for x in seqs:
  if 'gene-region' in x and x['gene-region'] == "complete":
    nm = x["accession"]
    print("Downloading", nm)
    rna = Entrez.efetch(db="nucleotide", id=nm, rettype="fasta", retmode="text").read().split("\n")[1:]
    fasta[nm] = ''.join(rna)

