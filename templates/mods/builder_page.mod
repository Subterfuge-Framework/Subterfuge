<style>
 .modpageicon
 {      
      float: left;
      height: 150px;
      width: 150px;
 }
 #modpageicons
 {      
      float: left;
      height: 150px;
      width: 150px;
 }
 .modmainsettings
 {
     float: left;
     border: 2px black solid;
     padding: 15px 10px;
     margin: auto;
     height: 150px;
     width: 80%;
 }
 .modbuilder
 {
     float: left;
     border: 2px black solid;
     padding: 15px 10px;
     margin-top: 10px;
     margin: auto;
     height: 345px;
     width: 96%;
 }
 #modframe
 {
     float: left;
     width: auto;
     width: 100%;
     margin: 10px;
 }
</style>


<div id = "pluginbox">
<div id = "plugintitle">{{module_name}}</div>
<div id = "modframe">

   <div class = "modpageicon" id = "demo">
      <img class = "modpageicon" src = "/static/images/plugins/{{module_name}}.png">
   </div>

<form enctype = "multipart/form-data" name = "builderform" method = "post" action = "/create/" >
   <fieldset class = "modmainsettings"><legend>&nbsp;Main Settings&nbsp;</legend>
   
      <center>
      <table>
      <tr>
      <td>Module Name:</td>
      <td>
      <input type = "text" name = "modname">
      </td>  
      <td>Module Icon:</td>
      <td>
      <input type = "file" name = "modicon">
      </td>   
      </tr>
      <tr>
      <td>Python Code:</td>
      <td>
      <input title = "This code should be the part of your module that actually does stuff." type = "file" name = "exploitcode">
      </td>    
      <td>Module Description:</td>
      <td>
      <input type = "text" name = "description">
      </td>    
      </tr>
      </table>
      </center>
   
   </fieldset>
   
   
   
   <fieldset class = "modbuilder"><legend>&nbsp;Building Your Module&nbsp;</legend>
   
      <p>
      The Subterfuge Module Builder allows you to integrate your own attack code into the framework.<br>
      Subterfuge Modules consist of the following:
      <pre>
      
      Python Code       -> This is the meat of the module providing the additional feature for the framework.
      GUI Integration   -> This piece of the code dictates how your module is displayed by Subterfuge.
      
      </pre>
      Subterfuge comes packaged with other utilities and modules that you can use to automatically make the scripting of your attack dynamic. Click below for more information:
      <p>
      
      <table>
      <tr>
      <td>
      How To Use Subterfuge's:
      </td>
      <td>
      <a href = "#"><div id = "redbutton" style = "color: white;">Database</div></a> 
      </td>
      <td>
      <a href = "#"><div id = "redbutton" style = "color: white;">GUI Framework</div></a> 
      </td>
      <td>
      <a href = "#"><div id = "redbutton" style = "color: white;">Functions</div></a> 
      </td>
      <tr>
      </table>
      
      
      <a href = "javascript: create()" name = "apply"><div id = "redbutton" style = "margin: 30px; color: white;">Create</div></a>

      <script type = "text/javascript">
      function create()
      {
        document.builderform.submit();
      }
       </script>
       
       
   
   </fieldset>
   
</form> 

</div>
</div>
