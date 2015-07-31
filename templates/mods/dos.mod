<script type="text/javascript">
$(document).ready(function() {  
$('#pluginconfigboxdos').hide();
});
</script>

<script type="text/javascript">
function showdosconfig()
{
   hideconfigs();
   
$('#pluginconfigboxdos').fadeIn(1000).show();
}
</script>

         <!--     PLUGIN ICONS     -->
<a href = '#dos'>
<div onclick = 'showdosconfig()' id = 'plugin' name = '{{plugin}}'>
<img src = '/static/images/plugins/dos.png'><br>
Denial of Service      </div>
      </a>
