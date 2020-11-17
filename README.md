# Molecular fingerprints
Scripts for generating molecular fingerprints for drugs. Input - drug SMILES.

1. SMILES need to be standartized (salts and other fragments need to be removed).

Run [standardiser](https://github.com/flatkinson/standardiser):
```
conda activate my-rdkit-env
python3 standardise_mols.py -i INPUT_FILE -o OUTPUT_FILE
```
where INPUT_FILE is a .tsv file with SMILES as first column and drug names as second column.

For most of the drugs, standardiser works fine, but not for all, so the output has to be checked manually and compared against [PubChem database](https://pubchem.ncbi.nlm.nih.gov/).

2. Run [Chemical Checker](https://chemicalchecker.com/) to generate drug descriptors:
```
conda activate sign
python3 run_chemical_checker.py -i INPUT_FILE -o OUTPUT_FILE
```
where INPUT_FILE is a .tsv file with SMILES as first column and drug names as second column.

3. Run [MAP4](https://github.com/reymond-group/map4) to generate additional molecular fingerprints.
```
cd map4/map4
conda activate map4
python map4.py -i -i INPUT_FILE -o OUTPUT_FILE --delimiter "\n" --is-folded
```
where INPUT_FILE is a text file with one SMILES in each line.
