from rapidconnect import RapidConnect
rapid = RapidConnect('Emotions', '24aa499b-e5a4-491e-90ce-9bb0f8d75c86');
import base64
import json
import emotion
# result = rapid.call('MicrosoftEmotionAPI', 'getEmotionRecognition', { 
#   'subscriptionKey': '90febbecca1c462f871ea1d8e349d76a',
#   'image': 'http://i.imgur.com/shDtPNc.jpg'
 
# })

def faceArea(dct):
    area = dct['faceRectangle']['width']*dct['faceRectangle']['height']
    print(area)
    return area

# maxFace = max(result, key=faceArea)

def getEmotions(face):
    print(rankedEmotions)
    return rankedEmotions

def getMaxEmotion(face):
    emotionsList = dictToList(face)
    maxEmo = max(emotionsList, key=lambda x: x[1])
    print(maxEmo)
    return maxEmo

def dictToList(dct):
    keys = dct['scores'].keys()
    scores = dct['scores']
    tupList = []
    for key in keys:
        tupList.append((key, scores[key]))
    return tupList

def classifyImages(lst):
    classifications = []
    for imageStr in lst:
        lst = emotion.returnData(imageStr).decode('ascii')
        data = json.loads(lst)
        maxFace = max(data, key=faceArea)
        maxEmo = getMaxEmotion(maxFace)
        classifications.append(maxEmo)
    return classifications


if __name__ == "__main__":
    lst = ["images/image1.jpeg", "images/image2.jpeg", "images/image3.jpeg", "images/image4.jpeg", "images/image5.jpeg"]
    print(classifyImages(lst))
    #with open("images/image16.jpeg", "rb") as image_file:
    #    encoded_string = "data:image/jpeg;base64," + str(base64.b64encode(image_file.read()))
    #    print(classify_image(encoded_string))

