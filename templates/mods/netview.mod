<script type="text/javascript">
$(document).ready(function() {  
$('#pluginconfigboxnetview').hide();
});
</script>

<script type="text/javascript">
function shownetviewconfig()
{
   hideconfigs();
   
$('#pluginconfigboxnetview').fadeIn(1000).show();
}
</script>

         <!--     PLUGIN ICONS     -->
<a href = '#netview'>
<div onclick = 'shownetviewconfig()' id = 'plugin' name = '{{plugin}}'>
<img src = '/static/images/plugins/netview.png'><br>
Network View      </div>
      </a>
