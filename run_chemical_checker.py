#! /usr/bin/env python

import pandas as pd
import os
from os import path
import argparse
import sys
import signaturizer
from signaturizer import Signaturizer

def main():
	parser = argparse.ArgumentParser( description="Run Chemical Checker" )
	parser.add_argument( "-i", help="Input tsv with with drug SMILES", default = 'drugs_standarised_smiles_curated.tsv')
	parser.add_argument( "-o", help="Output .tsv file, default stdout", default = sys.stdout)
	parser.add_argument( "-c", help="Column names provided", default = None)
	
	pa = parser.parse_args()

	if pa.c:
		smiles_df = pd.read_csv(pa.i, delimiter = '\t')
	else:
		smiles_df = pd.read_csv(pa.i, delimiter = '\t', names = ['SMILES', 'Drug Name'])
	smiles = smiles_df.SMILES.values.tolist()
	
	sign = Signaturizer('GLOBAL')
	descriptors = sign.predict(smiles)
	
	descriptors_df = pd.DataFrame(descriptors.signature, columns = list(range(0, descriptors.signature.shape[1])))
	descriptors_df.insert(0, 'Drug Name', smiles_df['Drug Name'], True)
	
	smiles_df = smiles_df.merge(descriptors_df, on = 'Drug Name')
	
	smiles_df.to_csv(pa.o, sep = '\t', index = False)
		
    
if __name__ == '__main__':
    main()    
