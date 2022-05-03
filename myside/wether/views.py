from django.shortcuts import render
from .wether_api import wether as api, numbers, interval_time
from plotly.offline import plot
from plotly.graph_objs import Scatter
# Create your views here.


def wether(request):

    x_data = [0, 1, 2, 3, 4]
    y_data = [1, 5, 6, 7, 8]
    plot_div = plot([Scatter(x=x_data, y=y_data, mode='lines', name='test', opacity=0.8, marker_color='green')], output_type='div')

    context = {
        'text': api,
        'values': numbers,
        'time': interval_time,
        'start': interval_time[0],
        'end': interval_time[-1],
        'plot_div': plot_div,
        }
    
    return render(request, 'wether/wether.html', context)

