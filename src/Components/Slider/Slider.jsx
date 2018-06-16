import React, { Component } from 'react';
import debounce from '../../config/util';
import info from '../../config/configs';

export default class Slider extends Component {

    mouseMoveHandler = (evt) => {
        debounce(this.getBookLocation(evt),250);
    }

    getBookLocation = (evt) => {
        evt.clientY;
        console.log(evt.clientY);
    }

    render() {
        return <div onMouseMove={this.mouseMoveHandler} className="o-slider">
        </div>
    }
}