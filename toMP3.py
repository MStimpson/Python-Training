import os
import ffmpy
import youtube_dl

os.system('cls')

print('\nDo NOT infringe on any copyrights!!!\n')
savePath = input('Please enter the path where you want to save the files.\nExample: C:/users/username/Music\n\n')
url = input('Please enter the url for the playlist or video you would like to download.\n')
#downloads songs
ydl = youtube_dl.YoutubeDL({'outtmpl': savePath+'/%(title)s'})
with ydl:
	result = ydl.extract_info(url, download=True)
if 'entries' in result:
	video = result['entries'][0]
else:
	video = result

#finds songs
matches=[]
for file in os.listdir(savePath):
	if file.endswith('.mkv'):
			matches.append(file)
	elif file.endswith('.webm'):
		matches.append(file)
	elif file.endswith('.mp4'):
		matches.append(file)
#converts songs		
for song in matches:
	if song.endswith('.mkv') or song.endswith('.mp4'):
		ff = ffmpy.FFmpeg( inputs={savePath+'/'+song: None},outputs={savePath+'/'+song[:-3]+'mp3': None})
		ff.run()
		for file2 in os.listdir(savePath):
			if(file2 == song[:-3]+'mp3'):
				os.remove(savePath+'/'+song)
	if song.endswith('.webm'):
		ff = ffmpy.FFmpeg( inputs={savePath+'/'+song: None},outputs={savePath+'/'+song[:-4]+'mp3': None})
		ff.run()				
		for file2 in os.listdir(savePath):
			if(file2 == song[:-4]+'mp3'):
				os.remove(savePath+'/'+song)
				
print("Finished.\n")