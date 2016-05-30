function showFeed(feed)
{
   $(document.getElementsByName("feedcont")).hide()
   $("#" + feed.className).show()
}

function startpwn(ID)
{
   $.post("/start/", {
      status:  "go"
   });   
   
   $("#startpwn").hide();
   $("#attack_loader").show("slow");
   $("#stoppwn").show();
}

function stoppwn(ID)
{
   $.post("/stop/", {
      status:  "no-go"
   });   
   
   $("#stoppwn").hide();
   $("#attack_loader").hide("slow");
   $("#startpwn").show();
}

function toggleMenu(iid){
   $("#sidebar_border_fix").toggle();
   
   var ID = "#" + iid + "s";
   //alert(ID);
   
   // create menu variables
   var slideoutMenu = $(ID);
   var slideoutMenuWidth = $(ID).width();

   // toggle open class
   slideoutMenu.toggleClass("open");

   // slide menu
   if (slideoutMenu.hasClass("open")) {
      slideoutMenu.animate({
          left: "100px"
      });	
   } else {
      slideoutMenu.animate({
          left: -slideoutMenuWidth
      }, 250);	
   }
}

function resetJobMenus(){
   $("#activejobs").removeClass('sbar_title_active');
   $("#feedjobs").removeClass('sbar_title_active');
   $("#vectorjobs").removeClass('sbar_title_active');
   $("#ajobs").hide();
   $("#fjobs").hide();
   $("#vjobs").hide();
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
}

function killJob(jid) {
   $.post("/killjob/", {
      jid:  jid
   });  
}

function newJob(stuff)
{
   
   alert(stuff);
   
   /*
   $.post("/stop/", {
      status:  "no-go"
   });   
   
   $("#stoppwn").hide();
   $("#attack_loader").hide("slow");
   $("#startpwn").show();
   
   */
}


//Get doc elements created by REACT JS after document.ready()
/*
function readyCheck() {
   $('div[id=job_cancel_icon]').click(function(e) {
      //Cancel the link behavior
      e.preventDefault();
      
      console.log('test')
      
      //var r = confirm("Are you sure you want to kill Job: " + $(this).attr('name'));
      //if (r == true) {
         //killJob($(this).attr('name'));
      //   console.log('test')
      //}
   });
}*/

//Document Interval loader
/*
setInterval(function(){
   readyCheck();
}, 5000);
*/

function hideFeeds() {
   $(".feedtitle").hide();
}

function hideFeedForms() {
   $(".feedformbox").hide();
}

function showFeeds() {
   $(".feedtitle").show();
}

function showFeedForm(id) {
   $("#" + id).show();
}

$(document).ready(function () {
   
$("#activejobs").click(function() {
   resetJobMenus()
   $(this).addClass('sbar_title_active');
   $("#ajobs").show();
});
$( "#feedjobs" ).click(function() {
   resetJobMenus()
   $(this).addClass('sbar_title_active');
   $("#fjobs").show();
});
$( "#vectorjobs" ).click(function() {
   resetJobMenus()
   $(this).addClass('sbar_title_active');
   $("#vjobs").show();
});
   
   
   $(document.getElementsByName("feedcont")).hide();
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