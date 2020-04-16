from Bio import GenBank

with open("sequence.gb") as handle:
    for record in GenBank.parse(handle):
        fileOut = open("chlamydia_trachomatis", "w")
        insert1 = record.locus + "\t" + record.size + "\t" 
        insert2 = str(record.residue_type) + "\t" + record.organism + " " 
        insert3 =  record.keywords[0] + "\t" + record.taxonomy[0] 
        fileOut.write(insert1 + insert2 + insert3)
        fileOut.close()
        fileOut2 = open("coding_sequence", "w")
        genes = ""
        for current in record.features:
            if current.key == "gene":
                print(current)
    fileOut2.close()
handle.close()


