# random-opt

Requirements:
1. Java
2. Ant
3. Jython

Jython files that are to be executed:
1. continuouspeaks.py
2. flipflop.py
3. tsp.py
4. NN_backprop.py
5. NN_RHC.py
6. NN_SA.py
7. NN_GA.py

Dataset files:
1. spam_trg.csv
2. spam_val.csv
3. spam_test.csv

Output folders:
1. NN_SPAM_OUTPUT
2. CONTPEAKS
3. FLIPFLOP
4. TSP

Steps before execution:
1. Edit the sys.path statement in all jython files to the correct path of ABAGAIL.jar
2. Make sure that dataset files are in the root directory of the repo.
3. Make sure output folders are made in the root directory.

Execution:
1. Simply run the jython files with the command "jython filename.py"
2. Based on the chosen file, output 'txt' files will be generated in one of the output folders.
3. To view these files, rename them to '.csv' and use whichever tool you find suitable to view the csv files. I personally used Excel to view and create the charts from the files.
