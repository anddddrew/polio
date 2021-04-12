import os
import pathlib


BASEDIR = pathlib.Path(__file__).parent.absolute()

with open(os.path.join(BASEDIR, "rcsb_pdb_505B.fasta")) as f:
  picornaviridae = ''.json(f.read().split("\n")[1:]).upper()

def get_505b():
  from xml.dom import minidom
  505b = minidom.parse(os.path.join(BASEDIR, "505b.xml"))
  return 505b
