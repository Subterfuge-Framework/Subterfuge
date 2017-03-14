import React from 'react';
import ReactDOM from 'react-dom';
 
//Get Installed Vectors
var VectorTable = React.createClass({
  getInitialState: function() {
    return {data: []};
  },
  componentDidMount: function() {
    $.ajax({
      url: this.props.url,
      dataType: 'json',
      cache: false,
      success: function(data) {
        this.setState({data: data});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },

  render: function() {
    return (
      <AvailableVectors data = {this.state.data} />
    );
  }
});
var handleClick = function(vector) {
      console.log(vector);
}
var AvailableVectors  = React.createClass({
  render: function() {
   return (
      <b>
      {this.props.data.map(function(vector) {
         return (
            <span>
            <div id = "job_cancel_icon"  style={{float:'left'}} onClick={handleClick.bind(this, vector)} value = "tmp"><span className = "icon-plus"></span></div>

            <span style={{float:'left'}}>{vector.Name}</span>
            <br /><br />
            </span>
         );
      })}
      </b>
    );
   }
});
ReactDOM.render(
   <VectorTable url={'/packages/vectors.json'} />,
   document.getElementById('vjobs')
);