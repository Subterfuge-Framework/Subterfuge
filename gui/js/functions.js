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

$(document).ready(function () {
   
   //Page Setup from variables
   //Get by name & iterate through IDs
   notificationUpdate("notificationbox_b");
   
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