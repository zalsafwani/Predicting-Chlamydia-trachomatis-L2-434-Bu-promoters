# Import necessary libraries
import re
from Bio import SeqIO


def main():
    
    # Open the fasta file to parse through it to save the complete sequence 
    for seqRecord in SeqIO.parse("sequence.fasta", "fasta"):
        clSeq = seqRecord.seq
    
    # Open the genes.list file to parse through
    # to get the position for the coding sequence, locus_tag, and gene name
    fileIn = open("genes.list", "r")
    
    # Open a file to write the data needed for coding_sequence table
    fileOut = open("coding_sequence", "w")
    
    # Read the first line
    line = fileIn.readline()

    # Read the genes.list file line by line
    # to get the first 100 position for coding sequence, locus_tag, and gene name
    # call the codingSeqCalc method to find the new position sequences
    # write the data needed for coding_sequence table:
    # locus_tag, gene name, strand, start and end position of the coding sequence,
    # sequence that has the new position (add 100 bp upstream of the ATG start codon)
    while (line):
        line = line.strip()
        if line.startswith("gene"):
            gene = ""
            gene_position = ""
            locuse_tage = ""
            geneplace = ""
            tag = ""
            geneName = ""
            strand = "forward"
            sequence = ""
            geneInfo = ""
            gene_position = line.split()
            geneplace = gene_position[1].strip()
            newPosition = codingSeqCalc(str(geneplace))
            line = fileIn.readline()
            if line.strip().startswith("/gene="):
                gene = line.split("/gene=")
                geneName = str(gene[1]).strip().strip('"')
                line = fileIn.readline()
            if line.strip().startswith("/locus_tag"):
                locuse_tage = line.strip().split("/locus_tag=")
                tag = str(locuse_tage[1]).strip('"')
                if geneplace.startswith("complement"):
                    strand = "complement"
                    geneplace = geneplace.strip("complement(").strip(')')
                    sequence = clSeq[newPosition[0]:newPosition[1]].reverse_complement()
                else:
                    if newPosition[0] == -99:
                        sequence = clSeq[1038741:1038843]+clSeq[0:1017]
                    else:
                        sequence = clSeq[newPosition[0]:newPosition[1]]
                pos = geneplace.split("..")
                geneInfo = ""
                if geneName == "":
                    geneName = "-"
                geneInfo = tag + '\t' + geneName + '\t' + strand +'\t' + pos[0] 
                geneInfo = geneInfo + '\t' + pos[1] + '\t' + str(sequence)
                fileOut.write(geneInfo)
                fileOut.write('\n')
                if tag == "CTL0050":
                    break
        else:
            line = fileIn.readline()
    fileOut.close()
    fileIn.close()
    
# This method will generate the new start and end position
# that will help us add 100 bp upstream of the ATG start codon
# that will help us find promoters when searching the promoterhunter tool
# with the new sequence that has new position
def codingSeqCalc(geneplace):
    strand = "complement"
    complement = False
    checkStrand = re.match(strand,geneplace)
    if (checkStrand):
        complement = True
        geneplace = geneplace.strip("complement(").strip(')')
    position = geneplace.split("..")
    startPos = int(position[0])
    endPos = int(position[1])
    if (complement == True):
        startPos -= 1
        endPos += 100
    else:
        startPos = startPos - 100
    return startPos , endPos

if __name__ == '__main__':
    main()
