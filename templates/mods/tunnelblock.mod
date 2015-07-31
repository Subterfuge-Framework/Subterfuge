<script type="text/javascript">
$(document).ready(function() {  
   $('#pluginconfigboxtunnelblock').hide(); 
});
</script>

<script type="text/javascript">
function showtunnelblockconfig()
{
   hideconfigs(); 
   $('#pluginconfigboxtunnelblock').fadeIn(1000).show();
}
</script>

         <!--     PLUGIN ICONS     -->
      <a href = "#tunnelblock">
      <div onclick = "showtunnelblockconfig()" id = "plugin" name = "{{plugin}}">
      <img src = "/static/images/plugins/tunnelblock.png"><br>
      Tunnel Block
      </div>
      </a>
