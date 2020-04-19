# Predicting promoters for Chlamydia trachomatis strain L2/434/Bu

Final project for my BIOI 4870 (Database Search & Pattern Discovery) class.

The project goals:
  1. Find the promoters for Chlamydia trachomatis L2/434/Bu.
  2. Find the aliases for the genes in Chlamydia trachomatis L2/434/Bu.
  
Befor setting the database we need to download the genbank file and the fasta file from NCBI for the Chlamydia trachomatis L2/434/Bu complete genome or use those files 
* **chamydia_trachomatisL2_434_Bu.gb** 
* **sequence.fasta**
  
  Steps to download the genbank file from NCBI using the terminal:
  
  1. Download Entrez Programming Utilities (E-utilities)
   Form https://www.ncbi.nlm.nih.gov/home/tools/ by clicking  Entrez Direct 
   https://www.ncbi.nlm.nih.gov/books/NBK179288/ 
   then from Installation section click download EDirect installer
  
  2. Run the code in the terminal: source ./install-edirect.sh
  
  3. Run the following command to get the genbank file for chamydia_trachomatisL2_434_Bu from NCBI nucleotide database.
  esearch -db nucleotide -query "AM884176.1" | efetch -format gb > chamydia_trachomatisL2_434_Bu.gb

## Database Setup
  * After downloading the genbank file
  * Run python3 genbankParse.py > genes.list
    * new file will be created called chlamydia_trachomatis
  * Use this code to insert data into chlamydia_trachomatis table
    * mysqlimport (database_Name) chlamydia_trachomatis -L
  * Then we will be parse the genes.list file and the sequence.fasta file 
    * Run python3 parsecodingseq.py
    * new file will be created called coding_sequence
  * Use this code to insert data into coding_sequence table
    * mysqlimport (database_Name) coding_sequence -L
    

## File Descriptions
### Data Aggregation/Preprocessing
* **genbankParse.py **  - Used to parse the genbank file
* **parsecodingseq.py ** - Used to parse the genes.list file (create from genbankParse.py file)


### Database Setup
* **projectcreate.sql ** - MYSQL code to used to set up the tables in the database (DDL)

### Analysis


### User Interface

## E.R. Diagram
