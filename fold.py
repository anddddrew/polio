from simtk.openmm.app import *
from simtk.openmm import *
from simtk.unit import *
from sys import stdout
import sys
import os as os
import argparse  


parser = argparse.ArgumentParser(description="Fold proteins.")
parser.add_argument('--scratch', action='store_true')
parser.add_argument('--temp', type=int, default=300)

