import plotly
from plotly.graph_objs import Scatter, Layout
import dataparse
import datetime

wave_list = dataparse.get_wave_dic()

data_height = []

""" create a list of tuples with (datetime, wave height)"""
for entry in wave_list:
    data_height.append((datetime.datetime.strptime(entry["date_time"], "%Y-%m-%dT%H:%M:%SZ"), entry["sea_surface_wave_significant_height (m)"]))

data_height.sort()

plotly.offline.plot({
    "data": [Scatter(x=[a.strftime("%Y-%m-%d %H:%M:%S") for (a, b) in data_height], y=[d for (c, d) in data_height])],
    "layout": Layout(title="Wave Height")
})
