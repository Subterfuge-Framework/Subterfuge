<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> 
<html xmlns="http://www.w3.org/1999/xhtml"> 
<head> 
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />  
<title>Subterfuge</title> 
<meta http-equiv="Content-Language" content="en" /> 
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

<!--	Tab icon	-->
<link rel="shortcut icon" href="/static/images/logo.png" />


<!--	Style Sheets	-->
<link rel="stylesheet" type="text/css" href="/static/css/main.css" />
<link rel="stylesheet" type="text/css" href="/static/css/settings.css" />
<link rel="stylesheet" type="text/css" href="/static/css/domtab.css" />
<link rel="stylesheet" type="text/css" href="/static/css/jquery-ui.css" />
 
<!--	jQuery	-->
<script type="text/javascript" src="/static/js/jquery.js"></script><!-- jQuery -->
<script type="text/javascript" src="/static/js/jquery-ui.js"></script><!-- jQuery-UI -->
<script type="text/javascript" src="/static/js/domtab.js"></script><!-- Configuration Menu-->


<!-- Initiating -->
<script type="text/javascript">
function initiating()
{
      $(".window").show("slow")
      $(".window").delay(3000).hide("slow");
}
</script>

<script type="text/javascript">
	//Auto Refresh Loads
var pLoadRate = {% for settings in setup %}{{ settings.ploadrate }}{% endfor %} + "000";
var auto_refresh = setInterval(
function ()
{
$('#creds').load('/').fadeIn("slow");
$('#notifications').load('/notifications/').fadeIn("slow");
$('#hostcheck').load('/hostcheck/').fadeIn("slow");

}, pLoadRate);
</script>

<script type="text/javascript">
$(document).ready(function() {
  $('#creds').load('/').fadeIn("slow");
});
</script>

<script type="text/javascript">
	//NetView Reload
$(document).ready(function() {
  $('#netviewmaincont').load('/netview/').fadeIn("slow");
});
</script>

<script type="text/javascript">
	$(document).ready(function () {
	  $("#onbar").hide();
	});

	$(document).ready(function () {
	  $("#stoppwn").hide();
	});
	
	$(document).ready(function () {
	  $("#notificationbox").hide();
	});

	$(document).ready(function () {
	  $(".window").hide();
	});
</script>

<script type="text/javascript">
$(document).ready(function () {
  $(".manualgate").hide();
  
        //select all the a tags named startpwn
    $('a[name=manualgate]').click(function(e) {
            //Cancel the link behavior
        e.preventDefault();
            //Get the A tag
        var id = $(this).attr('href');
        
            //Start Pwning
        $(".manualgate").fadeIn("slow");
        $(".autogate").fadeOut("slow");

    }); 
  
});
</script>




<script type="text/javascript">
$(document).ready(function() {  
        //select all the a tags named startpwn
    $('a[name=startpwn]').click(function(e) {
    
    {% if setup %}
      {% for settings in setup %}
	var auto = "{{ settings.autoconf }}"
      {% endfor %}
    {% endif %}

          //Auto Configure and Run
    if (auto == "yes")
    {
      var check = confirm ("Subterfuge will attempt to autoconfigure your network settings. You can turn off auto configuration in the settings tab.");
      if (check)
      {
               //Cancel the link behavior
           e.preventDefault();
               //Get the A tag
           var id = $(this).attr('href');
        
               //Get the screen height and width
           var maskHeight = $(document).height();
           var maskWidth = $(window).width();
        
               //Set height and width to mask to fill up the whole screen
           $('#mask').css({'width':maskWidth,'height':maskHeight});
            
               //transition effect     
           $('#mask').fadeIn(1000).hide();
           $('#mask').fadeTo("slow",0.8);
           $('#mask').delay(8000).hide("slow");
           
        
               //Get the window height and width
           var winH = $(window).height();
           var winW = $(window).width();
                  
               //Set the popup window to center
           $(id).css('top',  winH/2-$(id).height()/2);
           $(id).css('left', winW/2-$(id).width()/2);
        
               //transition effect
           $(id).fadeIn(2000);
           $('.window').delay(8000).hide("slow");

           
               //Start Pwning
           $('#startpwn').load('/startpwn/auto/');
                 
      }
     
    }
    else
    {
               //Cancel the link behavior
           e.preventDefault();
               //Get the A tag
           var id = $(this).attr('href');
        
               //Get the screen height and width
           var maskHeight = $(document).height();
           var maskWidth = $(window).width();
        
               //Set height and width to mask to fill up the whole screen
           $('#mask').css({'width':maskWidth,'height':maskHeight});
            
               //transition effect     
           $('#mask').fadeIn(1000).hide();
           $('#mask').fadeTo("slow",0.8);
           $('#mask').delay(2000).hide("slow");
           
        
               //Get the window height and width
           var winH = $(window).height();
           var winW = $(window).width();
                  
               //Set the popup window to center
           $(id).css('top',  winH/2-$(id).height()/2);
           $(id).css('left', winW/2-$(id).width()/2);
        
               //transition effect
           $(id).fadeIn(2000);
           $('.window').delay(2000).hide("slow");

           
               //Start Pwning
           $('#startpwn').load('/startpwn/regular');
    }
   });
           
               //if close button is clicked
          $('.window .close').click(function (e) {
              //Cancel the link behavior
              e.preventDefault();
              $('#mask, .window').hide();
          });     
           
               //if mask is clicked
          $('#mask').fadeIn(function () {
              $(this).hide();
              $('.window').hide();
          });  
      
 });

$(document).ready(function() {  
 
        //select all the a tags named stoppwn
    $('a[name=stoppwn]').click(function(e) {
            //Cancel the link behavior
        e.preventDefault();
            //Get the A tag
        var id = $(this).attr('href');
        
        $("#onbar").delay(1000).hide("slow")
        $("#stoppwn").delay(1000).hide("slow");
        $("#startpwn").delay(2000).show("slow");
        
            //Stop Pwning
        $('#stoppwn').load('/stoppwn/');
    });         
     
});

$(document).ready(function() {  
 
        //select all the a tags named reset
    $('a[name=reset]').click(function(e) {
            //Cancel the link behavior
        e.preventDefault();
            //Get the A tag         
        var id = $(this).attr('href');
     
            //Get the screen height and width
        var maskHeight = $(document).height();
        var maskWidth = $(window).width();
     
     
            //Get the window height and width
        var winH = $(window).height();
        var winW = $(window).width();
               
            //Set the popup window to center
        $(id).css('top',  winH/2-$(id).height()/2);
        $(id).css('left', winW/2-$(id).width()/2);     
        $(id).fadeIn(4000);
        
            //Start Pwning
        $('#intab').load('/resetpwn/');
        
    
        $(".window").show("slow")
        $(".window").delay(3000).hide("slow");
    });
     
});
 
</script>



</head>
