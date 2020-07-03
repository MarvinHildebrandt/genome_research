import csv
import os

# open gff file
with open('RefBeet-1.5-BeetSet2.v3_BP1.gff', newline = '') as gff:
	gff_reader = csv.reader(gff, delimiter='\t')
	
	#create list of lines
	feature_list = []
	for gff in gff_reader:
    		feature_list.append(gff)

	# discard non-entry lines
	feature_list = [feature for feature in feature_list if len(feature) == 9]

	# filter for chromosome
	roi_list = [feature for feature in feature_list if feature[0] == 'Chr5']

	# filter for region (between two indices)
	roi_list = [feature for feature in roi_list if int(feature[3]) > 1739000 and int(feature[4]) < 1910000]

	# filter for genes
	roi_list = [feature for feature in roi_list if feature[2] == 'gene']

	# Extract sequences of genes
	for gene in roi_list:
		if int(gene[3]) < int(gene[4]):
			os.system("python ffetch -i 'Chr5[" + gene[3] + ":" + gene[4] + "]' RefBeet1.5.1.fasta")
		else:
			os.system("python ffetch -i 'Chr5[" + gene[4] + ":" + gene[3] + "]' RefBeet1.5.1.fasta")

