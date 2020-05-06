# Import necessary libraries
import re

fileName = ""   # The name of the file result to be read
counter = 1     # To modify the file name 

# Open the file that will have the data needed
# for promoters_prediction data table as write mode
fileOut = open("promoters_prediction","w")

# Go through the first 6 files that were manyally generated
# using the online PromoterHunter tool
# read line by line to find the accuret promoters result
# by having the promoter in position less than 100
# where we added the additional 100 bps upstrem the ATG
# start codon for coding sequeces
# save locus tag and the promoter sequence to the new file
# where it will be used to insert data to the database
while(fileName != "resultCTL0006"):
    fileName = "resultCTL000"
    fileName += str(counter)
    fileIn = open(fileName,"r")
    promoterCheck = False
    line = fileIn.readline()
    while(line):
        if line.strip().startswith('<tr id="trb'):
            strandline = fileIn.readline()
            beginline = fileIn.readline().strip()
            begin = re.sub("<td>(\d\d*)</td>","\\1",beginline)
            if (int(begin) < 100 and promoterCheck == False):
                fileIn.readline()
                endline = fileIn.readline().strip()
                end = re.sub("<td>(\d\d*)</td>","\\1",endline)
                line = fileIn.readline().strip()
                while line:
                    if re.match('<td style="font-family:Courier">',line): 
                        seqP1 = fileIn.readline().strip()
                        seq35 = re.search("[ATCG]+",fileIn.readline().strip())
                        seqP2 = fileIn.readline().strip()
                        seq10 = re.search("[ATCG]+",fileIn.readline().strip())
                        seqP3 = fileIn.readline().strip()
                        promoterSeq = seqP1 + "(" + seq35[0] + ")" + seqP2 + "(" + seq10[0] + ")" + seqP3
                        locuse = fileName.strip('result')
                        result = locuse + "\t" + promoterSeq + "\n"
                        fileOut.write(result)
                        promoterCheck = True
                        break
                    else:
                        line = fileIn.readline().strip()
            else:
                line = fileIn.readline()
        else:
            line = fileIn.readline()
    counter += 1
    fileIn.close()
fileOut.close()
