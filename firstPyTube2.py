from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=k8Mc8YRigmw")

#print(yt.get_videos())
print(yt.filename)

yt.filter('mp4')[-1]


#video = yt.get('mp4','720p')

#video.download('/tmp/')