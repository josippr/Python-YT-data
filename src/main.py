
import urllib.request
import json

#full request: https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=pewdiepie&key="YOUR_API_KEY"


def request(name, api_key):
    
    #get data for the requested channel
    data = urllib.request.urlopen('https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=' + name + '&key=' + api_key).read()
    
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    views = json.loads(data)["items"][0]["statistics"]["viewCount"]
    #comments = json.loads(data)["items"][0]["statistics"]["commentCount"]
    videos = json.loads(data)["items"][0]["statistics"]["videoCount"]

    print("Statistics for " + name + ":" + "\nTotal subscribers: " + subs + "\nTotal comments: " + "\nTotal video views: " + views + "\nTotal uploaded videos: " + videos)



def main():
    
    #api key from console.developer.google.com; 
    #Youtube data v3 enabled
    api_key = "YOUR_API_KEY"

    #get channel username
    youtube_channel_username = input("Enter YouTube channel username: ")

    #get data
    request(youtube_channel_username, api_key)


if __name__ == "__main__":
    main()