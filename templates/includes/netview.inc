{% load modextras %}


<!--

<div id = "nettitle">HTTP CodeInjection:&nbsp;&nbsp;</div>
<div id = "nettitle"><img width = "25" src = "/static/images/netview/red.png"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div>
<div id = "nettitle">Tunnel Block:&nbsp;&nbsp;</div>
<div id = "nettitle"><img width = "25" src = "/static/images/netview/green.png"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div>
<div id = "nettitle">EvilGrade:&nbsp;&nbsp;</div>
<div id = "nettitle"><img width = "25" src = "/static/images/netview/red.png"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div>

-->

{% if client %}
    {% for host in client %}
    
   <div id = "netclient" class = "netos{{ forloop.counter }}">
      <div id = "netos">
         <div id = "osimgs{{ forloop.counter }}">
            <img width = "100" src = "/static/images/netview/{{ host.os }}.png">
         </div>
      </div>
      <div id = "netoptions">
         <table>
            <tr>
               <td>
                  IP:
               </td>
               <td>
                  {{ host.address }}
               </td>
            </tr>
            <tr>
               <td>
                  MAC:
               </td>
               <td id = "macs{{ forloop.counter }}">
                  {{ host.mac }}
               </td>
            </tr>
            <tr>
               <td>
                
               </td>
               <td id = "scanindicator{{ forloop.counter }}">
                  {% for result in scan %}
                     {% if result.address == host.address %}
                        {% if result.scanning == "1" %}
                           <img src = "/static/images/activity.gif">
                        {% endif %}
                     {% endif %}
                  {% endfor %}
               </td>
            </tr>
         </table>         
      </div>
         <a href = "javascript: expand('{{ forloop.counter }}')"  name = "expand{{ forloop.counter }}" class = "expand{{ forloop.counter }}"><div id = "redbutton2" style = "color: white;">Expand</div></a> 
         <a href = "javascript: scan('{{ host.address }}')" name = "scan{{ host.address }}" class = "scan{{ host.address }}"><div id = "redbutton2" style = "color: white;">Scan</div></a>      
   </div>
   
   
   
   <div id = "expand{{ forloop.counter }}">
      <div id = "cont">
         <div id = "expand">
         
   <div id = "netos">
      <div id = "osimge{{ forloop.counter }}">
         <img width = "100" src = "/static/images/netview/{{ host.os }}.png">
      </div>
   </div>
   <div id = "netoptions">
      <table>
         <tr>
            <td>
               IP:
            </td>
            <td>
               {{ host.address }}
            </td>
         </tr>
         <tr>
            <td>
               MAC:
            </td>
            <td id = "mace{{ forloop.counter }}">
               {{ host.mac }}
            </td>
         </tr>
         <tr>
            <td>
               
            </td>
            <td id = "scanindicator{{ forloop.counter }}">
               {% for result in scan %}
                  {% if result.address == host.address %}
                     {% if result.scanning == "1" %}
                        <img src = "/static/images/activity.gif">
                     {% endif %}
                  {% endif %}
               {% endfor %}
            </td>
         </tr>
      </table>         
   </div>
      <a href = "javascript: shrink('{{ forloop.counter }}')"  name = "shrink{{ forloop.counter }}" class = "shrink{{ forloop.counter }}"><div id = "redbutton2" style = "color: white;">Shrink</div></a>
      
      
      <script type="text/javascript">
			$(document).ready(function() {  
				 $("#expand{{ forloop.counter }}").hide();        
			});  
      </script>
      
      <a href = "javascript: scan('{{ host.address }}')" name = "scan{{ host.address }}" class = "scan{{ host.address }}"><div id = "redbutton2" style = "color: white;">Scan</div></a>    
      
   <div id = "expandbox">
      <div id = "netoptions">
         Open Ports:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      </div>
      
    {% for result in scan %}
      {% if result.address == host.address %}
         <div id = "ports{{ forloop.parentloop.counter }}">
         {% for port in result.ports|joinby %}         
                  {{ port }}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
         {% endfor %}
         </div>         
      {% endif %}
    {% endfor %}
   </div>
   
   
   <div id = "expandbox">
      <div id = "netoptions" class="modpanel{{ forloop.counter }}">
         Controls:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      </div>
      
    {% for module in modules %}
      <script type="text/javascript">
      $(document).ready(function() {  
         
                 //On Click
          $('a[name="ctrlpanel{{ forloop.counter }}c{{ forloop.parentloop.counter }}"]').click(function(e) {
                  //Cancel the link behavior
              e.preventDefault();
                  //Get the A tag
              var id = $(this).attr('href');
         
                  //Expanded View
               {% for host in client %}
                  {% for module in modules %}
                     $(".ctrlpanel{{ forloop.counter }}c{{ forloop.parentloop.counter }}").hide("slow");
                  {% endfor %}
               {% endfor %}
               $(".ctrlpanel{{ forloop.counter }}c{{ forloop.parentloop.counter }}").delay(1000).show("slow");
      
          });
      });  
      </script>
      
      <div id = "netoptions" class="modpanel{{ forloop.counter }}">
       <a href="javascript: injectionctrl('{{ host.address }}')" "><img height="65" width="65" src="/static/images/plugins/{{ module.name }}.png"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      </div>
      

     
      
    {% endfor %}
   </div>


    
         </div>
      </div>
   </div>
   
   



    {% endfor %}
{% endif %}







