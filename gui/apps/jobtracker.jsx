import React from 'react';
import ReactDOM from 'react-dom';
 
//Active Job Tracker
var JobTable = React.createClass({
  loadJobsFromServer: function() {
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
    this.loadJobsFromServer();
    setInterval(this.loadJobsFromServer, this.props.pollInterval);
  },
  render: function() {
    return (
      <Job data = {this.state.data} />
    );
  }
});

var killJob = function(event) {
   console.log(event);
   //this.setState({data: "badfa"});
   
   var qstring = "UPDATE Jobs SET Active = 0 where ID = " + event.ID
   
   //DB UPDATE QUERY
    $.ajax({
      url: '/dbupdate?qstring=' + btoa(qstring),
      dataType: 'json',
      cache: false,
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }
    });

   var qstring = "UPDATE Jobs SET Enabled = 0 where ID = " + event.ID
   
   //DB UPDATE QUERY
    $.ajax({
      url: '/dbupdate?qstring=' + btoa(qstring),
      dataType: 'json',
      cache: false,
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }
    });

}

//Build Job Table
var Job = React.createClass({

   render: function() {
      //this.handleClick("asdf");
      //console.log(this.props.data)
      var blah = "ASDFASD"

      var jobNodes = this.props.data.map(function(job, blah) {

      if (job.Enabled == 1) { var runningJob = 'gui/images/loader.gif'; } else { var runningJob = '';}
   
            
            
      if (job.Active == "1"){
         //Build Job Table
         return (
            <span>
            <img style={{float:'right'}} src = {runningJob} />
            <span style={{float:'left'}}>{job.Name}</span>
            <div id = "job_cancel_icon" onClick={killJob.bind(this, job)} name = {job.ID}  style={{float:'right'}}><span className = "icon-cancel-circle"></span></div>
            <br /><br />
            </span>
         );
      }

      });
      return (
      <b>{jobNodes}</b>
      );
   }
});



var qstring = "SELECT * from Jobs"

ReactDOM.render(
   <JobTable url={'/dbquery?qstring=' + btoa(qstring)} pollInterval={1000} />,
   document.getElementById('ajobs')
);