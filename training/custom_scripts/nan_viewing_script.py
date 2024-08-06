#!/usr/bin/env python

###################
# Script Overview #
###################
# This is a custom script to view contents of 'xyz' dictionaries within the .pt tensors by removing the nan mask. 

###########
# Modules #
###########
import argparse
import torch

############
# Argparse #
############
def get_args():
    parser = argparse.ArgumentParser(description='Process .pt tensor files')
    parser.add_argument('input_file', type=str, help='Path to the input .pt file')
    return parser.parse_args()

args = get_args()
input_file = args.input_file

########
# Main #
########
data = torch.load(input_file)

# Process the loaded data
if isinstance(data, dict):
    for key, value in data.items():
        print(f"Key: {key}, Value: {value}")

# Extract 'xyz' tensor
xyz_tensor = data['xyz']

# Flatten the tensor
shape = xyz_tensor.shape
tensor_reshaped = xyz_tensor.reshape(shape[0], -1)

# Drop rows containing NaN values
tensor_reshaped = tensor_reshaped[~torch.any(torch.isnan(tensor_reshaped), dim=1)]

# Reshape back
tensor = tensor_reshaped.reshape(tensor_reshaped.shape[0], *shape[1:])

# Print the reshaped tensor
print("Reshaped Tensor:")
print(tensor)

# Ex. Bash Command: /projects/bgmp/lmjone/internship/ProteinMPNN-PH/training/nan_viewing_script.py /projects/bgmp/lmjone/internship/ProteinMPNN-PH/training/mirrored_pdb_2021aug02/pdb/00/200l_A.pt