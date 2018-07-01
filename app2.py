from difflib import SequenceMatcher
import json, glob

with open("./challenge/challenge_set.json") as f:    
    input = json.load(f)
    
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def getData(path):
    with open(path) as f:    
        data = json.load(f)
    return data

def getPlaylistNameSimilarity(data, name):
    for i, playlist in enumerate(data["playlists"]):
        data["playlists"][i]["similarity_score"] = similar(name, playlist["name"])
    return data

def getRecommendTrack(name, pid):
    count = 0
    for filePath in glob.glob('./data/*.json'):
        data = getPlaylistNameSimilarity(getData(filePath), name)
        data['playlists'] = sorted(data['playlists'], key=lambda key:key['similarity_score'], reverse=True)
        for i, track_list in enumerate(data['playlists']):
            x_input = validateTrackList(input["tracks"])
            y_input = validateTrackList(track_list['tracks'])
            data["playlists"][i]["recommend_similarity_score"] = len(set(x_input).intersection(y_input))
        data['playlists'] = sorted(data['playlists'], key=lambda key:key['recommend_similarity_score'], reverse=True)
        recommend_list = []
        for i in data['playlists']:
            recommend_list = recommend_list + list(set(validateTrackList(i["tracks"])) - set(recommend_list))
        recommend_list = list(set(recommend_list) - set(validateTrackList(input['playlists']['name']['tracks'])))
        recommend_list = recommend_list[:500]
        count = count + 1
        print(count)
    printOutput(pid, recommend_list)
    return recommend_list

def printOutput(pid, list):
    import csv
    list.insert(0, pid)
    with open('test.csv', 'a') as flist:
        wr = csv.writer(flist, quoting=csv.QUOTE_ALL)
        wr.writerow(list)

def validateTrackList(track_list):
    validated_list = []
    for i in track_list:
        validated_list.append(i["track_uri"])
    return validated_list

if __name__ == "__main__":
    for i in input['playlists']:
        getRecommendTrack(i['name'], i['pid'])