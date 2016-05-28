import React from 'react';
import ReactDOM from 'react-dom';
 
//Get Installed Feeds
var FeedTable = React.createClass({
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
      <AvailableFeeds data = {this.state.data} />
    );
  }
});
var AvailableFeeds  = React.createClass({
  render: function() {
    var feedNodes = this.props.data.map(function(feed) {
         return (
            <div id = "panelform">
            <span style={{float:'left'}}>{feed.Name}</span>
            <br /><br />
            </div>
         );
    });
    return (
    <b>{feedNodes}</b>
    );
  }
});
ReactDOM.render(
   <FeedTable url={'/packages/feeds.json'} />,
   document.getElementById('fjobs')
);