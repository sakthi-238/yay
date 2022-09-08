from datetime import datetime
import send2trash
import os

time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
# Enter the name of the command you want to execute
#os.system("start cmd /k yt-dlp")
#like this
#os.system("yt-dlp -F --allow-unplayable-formats 'https://bpprod3linear.akamaized.net/bpk-tv/irdeto_com_Channel_405/output/manifest.mpd' -o "%(title)s.f%(format_id)s.%(ext)s" ")


command = "yt-dlp -f video=226400,audio_122083_tam=121600 --allow-unplayable-formats --external-downloader aria2c https://bpprod3linear.akamaized.net/bpk-tv/irdeto_com_Channel_365/output/manifest.mpd -o %(title)s.f%(format_id)s.%(ext)s"

os.system(command)


os.system(f"mp4decrypt --key 77de287e104b5c369d554be9364e8d36:f7f67ce95959aaa06591216933d1fbca manifest.fvideo=226400.mp4 out.mp4")

os.system(f"mp4decrypt --key 77de287e104b5c369d554be9364e8d36:f7f67ce95959aaa06591216933d1fbca manifest.faudio_122083_tam=121600.m4a out.m4a")

os.system(f"ffmpeg -i out.mp4 -i out.m4a -vcodec copy -acodec copy  /sdcard/wed-dl/yay/yay_{time}.mp4")

send2trash.send2trash("manifest.fvideo=226400.mp4")

send2trash.send2trash("manifest.faudio_122083_tam=121600.m4a")

send2trash.send2trash("out.mp4")

send2trash.send2trash("out.m4a")

