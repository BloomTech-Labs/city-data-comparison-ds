import difflib
import json


def data_loader():
    """This opens the JSON obj for all the city names."""
    with open('apps/data/spellcheck/spell_check_opject2.json', 'r') as myfile:
        data = myfile.read()
        obj = json.loads(data)
    return(obj)


def check_spelling(data, words):
    """This function taks a city name and check for the closest match in a list of words."""
    jsn = {}
    id_manager = []
    for i in difflib.get_close_matches(words.lower(), list(data.keys()), n=15):
        if list(data[i].values())[0]['ID'] not in id_manager:
            id_manager.append(list(data[i].values())[0]['ID'])
            jsn[list(data[i].keys())[0]] = list(data[i].values())[0]
        else:
            pass
    if len(jsn) > 0 and len(jsn) <= 5:
        res = jsn
    elif len(jsn) > 5:
        short_dict = {}
        for i in list(jsn.keys())[0:5]:
            short_dict[i] = jsn[i]
        res = short_dict

    else:
        if len(words.split()) <= 1:
            res = {'No Data': f'Cannot find {words}, please include the State name along with the City you are searching for.'}
        else:
            res = {'No Data': f'Cannot find {words}, please check the spelling or search for another City.'}
    return(res)


def force_id(data, words):
    """This funtion takes single word that you want to search for in a
    array and finds the most similarly spelled word. If there are no
    close matches it will return the city data for Seattle"""
    jsn = {}
    res = difflib.get_close_matches(words.lower(), list(data.keys()), n=1)
    if len(res) > 0:
        jsn['data'] = data[res[0]]
        jsn = jsn['data'][list(jsn['data'].keys())[0]]['ID']
    else:
        jsn['data'] = data['Seattle WA']
        jsn = jsn['data']['Seattle, WA']['ID']
    return(jsn)
