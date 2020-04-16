# Import necessary libraries
from Bio import GenBank

# Open the genbank file to parse through it
# then open a file in write mood to save the data neaded 
# and then be able to insert them in chlamydia_trachomatis table
with open("chamydia_trachomatisL2_434_Bu.gb") as handle:
    for record in GenBank.parse(handle):
        fileOut = open("chlamydia_trachomatis", "w")
        insert1 = record.locus + "\t" + record.size + "\t" 
        insert2 = str(record.residue_type) + "\t" + record.organism + " " 
        insert3 =  record.keywords[0] + "\t" + record.taxonomy[0] 
        fileOut.write(insert1 + insert2 + insert3)
        fileOut.close()
        
        # Go to the features section to get all the genes
        # and store the information needed for coding_sequence table
        for current in record.features:
            if current.key == "gene":
                print(current)

handle.close()


