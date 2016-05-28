import React from 'react';
import ReactDOM from 'react-dom';
 

//LootTable
//Track & Update Loot
var LootTable = React.createClass({
  loadLootFromServer: function() {
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
    
      /*console.log(this.state.data);
      var json = this.state.data;
      for(var i = 0; i < json.length; i++) {
         var obj = json[i];
         console.log(obj.id);
      }*/
  },
  getInitialState: function() {
    return {data: []};
  },
  componentDidMount: function() {
    this.loadLootFromServer();
    setInterval(this.loadLootFromServer, this.props.pollInterval);
  },
  
  //var tmp = this.state.data;
  

  render: function() {
    return (
      <Loot data = {this.state.data} />
      
    );
  }
});


      /*
      if ({loot.New} == 1){
         newLoot = newLoot + 1;
         alert(newLoot);
      }*/

var newLoot = 0;

//Loot
//Build Loot Table
var LootRow = React.createClass({
   render: function() {

      var details = this.props.loot.Details.split("#")
      
      var source = details[0]
      var protocol = details[1]
      var type = details[2]
      var loot = details[3]
      
      return (
         <tr className={"lootrow"+(this.props.loot.ID%2 ? "a":"b")}>>
            <td>{source}</td>
            <td>{protocol}</td>
            <td>{type}</td>
            <td>{loot}</td>
            <td>{this.props.loot.Datetime}</td>
         </tr>
      );
   }
});


var Loot = React.createClass({
  render: function() {
    var rows = [];
    var lootNodes = this.props.data.forEach(function(loot) {
      if (loot.ID == "1") {
         newLoot = 0;
      }
      if (loot.New == "1") {
         newLoot ++;
         
      }

      rows.push(<LootRow loot={loot} key={loot.ID} />)
      
      });
      
      //Set Loot Indicator
      if (newLoot != 0) {
         $(document.getElementById("lootnotificationbox")).show();
         document.getElementById("lootnotificationbox").innerHTML = '<div id = "notificationbox"><center><b>' + newLoot + '</b></center></div>';
      }
      else {
         $(document.getElementById("lootnotificationbox")).hide();
      } 
    
    
      //Build Loot Table
      //Do UNION join on HID to get host
      return (
         <table className="lootlist">
            <thread>
               <tr className="lootbar"><td>Source</td><td>Protocol</td><td>Type</td><td>Loot Details</td><td>Date</td></tr>
            </thread>
            <tbody>{rows}</tbody>
         </table>
      );
    


  }
});

var qstring = "SELECT * from Loot"

ReactDOM.render(
   <LootTable url={'/dbquery?qstring=' + btoa(qstring)} pollInterval={2000} />,
   document.getElementById('lootfeed')
);