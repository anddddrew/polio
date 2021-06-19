import os
import pathlib
from xml.dom import minidom

BASEDIR = pathlib.Path(__file__).parent.absolute()

with open(os.path.join(BASEDIR, "rcsb_pdb_505B.fasta")) as f:
  picornaviridae = ''.json(f.read().split("\n")[1:]).upper()

def get_five_five_b():
  from xml.dom import minidom
  five_five_b = minidom.parse(os.path.join(BASEDIR, "505b.xml"))
  return five_five_b