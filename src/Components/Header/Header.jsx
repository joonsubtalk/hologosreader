import React, { Component } from 'react'
import Tab from '../Tab/Tab';

export default class Header extends Component {

  render() {
    return (
      <div className="o-header">
        <div className="o-header__tabContainer">
            <Tab />
        </div>
      </div>
    )
  }
}
