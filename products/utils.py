import matplotlib.pyplot as plt
import seaborn as sns 
from io import BytesIO
import base64

def get_image():
    # create a bytes butter for the image to save 
    buffer = BytesIO()
    # create the plot with the use of BytesIO as its file 
    plt.savefig(buffer, format='png')
    # set  the cursor the begining of the stream
    buffer.seek(0)
    # retreive the entire content of the file 
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')

    # free the memory of the buffer 
    buffer.close()
    return graph 


def get_simple_plot(chart_type,*args,**kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10,4))
    # x
    x = kwargs.get('x')
    # y 
    y = kwargs.get('y')
    # data 
    data = kwargs.get('data')
    print(data)
    if chart_type == 'bar plot':
        title = "Total price by Day(Bar)"
        plt.title(title)
        plt.bar(x, y)
    elif chart_type == 'line plot':
        title = "Total price by Day(Line)"
        plt.title(title)
        plt.plot(x, y)
    else: 
        title = "Product Count"
        plt.title(title)
        sns.countplot(x="name",data=data)

    plt.tight_layout()
    graph = get_image()
    return graph 
        