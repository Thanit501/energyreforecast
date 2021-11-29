import matplotlib.pyplot as plt
import seaboorn as sns 
import base64
import pandas as pd
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    prd = model.predict(x)
    plt.grid()
    plt.scatter(x,y)
    plt.title("Production of energy")
    plt.xlabel("Ton")
    plt.ylabel("MWh")
    plt.plot(x,prd, linewidth='1')
    plt.show()
    return graph



