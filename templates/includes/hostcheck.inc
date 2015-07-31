{% load modextras %}
<script type="text/javascript">
      //Host: Check & Append
   var basehostcount = document.getElementById('currenthostcount').innerHTML;

   
function hostcount()
   {   
            //Count number of hosts
        var newhostcount = 0;
         {% if client %}
            {% for host in client %}
              newhostcount++;
            {% endfor %}
        {% endif %}
        
        
        
      if (newhostcount != basehostcount)
      {
            //Number of hosts to append
        var diff = newhostcount - basehostcount;
        
                
            //Set New HostCount
        document.getElementById('currenthostcount').innerHTML = newhostcount;
        
            //Append Hosts & CTRLs
        while (diff >  0)
         {
               //Get Host Info
            var hostaddress = new Array();
            var hostmac = new Array();   
            {% if client %}
               {% for host in client %}
                  hostaddress[{{ forloop.counter }}]   = "{{ host.address }}";
                  hostmac[{{ forloop.counter }}]       = "{{ host.mac }}";
               {% endfor %}
           {% endif %}
            
            
               //Find Host ID
            hostid = parseInt(basehostcount) + parseInt(diff);
            
               //Generate HTML
            var hostHTML = "";
               
               //Small Box
            hostHTML +='   <div id = "netclient" class = "netos' + hostid + '">';
            hostHTML +='      <div id = "netos">';
            hostHTML +='         <div id = "osimgs' + hostid + '">';
            hostHTML +='            <img width = "100" src = "/static/images/netview/unknown.png">';
            hostHTML +='         </div>';
            hostHTML +='      </div>';
            hostHTML +='      <div id = "netoptions">';
            hostHTML +='         <table>';
            hostHTML +='            <tr>';
            hostHTML +='               <td>';
            hostHTML +='                  IP:';
            hostHTML +='               </td>';
            hostHTML +='               <td>';
            hostHTML +='                  ' + hostaddress[hostid];
            hostHTML +='               </td>';
            hostHTML +='            </tr>';
            hostHTML +='            <tr>';
            hostHTML +='               <td>';
            hostHTML +='                  MAC:';
            hostHTML +='               </td>';
            hostHTML +='               <td id = "macs' + hostid + '">';
            hostHTML +='                  ' + hostmac[hostid];
            hostHTML +='               </td>';
            hostHTML +='            </tr>';
            hostHTML +='            <tr>';
            hostHTML +='               <td>';
            hostHTML +='                  ';
            hostHTML +='               </td>';
            hostHTML +='               <td id = "scanindicator' + hostid + '">';
            hostHTML +='               </td>';
            hostHTML +='            </tr>';
            hostHTML +='         </table>';
            hostHTML +='      </div>';
            hostHTML +='         <a href = "javascript: expand(\'' + hostid + '\')"  name = "expand' + hostid + '" class = "expand' + hostid + '"><div id = "redbutton2" style = "color: white;">Expand</div></a>';
            hostHTML +='         <a href = "javascript: scan(\'' + hostaddress[hostid] + '\')" name = "scan' + hostid + '" class = "scan' + hostid + '"><div id = "redbutton2" style = "color: white;">Scan</div></a>';   
            hostHTML +='   </div>';
       
               //Expanded Box
            hostHTML +='   <div id = "expand' + hostid + '">';
            hostHTML +='      <div id = "cont">';
            hostHTML +='         <div id = "expand">';
            hostHTML +='   <div id = "netos">';
            hostHTML +='      <div id = "osimge' + hostid + '">';
            hostHTML +='         <img width = "100" src = "/static/images/netview/unknown.png">';
            hostHTML +='      </div>';
            hostHTML +='   </div>';        
            hostHTML +='   <div id = "netoptions">';
            hostHTML +='         <table>';
            hostHTML +='            <tr>';
            hostHTML +='               <td>';
            hostHTML +='                  IP:';
            hostHTML +='               </td>';
            hostHTML +='               <td>';
            hostHTML +='                  ' + hostaddress[hostid];
            hostHTML +='               </td>';
            hostHTML +='            </tr>';
            hostHTML +='            <tr>';
            hostHTML +='               <td>';
            hostHTML +='                  MAC:';
            hostHTML +='               </td>';
            hostHTML +='               <td id = "mace' + hostid + '">';
            hostHTML +='                  ' + hostmac[hostid];
            hostHTML +='               </td>';
            hostHTML +='            </tr>';
            hostHTML +='            <tr>';
            hostHTML +='               <td>';
            hostHTML +='                  ';
            hostHTML +='               </td>';
            hostHTML +='               <td id = "scanindicator' + hostid + '">';
            hostHTML +='               </td>';
            hostHTML +='            </tr>';
            hostHTML +='         </table>';
            hostHTML +='   </div>';
            hostHTML +='      <a href = "javascript: shrink(\'' + hostid + '\')"  name = "shrink' + hostid + '" class = "shrink' + hostid + '"><div id = "redbutton2" style = "color: white;">Shrink</div></a>';
            hostHTML +='      <a href = "javascript: scan(\'' + hostaddress[hostid] + '\')" name = "scan' + hostaddress[hostid] +'" class = "scan' + hostaddress[hostid] +'"><div id = "redbutton2" style = "color: white;">Scan</div></a>';      
            hostHTML +='   <div id = "expandbox">';
            hostHTML +='      <div id = "netoptions">';
            hostHTML +='         Open Ports:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;';
            hostHTML +='      </div>';
            hostHTML +='         <div id = "ports' + hostid + '">';
            hostHTML +='         </div>';
            hostHTML +='   </div>';
            hostHTML +='   <div id = "expandbox">';
            hostHTML +='      <div id = "netoptions" class="modpanel' + hostid + '">';
            hostHTML +='         Controls:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;';
            hostHTML +='      </div>';
            hostHTML +='      <div id = "netoptions" class="modpanel{{ forloop.counter }}">';
            hostHTML +='       <a href="javascript: injectionctrl(' + hostid + ')" "><img height="65" width="65" src="/static/images/plugins/httpcodeinjection.png"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;';
            hostHTML +='      </div>';            
            hostHTML +='      <div id = "netoptions" class="modpanel{{ forloop.counter }}">';
            hostHTML +='       <a href="javascript: injectionctrl(' + hostid + ')" "><img height="65" width="65" src="/static/images/plugins/tunnelblock.png"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;';
            hostHTML +='      </div>';    
            hostHTML +='      <div id = "netoptions" class="modpanel{{ forloop.counter }}">';
            hostHTML +='       <a href="javascript: injectionctrl(' + hostid + ')" "><img height="65" width="65" src="/static/images/plugins/dos.png"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;';
            hostHTML +='      </div>';             
               //Closing divs
            hostHTML +='   </div>';
            hostHTML +='         </div>';
            hostHTML +='      </div>';
            hostHTML +='   </div>';
       

               //Append new host
            document.getElementById('netviewmaincont').innerHTML += hostHTML;
                      
               //Hide Expanded box onLoad
	    $("#expand" + hostid).hide();

       
            diff--;
         }
      }
   }

function update()
   {

         //Get Host Details
      {% if client %}
         {% for host in client %}
            
               //Update Host Data
            osimg = '<img width = "100" src = "/static/images/netview/{{ host.os }}.png">';
            mac = '{{ host.mac }}';
            document.getElementById('osimgs{{ forloop.counter }}').innerHTML = osimg;
            document.getElementById('osimge{{ forloop.counter }}').innerHTML = osimg;
            document.getElementById('macs{{ forloop.counter }}').innerHTML = mac;
            document.getElementById('mace{{ forloop.counter }}').innerHTML = mac;
            
            
               //Get Scan Results
            {% for result in scan %}
               var ports{{ forloop.counter }} = new Array();
                  {% for port in result.ports|joinby %}
                      ports{{ forloop.parentloop.counter }}[{{ forloop.counter }}] = "{{ port }}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
                  {% endfor %}
                  {% if result.address == host.address %}
                     {% if result.scanning == "1" %}
                        scanindicator = '<img src = "/static/images/activity.gif">'
                     {% else %}
                        scanindicator = ''
                     {% endif %}
                  {% endif %}
             {% endfor %}

               //Update Scan Results
            document.getElementById('scanindicator{{ forloop.counter }}').innerHTML = scanindicator;
            document.getElementById('ports{{ forloop.counter }}').innerHTML = "";             
            for (var i = 0; i < ports{{ forloop.counter }}.length; i++)
            {
               if (ports{{ forloop.counter }}[i] != undefined)
               {
                  document.getElementById('ports{{ forloop.counter }}').innerHTML += ports{{ forloop.counter }}[i];
               }
            }

         {% endfor %}
      {% endif %}
   }
   
   //Determine if Notification
function notificationcheck()
   {
         //Check for new Notification
      {% if alerts %}
         {% for notification in alerts %}
            status = "{{ notification.status }}";

               //If Notification Display it
            if (status == "new")
            {
                  notificationshow("{{ notification.title }}", "{{ notification.message }}");
                  setTimeout(notificationhide, 5000);
            }
         {% endfor %}
      {% endif %}
   }
function notificationshow(title, message)
   {
      document.getElementById('notificationboxtitle').innerHTML = title;
      document.getElementById('notificationboxmessage').innerHTML = message;
      $("#notificationbox").show("slide", { direction: "right" });
   }
function notificationhide()
   {
      $("#notificationbox").hide("slide", { direction: "right" });
   }

function loading()
   {
      $(".window").show("slow")
      $(".window").delay(3000).hide("slow");
   }    

function expand(hostid)
   {
      $("#expand" + hostid).delay(1000).show("slow");
      $(".netos" + hostid).hide("slow");
   }
   
function shrink(hostid)
   {
      $("#expand" + hostid).hide("slow");
      $(".netos" + hostid).delay(1000).show("slow");
   }
   
function scan(hostaddress)
   {
          //Start Scan
      $.post("/netctrl/scan/", { target:  hostaddress } );
      loading();          
   }
   
function injectionctrl(target)
   {
          //Display Injection CTRL
      $("#injectionctrl").show("slow");
      
          //Set Target div
      
   }   
function httpcodeinjection()
   {
          //Start Injection
      $(".window").show("slow")
      $(".window").delay(3000).hide("slow");
      
      $.post("/config/httpinjection/", {
            status:           document.getElementById('status').value,
            vector:           document.getElementById('vector').value,
            payload:          document.getElementById('payload').value,
            custominject:     document.getElementById('custominject').value
      });   
   }
   
   
      //Recheck Arp Poison
{% if status == "on" %}
	$(document).ready(function () {
	  $("#startpwn").hide("slow")
	});
	$(document).ready(function () {
	  $("#onbar").show("slow");
	});
	$(document).ready(function () {
	  $("#stoppwn").show("slow");
	});
{% else %}
	$(document).ready(function () {
	  $("#startpwn").show("slow");
	});
	$(document).ready(function () {
	  $("#onbar").hide("slow")
	});
	$(document).ready(function () {
	  $("#stoppwn").hide("slow");
	});

{% endif %}

   notificationcheck();
   hostcount();
   update();
   


</script>
   
