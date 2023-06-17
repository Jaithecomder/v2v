#!/bin/bash

# Create algorithm directory
mkdir algorithm
touch algorithm/__init__.py
touch algorithm/helpers.py
touch algorithm/hyperparameters.py
touch algorithm/testing.py
touch algorithm/utilities.py

# Create csv_processing directory
mkdir csv_processing
touch csv_processing/instant.ipynb
touch csv_processing/preprocessing.ipynb

# Create log_files directory
mkdir log_files
touch log_files/my_log_file.txt
touch log_files/nsd.txt
touch log_files/nsd_taxi_v15.0_.txt

# Create s123_code directory
mkdir s123_code
touch s123_code/__init__.py
touch s123_code/s123_gennet.py
touch s123_code/s123_genroute.py
touch s123_code/s1s2simulation.py

# Create setting1 directory
mkdir setting1
touch setting1/s1config.sumocfg
touch setting1/s1erbconfig.sumocfg
touch setting1/s1erbnet.net.xml
touch setting1/s1erbrou.rou.xml
touch setting1/s1net.net.xml
touch setting1/s1rou.rou.xml

# Create README.md file
touch README.md

# Create commit_files.sh script
echo "#!/bin/bash" >> commit_files.sh
echo "" >> commit_files.sh
echo "git add ." >> commit_files.sh
echo "git commit -m \"Add files\"" >> commit_files.sh
echo "git push origin master" >> commit_files.sh

# Change the permission of the script to make it executable
chmod +x commit_files.sh
