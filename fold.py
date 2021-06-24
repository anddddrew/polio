from simtk.openmm.app import *
from simtk.openmm import *
from simtk.unit import *
from sys import stdout
from lib import write_unfolded
import sys
import os as os
import argparse

parser = argparse.ArgumentParser(description="Fold proteins.")
parser.add_argument("--scratch", action="store_true")
parser.add_argument("--temp", type=int, default=300)
parser.add_argument("--step", type=int, default=100000, help="2500000000 Should fold the protein")
parser.add_argument("--fasta", type=str, default=None)
parser.add_argument("--writes", type=int, default=100, help="Default is 100.")

try:
  platform = Platform.getPlatformByName('CUDA')
except LookupError or Exception:
  platform = Platform.getPlatformByName('OpenCL')

if args.scratch:
  if args.fasta != None:
    fasta = args.fasta

  else:
     protein_fasta =  'proteins/data/6z6w.fasta'
     fasta = open(protein_fasta).read().split("\n")[1]

  print("Folding %s" % fasta)
  write_unfolded(fasta, "/temp/unfolded.pdb")
  pdb = PDBFile("/temp/unfolded.pdb")

else:
  pdb = PDBFile(args.pdb)


# Force fields is a method to estimate the force between atoms within molecules.
force_field = ForceField('5o5b.xml')

modeller = Modeller(pdb.topology, pdb.positions)
# Add the hydrogens to the force field (the protein)
modeller.addHydrogens(force_field)
print(modeller.topology)

system = force_field.createSystem(modeller.topology,
  implicitSolvent=OBC2,
  nonbondedMethod=NoCutoff, nonbondedCutoff=1*nanometer,
  constraints=HBonds)
