# ConvertMKVtoMP4
Convert MKV to MP4 with Python and FFMPEG


Create a new Folder... Name it whatever you want.

Put Main.py in that folder

https://github.com/BtbN/FFmpeg-Builds/releases
Download the 3 FFMPEG files from this link and put these files in the folder

Put all the MKV files you want to be converted to MP4 into the folder

This script is set to run using an Nvidia graphics card.
To use your CPU (Slower) use this function instead:

    def convert_to_mp4(input_path, output_path):
        try:
            input_filename = os.path.basename(input_path)
            output_filename = os.path.splitext(input_filename)[0] + ".mp4"
            output_file_path = os.path.join(output_path, output_filename)
    
            cmd = [
                "ffmpeg",
                "-i", input_path,
                "-c:v", "libx264",
                "-c:a", "aac",
                output_file_path
            ]
    
            subprocess.run(cmd, check=True)
    
            print("Conversion successful. Output file:", output_file_path)
        except Exception as e:
            print("Error during conversion:", str(e))



Main reason for doing this?
You can drag a MP4 file into Chrome Browser and Cast it to your google chrome cast.
where MKV wont cast properly.
