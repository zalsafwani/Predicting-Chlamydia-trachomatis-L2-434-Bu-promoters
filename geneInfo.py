# Import necessary libraries
import MySQLdb  
from Bio import Entrez, SeqIO, GenBank
import re

# Create the email that is needed when searching Entrez NCBI
# Create connection, cursor to execute queries from MySQL database.
Entrez.email = "zalsafwani@unomaha.edu"
conn = MySQLdb.connect(db="zalsafwani")
cursor = conn.cursor()

# Use the cursor to find locuse_tag and gene_symbol from coding_sequence table
# for all of the record that has known gene_symbol and not - (null)
cursor.execute("SELECT locus_tag, gene_symbol FROM coding_sequence WHERE gene_symbol != '-';")

# Get all of results from the query
row = cursor.fetchall()

# Open new file to save the data needed for gene_info table
outFile = open("gene_info", "w")

# Go through each result save the locuse and symbol 
for data in row:
    locus = data[0] + "\t"
    symbol = data[1] + "\t"
    
    # Search Entrez NCBI protein database using the locus
    # Go through the result and save the ID for the record
    handle = Entrez.esearch(db="protein" ,term=data[0])
    record = Entrez.read(handle)
    if len(record['IdList']) == 2:
        idnum = (record['IdList'][1])
    else:
        idnum = (record['IdList'][0])
    handle.close()
    
    # Retrive the record from Enterz protein database 
    # using the ID number saved from the previous step 
    # save the result as GenBank file
    handle2 = Entrez.efetch(db="protein", id=idnum, rettype="gb", retmode="text")
    
    # Parse through the GenBank file to find data needed for gene_info table
    # like version, length and full name of the gene and stor the result
    # into new file to be able to insert them easily
    for record in GenBank.parse(handle2):
        version = record.version + "\t" 
        length = record.size + "\t" 
        fullinfo = (record._definition_line()).strip()
        fullinfo = fullinfo.replace("DEFINITION ", "").strip()
        fullinfo = re.sub("\[Chlamydia.*\n*.*].", "", fullinfo).strip()
        insert =  locus + version  + symbol + length + fullinfo + '\n'
        outFile.write(insert)
    handle2.close()

# Close the cursor, connection and outFile
cursor.close()
conn.close()
outFile.close()
