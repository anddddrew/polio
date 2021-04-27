# Reverse engineering the polio virus (PV3)

**You can start here!**: [`polio.py`](polio.py)

## :thought_balloon: Background
This project applies techniques from [reverse engineering](https://en.wikipedia.org/wiki/Information_processor) to understand the [Polio](https://en.wikipedia.org/wiki/Polio) virus. The goal here is to build an understaning of this virus from the first basis.

### Biology versus Software
Biological systems are fundamentally [information processing systems](https://en.wikipedia.org/wiki/Information_processor). While it is not a perfect analogy, software provides a useful tool for thinking about biology. The table below provices a rough outline of this analogy.

### Downloading the Polio PV3 genome
[GenBank](https://www.ncbi.nlm.nih.gov/genbank/) is the NIH genetic sequence database, an annotated collection of all publicly available DNA and RNA sequences. The Polio PV3 sequences available in GenBank have been downloaded in [`download_sequences.py`](download_sequences.py).

### Folding proteins
The [OpenMM](http://openmm.org/) toolkit is useful for molecular simulation of protein folding in [`fold.py`](fold.py).

## Annotated functions
The `translate` function is used in [`corona.py`](corona.py) to identify and annontate functions for all proteins encoded by the genome.

## :bulb: TODO
- MD (Molecular dynamics)
- Secondary Structure prediction of the protein.
- Automatically download the nucleotide sequence data.

### Translating RNA to proteins
[`lib.py`](lib.py) contains a function `translate` that converts an RNA sequence to a chain of [amino acids](https://en.wikipedia.org/wiki/Amino_acid). This function is used in [`polio.py`](polio.py).

### Biology
- textbooks
  - Molecular Biology of the Cell
- classes 
  - better tests - https://ocw.mit.edu/courses/biology/7-012-introduction-to-biology-fall-2004/index.htm
  - suspected better lectures - https://ocw.mit.edu/courses/biology/7-014-introductory-biology-spring-2005/index.htm
  - alternative lectures - https://youtube.com/playlist?list=PLGhmZX2NKiNldpyRUBBEzNoWL0Cso1jip
  - basics - https://www.khanacademy.org/science/biology

### Epidemic modeling
- http://epidemicforecasting.org

### Antibodies
- https://www.abcam.com/products?sortOptions=Relevance&selected.classification=Primary+antibodies&keywords=Poliovirus%20type%203&gclid=Cj0KCQjwyZmEBhCpARIsALIzmnL9mqAYnktr6WPFSV-Sh6Q_G7Vsba0rYueUgARZWrxzQTU01Kxy0uwaAjF9EALw_wcB&gclsrc=aw.ds


### Unit Tests
You can run unit tests via running ```./run_tests``` in the root of the directory, This will automatically run all unit tests. 

> Note: There are 3 types of polio PV1, PV2, PV3 - Each have a slightly different capsid protein All three are the extremely virulent and produce the same symptoms.

⚠️ This is not medical advice, THe information in the repository is for informational purposes only.

*A project by Andrew Nijmeh*
