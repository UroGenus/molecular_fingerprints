# molecular_fingerprints
Scripts for generating molecular fingerprints for drugs

To run [standardiser](https://github.com/flatkinson/standardiser):
```
conda activate my-rdkit-env
python3 standardise_mols.py -i INPUT_FILE -o OUTPUT_FILE
```
where INPUT_FILE is a .tsv file with SMILES as first column and drug names as second column.
