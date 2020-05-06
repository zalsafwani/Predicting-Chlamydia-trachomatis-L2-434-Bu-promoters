import MySQLdb  
from Bio import Entrez, SeqIO, GenBank
import re

Entrez.email = "zalsafwani@unomaha.edu"
conn = MySQLdb.connect(db="zalsafwani")
cursor = conn.cursor()

cursor.execute("select locus_tag, gene_symbol from coding_sequence where gene_symbol != '-';")
row = cursor.fetchall()
outFile = open("gene_info", "w")
for data in row:
    locus = data[0] + "\t"
    symbol = data[1] + "\t"
    
    handle = Entrez.esearch(db="protein" ,term=data[0])
    record = Entrez.read(handle)
    if len(record['IdList']) == 2:
        idnum = (record['IdList'][1])
    else:
        idnum = (record['IdList'][0])
    handle.close()
    
    handle2 = Entrez.efetch(db="protein", id=idnum, rettype="gb", retmode="text")
    for record in GenBank.parse(handle2):
        version = record.version + "\t" 
        length = record.size + "\t" 
        fullinfo = (record._definition_line()).strip()
     
        fullinfo = fullinfo.replace("DEFINITION ", "").strip()
        fullinfo = re.sub("\[Chlamydia.*\n*.*].", "", fullinfo).strip()
        insert =  locus + version  + symbol + length + fullinfo + '\n'
        outFile.write(insert)
    handle2.close()
cursor.close()
conn.close()
outFile.close()
