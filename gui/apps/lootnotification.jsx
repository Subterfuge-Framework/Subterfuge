import React from 'react';
import ReactDOM from 'react-dom';
 
var LootNotification = React.createClass({
  render: function() {
    return (
      <div id = "notificationbox">5</div>
    );
  }
});
ReactDOM.render(
  <LootNotification />,
  document.getElementById('lootnotificationbox')
);