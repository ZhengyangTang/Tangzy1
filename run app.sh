python get_all_images.py $1
ffmpeg -r 1 -i c:\EC601\EC601_IMAGES\0%d.jpg video1.mp4
python google_vision_image_analysis.py