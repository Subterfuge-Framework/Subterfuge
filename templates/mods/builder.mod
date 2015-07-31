<script type="text/javascript">
$(document).ready(function() {  
   $('#pluginconfigboxbuilder').hide(); 
});
</script>

<script type="text/javascript">
function showbuilderconfig()
{
   hideconfigs();
   
   $('#pluginconfigboxbuilder').fadeIn(1000).show();
}
</script>

         <!--     PLUGIN ICONS     -->
      <a href = "#builder">
      <div onclick = "showbuilderconfig()" id = "plugin" name = "{{plugin}}">
      <img src = "/static/images/plugins/builder.png"><br>
      Subterfuge Module Builder
      </div>
      </a>
