function showFeed(feed)
{
   $(document.getElementsByName("feedcont")).hide()
   $("#" + feed.className).show()
}

function test(ID)
{
   $.post("/start/", {
      status:  "go"
   });   
   
   //alert(ID);
}



function notificationUpdate(ID)
{
   var nloot = document.getElementById("new_loot").innerHTML;
   document.getElementById(ID).innerHTML = "<center><b>" + nloot + "</b></center>";
}


function dbQuery(qstring)
{
   //POST request to py to get db response
    $.ajax({
      url: '/dbquery?qstring=' + btoa(qstring),
      dataType: 'json',
      cache: false,
      success: function(data) {
        this.setState({data: data});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
   
   
   
   
   //alert(result)    '/dbquery?qstring=' + btoa(qstring)
   
   //return result
   
   
   //$('#CheckIn').load('/dbquery?qstring=' + btoa(qstring));
   
   //var nloot = document.getElementById("new_loot").innerHTML;
   //document.getElementById(ID).innerHTML = "<center><b>" + nloot + "</b></center>";
}


$(document).ready(function () {
   
   $(document.getElementsByName("feedcont")).hide()
   $("#hostsfeed").show();
   
   //Page Setup from variables
   //Get by name & iterate through IDs
   //notificationUpdate("notificationbox_b");
   
   //dbQuery("tbd");
   
   /*
  
        //Code executed when start button actuated
    $('a[name=start]').click(function(e) {
            //Cancel the link behavior
        e.preventDefault();
            //Get the A tag
        var id = $(this).attr('href');
        
            //Start Pwning
        $(".manualgate").fadeIn("slow");
        $(".autogate").fadeOut("slow");

    });

   */
    
  
});