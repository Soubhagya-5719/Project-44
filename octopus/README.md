# Mesh Generation Code
 - This code generates the smpl mesh from images of a person taken at 8 different angles
 - This code utilizes Octopus (https://github.com/thmoa/octopus), Semantic texture
 stitching (https://github.com/thmoa/semantic_human_texture_stitching), Openpose and
 CIHP PGN
## Instructions
 - Download the CIHP PGN checkpoint and place in the CIHP_PGN/checkpoint folder
 - Openpose must be rebuilt
 - Install all dependencies required for the 4 programs that are being used
 - Place the images in the "images" directory and run the run.sh script