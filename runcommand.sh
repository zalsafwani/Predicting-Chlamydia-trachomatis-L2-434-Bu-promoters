echo "Set up Database"
mysql -t < projectcreate.sql
python3 genbankParse.py
mysqlimport zalsafwani chlamydia_trachomatis -L
python3 parsecodingseq.py
mysqlimport zalsafwani coding_sequence -L
python3 phiSITEFilterResults.py
mysqlimport zalsafwani promoters_prediction -L
python3 protein.py
mysqlimport zalsafwani protein_info -L
