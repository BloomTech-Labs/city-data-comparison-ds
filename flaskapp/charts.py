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


def rent(seattle2):
    rent = seattle2['Rent']
    rentkeys = list(rent.keys())
    rentvalues = list(rent.values())
    fig2 = go.Figure(go.Bar(
            x=rentvalues,
            y=rentkeys,
            orientation='h'))

    fig2.update_layout(
        title="Rent",
        plot_bgcolor='#F9F9FB'
    )
    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON2


def housingtest(seattle):
    rng = pd.date_range('1/1/2011', periods=7500, freq='H')
    ts = pd.Series(np.random.randn(len(rng)), index=rng)

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


    rent = seattle['Rent']
    rentkeys = list(rent.keys())
    rentvalues = list(rent.values())
    orgkeys = [rentkeys[0],rentkeys[6],rentkeys[1],rentkeys[2],rentkeys[3],rentkeys[4],rentkeys[5]]
    orgvals = [rentvalues[0],rentvalues[6],rentvalues[1],rentvalues[2],rentvalues[3],rentvalues[4],rentvalues[5]]
    fig2 = go.Figure(go.Bar(
            x=orgkeys,
            y=orgvals))

    fig2.update_layout(
        title="Avg Rent Price in Seattle, Washington",
        plot_bgcolor='#F9F9FB'
    )


    built = seattle['Year Built']
    builtkeys = list(built.keys())
    builtvalues = list(built.values())
    fig3 = go.Figure(go.Bar(
            x=builtkeys,
            y=builtvalues))

    fig3.update_layout(
        title="All Properties in Seattle Washington broken down by year built",
        plot_bgcolor='#F9F9FB'
    )
    fig3.update_yaxes(title_text='% of all houses')

    bedrooms = seattle['Housing by bedrooms']
    bedroomskeys = list(bedrooms.keys())
    bedroomsvalues = list(bedrooms.values())
    fig4 = go.Figure(go.Bar(
            x=bedroomskeys,
            y=bedroomsvalues))

    fig4.update_layout(
        title="All Properties in Seattle Washington broken down by Number of bedrooms",
        plot_bgcolor='#F9F9FB'
    )
    fig4.update_yaxes(title_text='% of all houses')

    smoc = seattle['Selected Monthly Owner Costs with Mortgage']
    smockeys = list(smoc.keys())
    smocvalues = list(smoc.values())
    fig5 = go.Figure(go.Bar(
            x=smockeys,
            y=smocvalues))

    fig5.update_layout(
        title="Selected Monthly Owner Costs with Mortgage",
        plot_bgcolor='#F9F9FB'
    )
    fig5.update_yaxes(title_text='% by price range')


    vehicle = seattle['Vehicles Available']
    vehiclekeys = list(vehicle.keys())
    vehiclevalues = list(vehicle.values())
    fig6 = go.Figure(go.Bar(
            x=vehiclekeys,
            y=vehiclevalues))

    fig6.update_layout(
        title= "Number of Vehicles Available per Home",
        plot_bgcolor='#F9F9FB'
    )
    fig6.update_yaxes(title_text='% of all homes')

    Population = seattle['Population Growth']
    Populationkeys = list(Population.keys())
    Populationvalues = list(Population.values())
    fig7 = go.Figure(go.Scatter(
            x=Populationkeys,
            y=Populationvalues))

    fig7.update_layout(
        title= "Population Growth of Seattle Washington",
        plot_bgcolor='#F9F9FB'
    )
    fig7.update_yaxes(title_text='')


    males = seattle['Marital Status']['Males']
    females = seattle['Marital Status']['Females']
    maleskeys = list(males.keys())
    malesvalues = list(males.values())
    femaleskeys = list(females.keys())
    femalesvalues = list(females.values())
    fig8 = go.Figure(go.Bar(
            x=maleskeys,
            y=malesvalues,
            name='Male'))
    fig8.add_trace(go.Bar(x=femaleskeys , y=femalesvalues, name="Female"))
    fig8.update_layout(
        title= "Marital Status by Gender",
        plot_bgcolor='#F9F9FB'
    )
    fig8.update_yaxes(title_text='% of all homes')


    graphs = [fig,fig2,fig3, fig4, fig5, fig6, fig7, fig8]

    ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]
    content = [['Housing Prices', 'Data pulled from the "Historical Property Value Data" key.', 'housing'],
                ['Rent Prices','', ''],
                ['Year Structure was Built','', ''],
                ['All houses by number of bedrooms.','', ''],
                ['Selected Monthly Owner Costs with Mortgage','',''],
                ['Vehicles Available by Home','',''],
                ['Population Growth','','social'],
                ['Marital Status by Gender','','']]

    # Convert the figures to JSON
    # PlotlyJSONEncoder appropriately converts pandas, datetime, etc
    # objects to their JSON equivalents
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    return((graphJSON, ids, content))
