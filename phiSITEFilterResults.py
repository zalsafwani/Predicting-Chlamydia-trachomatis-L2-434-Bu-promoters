import re

fileName = ""
counter = 1
fileOut = open("promoters_prediction","w")
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


