import boto3
import os
import subprocess
from config import AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY, SOURCE_BUCKET, DEST_BUCKET, FFMPEG_PARAMS

s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

def download_file(filename):
    s3.download_file(SOURCE_BUCKET, filename, filename)

def upload_file(filename):
    s3.upload_file(filename, DEST_BUCKET, filename)

def convert_to_av1(filename):
    output_filename = f"{filename.split('.')[0]}_av1.mp4"
    cmd = f"ffmpeg -i {filename} {FFMPEG_PARAMS} {output_filename}"
    subprocess.run(cmd, shell=True)
    return output_filename

def calculate_scores(output_filename):
    cmd_vmaf = f"ffmpeg -i {filename} -i {output_filename} -filter_complex libvmaf -f null -"
    subprocess.run(cmd_vmaf, shell=True)
    cmd_psnr = f"ffmpeg -i {filename} -i {output_filename} -vf psnr -f null -"
    subprocess.run(cmd_psnr, shell=True)

if __name__ == "__main__":
    filename = "source_video.mp4" # This should be fetched dynamically
    download_file(filename)
    output_filename = convert_to_av1(filename)
    calculate_scores(output_filename)
    upload_file(output_filename)
