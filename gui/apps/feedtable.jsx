import React from 'react';
import ReactDOM from 'react-dom';

import Form from "react-jsonschema-form";
 
var classNames = require("classnames");




//Get Installed Feeds
var FeedTable = React.createClass({
  getInitialState: function() {
    return { data: [] };
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

var OpenFeed = function(event) {
   console.log(event);
   hideFeeds();
   showFeedForm(event.id);

}

var FeedForm  = React.createClass({
   render: function() {
      
      const formData = {};

      const log = (type) => console.log.bind(console, type);
      const onSubmit = ({formData}) => submitData({formData});

      return (
         <div id = {this.props.data.id} className = "feedformbox">
           <Form schema={this.props.data}
                 formData={formData}
                 onChange={log("changed")}
                 onSubmit={onSubmit}
                 onError={log("errors")} />
         </div>
      );
   }
});

function submitData(data) {
   $.post("/settings/", data);
   hideFeedForms();
   showFeeds();
}
      
var AvailableFeeds  = React.createClass({
   render: function() {
      var feedNodes = this.props.data.map(function(feed) {
         console.log(feed)
         return (
            <div id = "panelform" className="feedformtitle" key={feed.id}>
            <span className="feedtitle" style={{float:'left'}} onClick={OpenFeed.bind(this, feed)}>{feed.title}</span>
                                          
            <FeedForm data = {feed} key={feed.id} />

                                          
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