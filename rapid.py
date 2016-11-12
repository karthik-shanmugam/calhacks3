from rapidconnect import RapidConnect
rapid = RapidConnect('Emotions', '24aa499b-e5a4-491e-90ce-9bb0f8d75c86');
import base64
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
    print(emotionsList)
    maxEmo = max(emotionsList, key=lambda x: x[1])
    return maxEmo

def dictToList(dct):
    keys = dct['scores'].keys()
    scores = dct['scores']
    tupList = []
    for key in keys:
        tupList.append((key, scores[key]))
    return tupList

# print(getMaxEmotion(maxFace))


def classify_image(link):
    result = rapid.call('MicrosoftEmotionAPI', 'getEmotionRecognition', { 
        'subscriptionKey': '90febbecca1c462f871ea1d8e349d76a',
        'image': link
    })
    print(link)
    print(result)
    if result:
        maxFace = max(result, key=faceArea)
        return getMaxEmotion(maxFace)
    else:
        return "none"

if __name__ == "__main__":
    with open("images/image16.jpeg", "rb") as image_file:
        encoded_string = image_file.read()
        print(classify_image(encoded_string))

