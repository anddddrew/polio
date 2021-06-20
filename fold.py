from simtk.openmm.app import *
from simtk.openmm import *
from simtk.unit import *
from sys import stdout
import sys
import os as os
import argparse


parser = argparse.ArgumentParser(description="Fold proteins.")
parser.add_argument("--scratch", action="store_true")
parser.add_argument("--temp", type=int, default=300)
parser.add_argument("--step", type=int, default=100000, help="2500000000 Should fold the protein")
parser.add_argument("--fasta", type=str, default=None)
parser.add_argument("--writes", type=int, default=1000, help="The default integer is 1000 (1k)"
