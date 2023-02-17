import pytube
video_url = 'https://www.youtube.com/watch?v=lIi7Jj32XUc&ab_channel=top10movies'
try:
    video = pytube.YouTube(video_url).streams.first()  
    video.download('Users\Expert\Desktop\practice')  
    print("Success: The file is downloaded.")
except:
    print("Error: There might be an issue with the url provided.")