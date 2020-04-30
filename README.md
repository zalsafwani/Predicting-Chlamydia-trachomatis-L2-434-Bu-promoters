# Predicting promoters for Chlamydia trachomatis strain L2/434/Bu

Final project for my BIOI 4870 (Database Search & Pattern Discovery) class.

The project goals:
  1. Find the promoters for Chlamydia trachomatis L2/434/Bu.
  2. Find protein informations for the valid gene names in Chlamydia trachomatis L2/434/Bu.
  
## Language and installation
  * Python3
    * Biopython
  * MySQL database

## Database Setup
  * Run the command to create the tables in the database
    * mysql -t < projectcreate.sql 
  * To download the genbank file and fasta file 
    * Run python3 genbankParse.py 
      * Four files will be created after runing the above command:
      1. **chamydia_trachomatisL2_434_Bu.gb** 
      2. **sequence.fasta**
      3. **chlamydia_trachomatis**
      4. **genes.list**
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
* **chlamydia_trachomatis ** chlamydia_trachomatis table data (DML)
* **coding_sequence ** coding_sequence table data (DML)
### Analysis


### User Interface

## E.R. Diagram
