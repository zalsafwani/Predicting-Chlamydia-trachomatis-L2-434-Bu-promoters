echo "Set up Database"

# Create the tables into the database
mysql -t < projectcreate.sql

# Set up the data file for chlamydia_trchomatis table
python3 genbankParse.py

# Insert the chlamydia_trchomatis data into the database
mysqlimport zalsafwani chlamydia_trachomatis -L

# Set up the data file for coding_sequence table
python3 parsecodingseq.py

# Insert the coding_sequence data into the database
mysqlimport zalsafwani coding_sequence -L

# Set up the data file for promoters_prediction table
python3 phiSITEFilterResults.py

# Insert the promoters_prediction data into the database
mysqlimport zalsafwani promoters_prediction -L

# Set up the data file for gene_info table
python3 geneInfo.py

# Insert the gene_info data into the database
mysqlimport zalsafwani gene_info -L
