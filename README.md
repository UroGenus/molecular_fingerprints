# Drug descriptors
Scripts for generating drug descriptors. Input - drug SMILES.

1. SMILES need to be standartized (salts and other fragments need to be removed).

Install [standardiser](https://github.com/flatkinson/standardiser) and run it:
```
conda activate my-rdkit-env
python3 standardise_mols.py -i INPUT_FILE -o OUTPUT_FILE
```
where INPUT_FILE is a .tsv file with SMILES as first column and drug names as second column.

For most of the drugs, standardiser works fine, but not for all, so the output has to be checked manually and compared against [PubChem database](https://pubchem.ncbi.nlm.nih.gov/).

2. Install [Chemical Checker](https://chemicalchecker.com/)  [as follows](https://pypi.org/project/signaturizer/) and run it to generate drug descriptors:
```
conda activate sign
python3 run_chemical_checker.py -i INPUT_FILE -o OUTPUT_FILE
```
where INPUT_FILE is a .tsv file with SMILES as first column and drug names as second column.
For more details and options, see [Chemical Checker tutorial](http://gitlabsbnb.irbbarcelona.org/packages/signaturizer/blob/master/notebook/signaturizer.ipynb).

3. Run [MAP4](https://github.com/reymond-group/map4) to generate additional molecular fingerprints.
```
cd <path/to/map4/map4>
conda activate map4
python map4.py -i <path/to/smiles.csv> -o output_fingerprints_file.csv --delimiter "\n" --is-folded
```
where
- `path/to/map4` is the folder there MP4 has been installed, for installation instructions see [the MAP4 repository docu](https://github.com/reymond-group/map4)
- `smiles.csv` is a text file with one smiles per line
- `output_fingerprints_file.csv` is the output file containing the original smiles and 1027 binary fingerprint features

For more details and options, see [the MAP4 repository docu](https://github.com/reymond-group/map4).
