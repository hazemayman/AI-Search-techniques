import script as script
from flask import Flask, request, jsonify
app = Flask(__name__, static_folder='../build', static_url_path='/')


@app.route('/api/SendData', methods=['GET', 'POST'])
def get_current_time():
    data = request.json
    if(data[1] == 'BFS'):
        myBFS = script.BFS(data[0])
        myBFS.SearchForPath()
    if(data[1] == 'DFS'):
        myBFS = script.BFS(data[0])
        myBFS.SearchForPathDFS()
    if(data[1] == 'UCS'):
        myBFS = script.BFS(data[0])
        myBFS.SearchForPathUCS()
    if(data[1] == 'DLS'):
        myBFS = script.BFS(data[0])
        myBFS.SearchForPathDLS()
    if(data[1] == 'IDDS'):
        myBFS = script.BFS(data[0])
        myBFS.SearchForPathIDDS()
    if(data[1] == 'A*'):
        myBFS = script.BFS(data[0])
        myBFS.SearchForPathASTAR()
    if(data[1] == 'Greedy'):
        myBFS = script.BFS(data[0])
        myBFS.SearchForPathGreedy()
    closeSet = myBFS.returnCloseSet()
    print(len(closeSet))
    return {'closeSet': closeSet, 'path': myBFS.returnPath()}

@app.route('/')
def index():
    return app.send_static_file('index.html')
