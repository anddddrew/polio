# A genome sequence is a compelte list of nucelotides
# (A, C, G AND T for DNA genomes) that make up all
# chromosomes of an individual specie.

class Genome:
  def __init__(self, nucelotides):
    self.nucelotides = nucelotides
  
  def get_nucelotides(self):
    return self.nucelotides

class GenomeBuilder():
  def __init__(self, nucelotides):
    self.genome = Genome(nucelotides)
  
  def build(self):
    return self.genome