import os
includefilters=['.mp4','.mkv','.avi','.mov','.webm','.3gp']

allVideos={f for f in os.listdir() for t in includefilters if t in f }

def convert_other_video_to_mp4():
	mp4FileSet={x for x in os.listdir() if x.endswith('.mp4')}
	nonmp4filelist=allVideos - mp4FileSet
	for v in nonmp4filelist:
		os.system(f'start ffmpeg -y -i "{v}" -vcodec libx265 "{v.split(".")[0]+".mp4"}" ')
convert_other_video_to_mp4()

def concat_all_mp4_videos():
	# mp4FileSet={x for x in os.listdir() if x.endswith('.mp4')}
	mp4files='\n'.join(sorted([f"file '{x}'" for x in os.listdir() if x.endswith('.mp4')]))

	print(mp4files)
	
	open('fileQueue','w').write(mp4files)
	
	COMMAND=f"start cmd /k \"ffmpeg -safe 0 -f concat  -i fileQueue -vcodec libx265 -crf 28 output.mp4\" "
	os.system(COMMAND)
concat_all_mp4_videos()


a=['apple','ball','all','zall']
print(sorted(a))
