import React, { Component } from 'react'

export default class Footer extends Component {
  render() {
    return (
      <div>
          <p>
          {this.props.name}
          </p>
      </div>
    )
  }
}
Footer.defaultProps = {name: "-------------------------------------  Footer  ---------------------------------------"}