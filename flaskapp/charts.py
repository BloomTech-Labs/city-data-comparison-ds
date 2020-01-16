import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import json


def seattle():
    with open('data/seattle.json', 'r') as myfile:
        data=myfile.read()
    seattlejsn = json.loads(data)
    return(seattlejsn)

def housing(seattle):
    homevals = seattle['Historical Property Value Data']
    avghome = homevals['Average Home Value']
    dates = list(avghome.keys())
    values = list(avghome.values())
    onedates = list(homevals['One Bedroom Houses'].keys())
    onevalues = list(homevals['One Bedroom Houses'].values())
    twodates = list(homevals['Two Bedroom Houses'].keys())
    twovalues = list(homevals['Two Bedroom Houses'].values())
    threedates = list(homevals['Three Bedroom Houses'].keys())
    threevalues = list(homevals['Three Bedroom Houses'].values())
    fourdates = list(homevals['Four Bedroom Houses'].keys())
    fourvalues = list(homevals['Four Bedroom Houses'].values())
    fivedates = list(homevals['Five Bedroom Houses'].keys())
    fivevalues = list(homevals['Five Bedroom Houses'].values())
    fig = go.Figure(data=go.Scatter(x=dates, y=values, name='Avg Price for all homes',
                        line = dict(color='black', width=4, dash='dash')))

    fig.update_layout(
        title="Seattle Washington Property Value",
        plot_bgcolor='#F9F9FB'
    )
    fig.add_trace(go.Scatter(x=onedates, y=onevalues,
                        mode='lines',
                        name='One Bedroom Houses'))
    fig.add_trace(go.Scatter(x=twodates, y=twovalues,
                        mode='lines',
                        name='Two Bedroom Houses'))
    fig.add_trace(go.Scatter(x=threedates, y=threevalues,
                        mode='lines',
                        name='Three Bedroom Houses'))
    fig.add_trace(go.Scatter(x=fourdates, y=fourvalues,
                        mode='lines',
                        name='Four Bedroom Houses'))
    fig.add_trace(go.Scatter(x=fivedates, y=fivevalues,
                        mode='lines',
                        name='five Bedroom Houses'))
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON
