import difflib
import json

def spellchecker(words):
    with open('data/spellcheck/spell_check_opject.json', 'r') as myfile:
        data=myfile.read()
    obj = json.loads(data)
    jsn = {}
    lenth = []
    for i in difflib.get_close_matches(words.lower(), list(obj.keys()), n=5):
        lenth.append(i)
        jsn[list(obj[i].keys())[0]] = list(obj[i].values())[0]
    if len(lenth) > 0:
        res = jsn
    else:
        if len(words.split()) <= 1:
            res = {'No Data': f'Cannot find {words}, please include the State name along with the City you are searching for.'}
        else:
            res = {'No Data': f'Cannot find {words}, please check the spelling or search for another City.'}
    return(res)
