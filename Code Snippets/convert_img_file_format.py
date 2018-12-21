import glob
import os
import tqdm
import cv2

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--src', '-s', help="Source directory", type=str)
parser.add_argument('--source_type', '-f', help="Source image type", type=str)
parser.add_argument('--target_type', '-t', help="Target image type", type=str)
parser.add_argument('--delete', '-d', default=False, help="Delete the src files", type=bool)

args = parser.parse_args()

directory = args.src
source_type = args.source_type
target_type = args.target_type
delete_source_afterwards = args.delete

allowed_types = ['png', 'jpg'] # just these for now

if source_type in allowed_types and target_type in allowed_types:

    src_files = glob.glob(os.path.join(directory, f'*.{source_type}')) 

    print('Converting Files...')
    for fname in tqdm.tqdm(src_files):                                   
        img = cv2.imread(fname)
        new_fname = f'{fname[0:-3]}{target_type}'
        cv2.imwrite(new_fname, img)

        if delete_source_afterwards:
            if os.path.exists((new_fname):
                os.remove(fname)
