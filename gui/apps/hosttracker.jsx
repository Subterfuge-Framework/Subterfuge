import React from 'react';
import ReactDOM from 'react-dom';

//HostList
//Track & Update Hosts
var HostList = React.createClass({
  loadHostsFromServer: function() {
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
  getInitialState: function() {
    return {data: []};
  },
  componentDidMount: function() {
    this.loadHostsFromServer();
    setInterval(this.loadHostsFromServer, this.props.pollInterval);
  },
  

  render: function() {
    return (
      <Host data = {this.state.data} />
    );
  }
});

//Host
//Build Host Columns
var Host = React.createClass({
  render: function() {
    var hostNodes = this.props.data.map(function(host) {
      //Build Host Rows
      return (
      <div id = "hostrow">
         <div id = "hostfill">
            <div id = "hostdetails">
              <center><span className = "hostdetails">
                {host.Host}
              </span></center>
              <span className="hostdescription">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IP Address</span>
            </div>
            <div id = "hostdetails">
               <center><span className = "hostdetails">{host.OS}</span></center>
               <span className = "hostdescription">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OS</span>
            </div>
            <div id = "hostdetails">
               <span className = "hostdetails"><div id = "lootbox" className = "loot"><center>10</center></div></span>
               <span className = "hostdescription">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Loot</span>
            </div>
            <div id = "hostdetails">
               <center><span className = "hostdetails">{host.LastActive}</span></center>
               <span className = "hostdescription">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Last Active</span>
            </div>
         </div>
      </div>
      );
    });
    return (
    <b>{hostNodes}</b>

    );
  }
});

var qstring = "SELECT * from Hosts"

ReactDOM.render(
   <HostList url={'/dbquery?qstring=' + btoa(qstring)} pollInterval={2000} />,
   document.getElementById('hostsfeed')
);