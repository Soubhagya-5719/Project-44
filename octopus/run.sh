#!/bin/bash
#SBATCH -A teja.dhondu
#SBATCH --gres=gpu:2
#SBATCH --ntasks 20
#SBATCH --mem-per-cpu=1024	
#SBATCH --time=2-00:00:00
#SBATCH --mail-type=END
#SBATCH --output=output.txt

module load cuda/10.2
module load cudnn/7.6.5-cuda-10.2

# Prepare data
cd
source anaconda3/etc/profile.d/conda.sh
conda activate smpl
cd octopus
rm -rf data/sample
python3 prepare_data.py
conda deactivate

# OpenPose
cd /home/teja.dhondu/octopus/openpose
rm -rf build
mkdir build
cd build
cmake ..
make -j20
cd ..
mkdir -p ../data/sample/keypoints
./build/examples/openpose/openpose.bin --image_dir ../data/sample/frames --write_json ../data/sample/keypoints --face --number_people_max 1 --display 0 --render_pose 0

# Segmentation
cd ../CIHP_PGN
conda activate smpl
mkdir -p ../data/sample/segmentations
python3 test_pgn.py

# Octopus
cd ..
mkdir -p data/sample/out
python3 infer_single.py sample data/sample/segmentations data/sample/keypoints --out_dir data/sample/out
python3 make_pickle.py

# Texture stitching
mkdir -p data/sample/unwraps
cd semantic_human_texture_stitching
python3 step1_make_unwraps.py ../data/sample/out/frame_data.pkl ../data/sample/frames ../data/sample/segmentations ../data/sample/unwraps
python3 step2_segm_vote_gmm.py ../data/sample/unwraps ../data/sample/out/segm.png ../data/sample/out/gmm.pkl
python3 step3_stitch_texture.py ../data/sample/unwraps ../data/sample/out/segm.png ../data/sample/out/gmm.pkl ../data/sample/out/sample_texture.png
cd ../texture_overlay
cp Dwarf_Low.obj.mtl ../data/sample/out
python3 texture_overlay.py	
