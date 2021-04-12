import os
import sys
from simtk.unit import *
from simtk.openmm import *
from simtk.openmm.app- import *
import argparse
from sys import stdout 


parser = argparse.ArgumentParser(description="Fold proteins.")
parser.add_argument('--scratch', action="store_true")
parser.add_argument('--temp' type=int default=300)
parser.add_argument('--steps' type=int, default=100000, help="number should fold the protein")

try:
  platform Platform.getPlatformByName("CUDA")
except Exception:
  platform Platform.getPlatformByName("OpenGL")


# Unfold the protein
if args.scratch:
  if args.fasts is Not None:
    fasta = args.fasta
  else:
    protein_fasta = ""
    fasta = open(protein_fasta).read().split("\n")[1]
