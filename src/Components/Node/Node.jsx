import React, {Component} from 'react';
import './Node.css'
 class Node extends Component{  
    render(){
        const {
            col,
            row,
            weight,
            iswall,
            isStart,
            isFinshed,
            mouseDown,
            mouseUp,
            mouseOnHold
        } = this.props;
        const nodeClass = isFinshed ? "node-finish": isStart ? "node-start" : iswall ? "node-wall" : ""
        return(
            <div
            id = {'node-'+col+'-'+row}
            className={'text-center node ' + nodeClass } 
            onMouseDown = {() => mouseDown(col , row)}
            onMouseEnter = {() => mouseOnHold(col , row)}
            onMouseUp = {() => mouseUp()}
            > {weight}
            </div>
        );
    }
}

export default Node;
