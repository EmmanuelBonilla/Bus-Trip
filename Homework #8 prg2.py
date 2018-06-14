#-------------------------------------------------------------------
# Emmanuel Bonilla
# Washington State University, Tri-Cities
# CptS111: Introduction to Algorithmic Problem Solving
# Summer 2016: Homework 08
# System: Python v3.5.1 IDLE (MS Windows OS)
#-------------------------------------------------------------------

from math import *
from os import getcwd

#Purpose: Read lines from input file, remove the carriage return thru rawline loop
#Parameters: Has to be an existing file
#Return: Read lines from the opened file
def readLinesFromFile (filename):
    inFile = open (filename,'r')
    RawLines = inFile.readlines()
    inFile.close ()
    Lines = []
    
    for rawline in RawLines:
        Lines.append (rawline[:-1])
        
    return Lines
   
#Purpose: Process the inputed file and put results in outfile in the same directory
def processFile ():
    ueFileName = input ("\nPlease enter a data file name: ")
    myPath = getcwd () + "\\"
    fileExt = ".txt" #  Text file extension
    busRec = readLinesFromFile (myPath + ueFileName + fileExt)# process the bus trip into a file
    
    if len(busRec) > 0:
        #Display header data out to new txt file in same sub directory
        fileName = "Results of " + ueFileName + fileExt
        outFile = open (fileName, 'w')
        print ("Cities:          Odometer:  Tank:   Miles:   Gal:    Mpg: ",file=outFile)
        print("-" * 64,file=outFile)

        #split the inputed file and print results in file after the header
        prevOdom, frstOdom, prevGas, frstGas, miles, gal, mpg = 0,0,0,0,0,0,0
        
        for tripRec in busRec:
            trip = tripRec.split(' ')
            city = (trip[0])
            odom = eval(trip[1])
            gas = eval(trip[2])

            if prevOdom == 0:
                frstOdom = odom
                frstGas = gas
            else:
                miles = (odom - prevOdom)
                gal = (prevGas - gas)
                mpg = miles / gal
                            
            prevOdom = odom
            prevGas = gas
            formatFile = "{0:15}{1:10}{2:8}{3:9.2f}{4:8.2f}{5:7.2f}".format(city,odom,gas,miles,gal,mpg)
            print(formatFile,file=outFile)

        #print the footer of file with total results
        print ("-" * 64,file=outFile)
        totMiles = prevOdom - frstOdom
        totGas= frstGas - prevGas
        avgMpg = totMiles / totGas
        formatFile = "{0:33}{1:9.2f}{2:8.2f}{3:7.2f}".format("Total:",totMiles,totGas,avgMpg)
        print(formatFile,file=outFile)
        
    else:
        print ("\nDude get out of your house!")
        
    outFile.close()

    return

#this will continue to loop until user selects to quit
def main():
    badfile = True

    while badfile:
        print ("\nWhat would you like to do today? ")
                
        try:
            print("\n0: Quit/Nothing \n1: Process file")
            ueMenu = abs(int(eval(input("\nPlease pick an option: "))))            
        
            if ueMenu == 1:
                processFile()
            
            elif ueMenu == 0:
                badfile = False
            
            elif ueMenu > 1 or ueMenu < 0:
                print('"\nInvalid input, Please try again"')
            
        except:
            print ('\n"Invalid File Name, Please Try Again."')       
    return
main()
