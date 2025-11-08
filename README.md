# Change_paths_in_a_moved_WarpTools_directory
For CryoET projects, when a WarpTools directory is moved, all the metadata files and settings files in the directory still record the old absolute paths to the raw data. This script will replace all the absolute paths with the new path to the raw data in a WarpTools directory which has been moved or renamed on your machine.


To use, open the script and read the instructions inside. Then to run, place the script inside the /warp_frameseries/ folder inside the moved/renamed WarpTools directory and run `./tomo_pathswap.py` to execute the script. 
