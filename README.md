# Animated Searching Techniques

this project used to compare different searching techniques in a weighted grid with the ability to weight individual nodes, create a goal node and change it's position , change the position of the start node, and create a wall which is a blocking node, the goal of this simulation is to find a route from the starting node to the goal node using the picked algorithm, you can create random grid with defined probability for the wall nodes, and can adjust the speed of the simulation.

this project has both frontend created using react, and backend - developed with python -  which contains the implementation of the algorithms and the API endpoints

## Installation

clone this repository locally 

```bash
git clone https://github.com/hazemayman/AI-Search-techniques.git
```
---
make sure python 3.5 or above installed and install FLASK
```bash
cd AI-Search-techniques
pip install Flask
pip install -U flask-cors
```
---
install all the required dependencies for the front end
```bash
npm install
```

## Usage
start the server by navigating to the **/api** folder and running the **api.py**
```bash
python api.py
```
---
start the react front end application by navigating. make sure you are in the root folder
```bash
npm start
```

## To use optimized Build Version

instead of running in development mode using **npm start**, you can try to build the source code and serve it for optimized more smooth version of the application

make sure you are on the root folder

```bash
npm run build
npm install -g serve
serve -s build
```
## Screenshots 
<p align="center">
  <img src="./ss/action.gif" alt="animated" />
</p>