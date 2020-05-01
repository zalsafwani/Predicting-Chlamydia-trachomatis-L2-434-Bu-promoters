# Import necessary libraries
from Bio import GenBank
from Bio import Entrez
from Bio import SeqIO

Entrez.email = "zalsafwani@unomaha.edu"
search = Entrez.efetch(db="nucleotide", id="AM884176.1", rettype="gb", retmode="text")
searchin = open("chamydia_trachomatisL2_434_Bu.gb","w")
searchin.write(search.read())
searchin.close()


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
        fileOut2 = open("genes.list","w")
        for current in record.features:
            if current.key == "gene":
                fileOut2.write(str(current))
        fileOut2.close()
handle.close()

clSeq = ""
fileOut3 = open("sequence.fasta","w")
fileOut3.write(">AM884176.1 Chlamydia trachomatis strain L2/434/Bu complete genome\n")
for seq_record in SeqIO.parse("chamydia_trachomatisL2_434_Bu.gb", "genbank"):
    clSeq = str(seq_record.seq)
    fileOut3.write(clSeq)
fileOut3.close()
