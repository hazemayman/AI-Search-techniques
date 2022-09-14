import React, { Component } from "react";
import Node from '../Node/Node'
import './Board.css'


const NUMBER_OF_ROWS  = 20;
const NUMBER_OF_COLMS = 50;
const Start_node_row = 0
const Start_node_colm = 0

const finish_node_row = NUMBER_OF_ROWS-1
const finish_node_colm =NUMBER_OF_COLMS-1
let newGrid;
let Weights_on = false;
let val="BFS";
let speed=10;
let random=10;

class Board extends Component{
    constructor(props){
        super(props);
        this.state = {
            grid : [],
            MousePressedOn : false,
        }

    }


    randomObs(){
        let percentage = random/100;
        let k = 10
        let A = []
        for(var i = 0; i <NUMBER_OF_COLMS;i++){
                
            for(var j = 0; j <NUMBER_OF_ROWS;j++){
               
                 A.push([i,j])
            }
        }
        for(let i =0; i < A.length-1;i++){
            setTimeout(() => {
                let nm = Math.random();
                if(nm < percentage){
                    getNewGridAfterChange(this.state.grid , A[i][0] , A[i][1]);
                    k = k + 10;
                
                    this.setState({MousePressedOn : false});
                }
            }, k);
        }


    }
    componentDidMount(){
        const grid = CreateInitialGrid();
        this.initiate();
        this.setState({grid});
    }

    hadnleMouseDown(col , row){
        let sliderr = document.getElementById("goalState");
        if(sliderr.checked){
            createGoalNode(this.state.grid , col , row)
            this.setState({ MousePressedOn : false});
        }else{
            newGrid = getNewGridAfterChange(this.state.grid , col , row);
            this.setState({ MousePressedOn : true});
        }


    }
    hadnleMouseonHold(col , row){
        if(!this.state.MousePressedOn ) return;
        if(newGrid){
            let changedGrid = chnagePos(this.state.grid,col,row)
            this.setState({grid : changedGrid})
            newGrid = this.state.grid[col][row]
        }else{
            getNewGridAfterChange(this.state.grid , col , row);
            this.setState({MousePressedOn : true});
        }
        


    }
    MouseUp(){
      this.setState({MousePressedOn : false});

    }
    initiate(){
        let buttonClear = document.getElementById("clear");
        buttonClear.addEventListener('click' , ()=>{
            this.clearGrid()
        })
        let button1= document.getElementById("start");
        button1.addEventListener('click',()=>{
            this.startAlgorithm();
        })
        let button2= document.getElementById("weights");
        button2.addEventListener('click', ()=>{
            Weights_on = !Weights_on;
            this.setState({MousePressedOn : false});
            this.ResetBoard();
        })
        let button3= document.getElementById("reset");
        button3.addEventListener('click',()=>{
            this.setState({MousePressedOn : false});
            this.ResetBoard();
        })
        let button4= document.getElementById("random");
        button4.addEventListener('click',()=>{
            this.randomObs();
        })
        document.getElementById("BFS").addEventListener('click',()=>{
            val = 'BFS';
        })
        document.getElementById("DFS").addEventListener('click',()=>{
            val = 'DFS';
        })
        document.getElementById("UCS").addEventListener('click',()=>{
            val = 'UCS';
        })
        document.getElementById("DLS").addEventListener('click',()=>{
            val = 'DLS';
        })
        document.getElementById("IDDS").addEventListener('click',()=>{
            val = 'IDDS';
        })
        document.getElementById("A*").addEventListener('click',()=>{
            val = 'A*';
        })
        document.getElementById("Greedy").addEventListener('click',()=>{
            val = 'Greedy';
        })

        document.getElementById("value").innerHTML = document.getElementById("myRange").value; // Display the default slider value

        document.getElementById("myRange").oninput = function() {
            
            document.getElementById("value").innerHTML = speed;
            speed=this.value;
     
            
        }
        document.getElementById("value1").innerHTML = document.getElementById("myRange1").value; // Display the default slider value

        document.getElementById("myRange1").oninput = function() {
            
            document.getElementById("value1").innerHTML = random;
            random=this.value;
     
            
        }
    }
    ResetBoard(){
        let newGrid = CreateInitialGrid();

        for(var i = 0; i <NUMBER_OF_COLMS;i++){
            for(var j = 0; j <NUMBER_OF_ROWS;j++){
                if(i == Start_node_colm && j == Start_node_row){
                    document.getElementById('node-'+i+'-'+j).className = 'node node-start'
                }else if(i == finish_node_colm && j == finish_node_row){
                    document.getElementById('node-'+i+'-'+j).className = 'node node-finish'
                }else{
                    document.getElementById('node-'+i+'-'+j).className = 'node'
                }
             
            }
        }

        this.setState({grid : newGrid});
    }

    startAlgorithm(){
        const sendGrid = ConvertGrid(this.state.grid);

        
        fetch('http://127.0.0.1:5000/api/SendData' , {
            method : 'POST',
            headers : {
            'Content-Type' : 'application/json',
            },
            body : JSON.stringify([sendGrid,val])
        })
        .then(res => res.json())
        
        .then(data => {
            console.log("success loading");
            let shortestPath = data.path;
            let closeSet = data.closeSet;
            let SpeedOfAnimation = speed;
            let myGrid = this.state.grid;
            for(let i = 1;i<closeSet.length-1;i++){
                if(i === closeSet.length-2){
                    setTimeout(()=>{
                      animateTheShortestPath(shortestPath , myGrid);
                    }, SpeedOfAnimation * i)
                }
                setTimeout(()=>{
                    const Node = myGrid[closeSet[i][0]][closeSet[i][1]]
                    Node.is_visted_node = true;
                    document.getElementById('node-'+Node.col+'-'+Node.row).className = 'node node-visited';
                }, SpeedOfAnimation * i)
            }

        }).catch((error) => {
            console.error('error : ' , error);
        });

        


    }
    clearGrid(){
        for(let i = 0;i<NUMBER_OF_COLMS;i++){
            for(let j = 0;j<NUMBER_OF_ROWS;j++){
                let node = document.getElementById("node-"+i+'-'+j)
                    node.classList.remove("node-visited")
                    node.classList.remove("node-final-path")

            }
        }
    }
    render(){ 

        const {grid , MousePressedOn} = this.state;
        return(
            <React.Fragment>

           
            <div className="text-center Board-container">
                {grid.map((col , colIndex)=>{
                    return(
                    <div className={"column col" + colIndex}>
                        {col.map((NodeElement , NodeIndex) =>{
                            const {col , row ,weight  , isFinish , isStart , isWall} = NodeElement
                            return(
                                <Node
                                key = {NodeIndex}
                                col = {col}
                                row = {row}
                                weight = {Weights_on? weight : null}
                                iswall = {isWall}
                                isStart = {isStart}
                                isFinshed = {isFinish}
                                MousePressedOn = {MousePressedOn}
                                mouseDown = {(col , row) => this.hadnleMouseDown(col , row)}
                                mouseUp = {() => this.MouseUp()}
                                mouseOnHold = {(col , row) => this.hadnleMouseonHold(col , row)}
                                ></Node>
                            );
                        })}
                    </div>
                    );
                })}
            </div>
            </React.Fragment>
           
        )
    }
}


const CreateInitialGrid = () =>{
    const grid = [];
    for(var i = 0; i <NUMBER_OF_COLMS;i++){
        grid.push(Array(NUMBER_OF_ROWS));
    }
    for(var i = 0; i <NUMBER_OF_COLMS;i++){
        for(var j = 0; j <NUMBER_OF_ROWS;j++){
            grid[i][j] = CreateNode(i,j);
        }
        
    }
    return grid;
}
const animateTheShortestPath = (ShortestPath , myGrid) =>{
    for(let i = 1;i<ShortestPath.length-1;i++){
        setTimeout(() => {
            const Node = myGrid[ShortestPath[i][0]][ShortestPath[i][1]];
            document.getElementById('node-'+Node.col+'-'+Node.row).className = 'node node-final-path';
        }, i * 20);
    }
}
function generateRandomIntegerInRange(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
const CreateNode = (col , row) =>{
    return{
        col,
        row,
        weight : Weights_on ?  generateRandomIntegerInRange(10 , 50): 1 ,
        isWall : false,
        isVisted : false,
        isStart : row === Start_node_row && col === Start_node_colm,
        isFinish : row === finish_node_row && col === finish_node_colm,
        ParentNode : null,
        f : 0,
        h : 0,
        g : 0,
    }
}


const getNewGridAfterChange = (grid , col , row) =>{

    const newGrid = grid.slice();
    const Node = newGrid[col][row];
    if (Node.isFinish == true || Node.isStart == true){
        return Node;
    }
    const NewNode = {
        ...Node,
        isWall : !Node.isWall,
    }
    newGrid[col][row] = NewNode;
    

}
const createGoalNode = (grid , col , row) =>{

    const newGrid = grid.slice();
    const Node = newGrid[col][row];
    if(Node.isStart == false){
        const newNode = {
            ...Node,
            isFinish: !Node.isFinish
        }
        newGrid[col][row] = newNode;
    }
   
}
const chnagePos = (grid , col , row) =>{
    let cur_state = newGrid.isFinish? "finish" : "start";
    const dumpArray = grid.slice();
    const Node = dumpArray[col][row];
    if(cur_state == "start"){
        const newNode = {
            ...Node,
            isStart : true,
            iswall : false
        }
        const lastnode = {
            ...newGrid,
            isStart : false,
            iswall : false
        }
        dumpArray[col][row] = newNode;
        dumpArray[lastnode.col][lastnode.row] = lastnode
        return dumpArray

    }else{
        const newNode = {
            ...Node,
            isFinish : true,
            iswall : false
        }
        const lastnode = {
            ...newGrid,
            isFinish : false,
            iswall : false
        }
        dumpArray[col][row] = newNode;
        dumpArray[lastnode.col][lastnode.row] = lastnode
        return dumpArray

    }


}

const ConvertGrid = (grid) =>{
    let sendGrid = []
    for(var i = 0; i <NUMBER_OF_COLMS;i++){
        sendGrid.push(Array(NUMBER_OF_ROWS));
    }

    for(var i = 0; i <NUMBER_OF_COLMS;i++){
        for(var j = 0; j <NUMBER_OF_ROWS;j++){
            if(grid[i][j].isWall){
                sendGrid[i][j] = [3,grid[i][j].weight];

            }else if(grid[i][j].isStart){
                sendGrid[i][j] = [1,grid[i][j].weight];
                
            }else if(grid[i][j].isFinish){
                sendGrid[i][j] = [2,grid[i][j].weight];
                
            }else{
                sendGrid[i][j] = [4,grid[i][j].weight];
            }

            
        }
    }

    // console.log(sendGrid)
    return sendGrid;

}

export default Board;