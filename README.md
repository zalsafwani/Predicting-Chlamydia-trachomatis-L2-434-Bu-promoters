# Predicting promoters for Chlamydia trachomatis strain L2/434/Bu

Final project for my BIOI 4870 (Database Search & Pattern Discovery) class.

The project goals:
  1. Find promoters for Chlamydia trachomatis L2/434/Bu.
  2.	Find gene information’s for the known gene names from the first 50 coding sequences (CDS) in Chlamydia trachomatis L2/434/Bu.  
## Language and installation
  * Python3
    * Biopython
  * MySQL database

## Database Setup
  * Run the command to create the tables in the database
    * mysql -t < projectcreate.sql 
  * To download the genbank file and fasta file from NCBI nucleotide database
    * Run python3 genbankParse.py 
      * Four files will be created after runing the above command:
      1. **chamydia_trachomatisL2_434_Bu.gb** 
      2. **sequence.fasta**
      3. **chlamydia_trachomatis**
      4. **genes.list**
  * Use this code to insert data into chlamydia_trachomatis table
    * mysqlimport database_Name chlamydia_trachomatis -L
  * Then we will be parse the genes.list file and the sequence.fasta file 
    * Run python3 parsecodingseq.py
    * new file will be created called coding_sequence
  * Use this code to insert data into coding_sequence table
    * mysqlimport database_Name coding_sequence -L
  * To get the filter result of phiSITE PromoterHunter tool with sequences from coding_sequence table
    * Run python3 phiSITEFilterResults.py
    * new file will be created called promoters_prediction
  * Use this code to insert data into promoters_prediction table
    * mysqlimport database_Name promoters_prediction -L
  * To get protein information from NCBI protein database 
    * Run python3 geneInfo.py 
    * new file will be created called gene_info
  * Use this code to insert data into gene_info table
    * mysqlimport database_Name gene_info -L
    

## File Descriptions
### Data Aggregation/Preprocessing
* **genbankParse.py **  - Used to retreive genbank file and sequence and parse genbank file
* **parsecodingseq.py ** - Used to parse the genes.list file (create from genbankParse.py file)
* **geneInfo.py ** - Used to retreive gene information for known gene names in Chlamydia trachomatis
* **phiSITEFilterResults.py ** Filter result of phiSITE PromoterHunter tool with sequences from coding_sequence table


### Database Setup
* **projectcreate.sql ** - MYSQL code to used to set up the tables in the database (DDL)
* **chlamydia_trachomatis ** chlamydia_trachomatis table data (DML)
* **coding_sequence ** coding_sequence table data (DML)
* **promoters_prediction ** promoters_prediction table data (DML)
* **gene_info ** gene_info table data (DML)

### Analysis
* **phiSITEFilterResults.py ** Filter result of phiSITE PromoterHunter tool with sequences from coding_sequence table

## E.R. Diagram


