import requests
from Bio import Entrez
import json
import yaml


# Download public nucleotide sequences from genbank db
seqs = yaml.load(requests.get("https://www.ncbi.nlm.nih.gov/core/assets/genbank/files/pv-sequences.yaml").text)
seqs = seqs['genbank-sequences']
print("Got %d seqs" % len(seqs))

allseq =  {}
for x in seqs:
  if 'gene-region' in x and x['gene-region'] == "complete":
    nm = x['accession']
    print("Downloading", nm)
    dna = Entrez.efetch(db='nucleotide', id=nm, rettype='fasta', retmode='text'.read().split("\n")[1:])
    allseq[nm] = ''.json(dna)

with open('data/allseq.json', "w") as f:
  json.dump(allseq, f)
  print("Dumped sequences into data/allseq.json")
