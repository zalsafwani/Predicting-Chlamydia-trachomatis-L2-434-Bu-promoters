import re
from Bio import SeqIO


def main():

    for seqRecord in SeqIO.parse("sequence.fasta", "fasta"):
        clSeq = seqRecord.seq

    fileIn = open("genes.list", "r")
    fileOut = open("coding_sequence", "w")
    line = fileIn.readline()

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
                    sequence = clSeq[newPosition[0]:newPosition[1]].complement()
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
                if tag == "CTL0100":
                    break
            elif line.startswith(" "):
                line = fileIn.readline()
        else:
            line = fileIn.readline()
    fileOut.close()
    fileIn.close()
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
        endPos = endPos + 100
    else:
        startPos = startPos - 100
    return startPos , endPos

if __name__ == '__main__':
    main()
