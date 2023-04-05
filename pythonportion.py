#author @Gabriel Stewart-Guido
#date: April 4, 2023
#Program that loads pdb file from cmd line argument.
#readlines() is used to get individual lines separated and then
#lines are looped through.
import sys

pdb_file=str(sys.argv[1])
file1=open(pdb_file,'r')
Lines=file1.readlines()
file1.close()

for x in Lines:

        atom='ATOM'
        if x[0:4]==atom:
            atom_serial=x[7:12]
            print(f'Atom serial number:{atom_serial}')
            coordinates=x[33:56]
            splitted=coordinates.split(" ")
            x1=splitted[0]
            x2=splitted[1]
            x3=splitted[2]
            print(f'X coordinates: {x1}')
            print(f'Y coordinates: {x2}')
            print(f'Z coordinates: {x3}')
