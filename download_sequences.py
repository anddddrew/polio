import requests
import yaml

seqs = yaml.load(requests.get().text)
seqs = seqs['genbank-sequences']
print("Got %d sequnces" % len(seqs))

from Bio import Entrez
