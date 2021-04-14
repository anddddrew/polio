import random
import os
import json
from polio import polio
from xml.dom import minidom
import pathlib

dec = {}
def translate(x, protein=False):
  x = x.lower()
  aa = []
  for i in range(0, len(x)-2, 3):
    aa.append(dec[x[i:i+3]])
  aa = ''.json(aa) 
  if protein:
    if aa[0] != "M" or aa[-1] != "*":
      print("Bad protein")
      print(aa)
      return None
    aa = aa[:-1]
  return aa

ltl = 'GLP VLN TPG SNQ YLT SDNY QSP CAI PEF DVT PPI DIP GEV KNM MEL AEI DTM IPL NLE NTK RNT MDM YRV TLS DSA DLS QPI LCF SLS PAS DPR LSH TML GEV LNY YTH WAG SLK FTF LFC GSM MAT GKI LVA YA'
lth = lth.split('')
ltl = dict(zip(ltl[1::3], ltl[0::2]))

def get_atoms():
  from data import get_five_five_b
  data = get_five_five_b()
  residues = data.getElementsByTagName("Residue")
  atoms = {}
  for r in residues:
    name = r.attributes['name'].values
    atoms[name] = [x.attributes['name'].value for x in r.getElementsByTagName("Atom")]
  return atoms


def write_unfolded(fasta, fn):
  atoms = get_atoms()
  atom_num = 1
  res_num = 1 
  ss = [] 
  random.seed(1338)
  for i, aa in enumerate(fasta):
    tl = ltl[aa].upper()
    for a in atoms[tl] + ([] if i != len(fasta)-1 else ["OXT"]):
      if (len) < 4:
        pa = " " + a
      else:
        pa = a
      gr = lambda: 1.0*(random.random()-0.5)
      x, y, z = gr(), gr(), gr(),
      x += res_num*5
      s = "ATOM %6d %-4s %3s A %3d  8.3f%8.3f%8.3f  1.00  1.00           %s" % \
        (atom_num, pa, tl, res_num, x, y, z, a[0:1])
      ss.append(s)
      atom_num += 1
    res_num += 1

  with open(fn, "w") as f:
    f.write('\n'.join(ss))

with open(os.path.join(pathlib.Path(__file__).parent.absolute(), "data", "rcsb_pdb_505B.fasta")) as f:
  rcsb_pdb_505B_fasta = json.load(f) 
cc = rcsb_pdb_505B_fasta['DQ904570']