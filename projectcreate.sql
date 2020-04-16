
/* Choose the database name USE (name);
 * If these tables exist already, delete them.
 * Careful with this type of statement, 
 * especially if you have been collecting data 
 * regularly and don't have it backed up.
 */
--USE zalsafwani;
DROP TABLE IF EXISTS chlamydia_trachomatis,
		     promoters_prediction,
		     protein_aliases,
		     coding_sequence;

/* DDL statements are below for the 
 * chlamydia_trachomatis, coding_sequence,
 * promoters_prediction , 
 * protein_aliases tables.
 */
CREATE TABLE chlamydia_trachomatis(
    accession_number    VARCHAR(20)     NOT NULL,
    basepairs           VARCHAR(25)     NOT NULL,
    dna_type            VARCHAR(20)     NOT NULL,
    definition          VARCHAR(100)     NOT NULL,
    orgnism             VARCHAR(100)     NOT NULL,
    PRIMARY KEY (accession_number)
    );

CREATE TABLE coding_sequence(
    locus_tag           VARCHAR(20)     NOT NULL,
    gene_name           VARCHAR(20),
    strand              VARCHAR(20)     NOT NULL,
    start_position      INT             NOT NULL,
    end_position        INT             NOT NULL,
    sequence            VARCHAR(1000)   NOT NULL,
    PRIMARY KEY (locus_tag)
    );

CREATE TABLE promoters_prediction(
    locus_tag           VARCHAR(20)     NOT NULL,
    promoters_ID        VARCHAR(20)     NOT NULL,
    strand              VARCHAR(20)     NOT NULL,
    start_position      INT             NOT NULL,
    end_position        INT             NOT NULL,
    sequence            VARCHAR(25)     NOT NULL,
    FOREIGN KEY (locus_tag) REFERENCES coding_sequence (locus_tag) ON DELETE CASCADE, 
    PRIMARY KEY (promoters_ID)
    );

CREATE TABLE protein_aliases(
    locus_tag		VARCHAR(20)	NOT NULL,
    gene_name		VARCHAR(20)	NOT NULL,
    aliases		VARCHAR(50)	NOT NULL,
    FOREIGN KEY (locus_tag) REFERENCES coding_sequence (locus_tag) ON DELETE CASCADE
    );
 
