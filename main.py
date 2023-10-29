import os
import subprocess

def convert_to_mp4(input_path, output_path):
    try:
        input_filename = os.path.basename(input_path)
        output_filename = os.path.splitext(input_filename)[0] + ".mp4"
        output_file_path = os.path.join(output_path, output_filename)

        cmd = [
            "ffmpeg",
            "-i", input_path,
            "-c:v", "h264_nvenc",  # Use NVENC for H.264 video encoding
            "-c:a", "aac",
            output_file_path
        ]

        subprocess.run(cmd, check=True)

        print("Conversion successful. Output file:", output_file_path)
    except Exception as e:
        print("Error during conversion:", str(e))

def convert_all_mkvs_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".mkv"):
            mkv_path = os.path.join(folder_path, filename)
            convert_to_mp4(mkv_path, folder_path)

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the script
    convert_all_mkvs_in_folder(script_dir)
