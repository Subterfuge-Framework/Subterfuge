<script>
function notificationshow(title, message)
   {
      document.getElementById('indicator_text').innerHTML = message + '<a href = "http://www.kinozoa.com/blog/troubleshooting/?=\'' + message + '\'" target = "_blank">&nbsp;&nbsp;<img width = "15" src = "/static/images/help.png"></a>';
      $("#indicator_text").show("slide", { direction: "right" });
   }
   //Determine if Notification
function notificationcheck()
{
         //Check for notifications (Check for new. If not new display last.)
         {% if alerts %}
            {% for notification in alerts %}
			            status = "{{ notification.status }}";
						

		                //If Notification Display it
		             if (status == "new")
		             {
		                   notificationshow("{{ notification.title }}", "{{ notification.message }}");
		             }
					 {% if forloop.last %}
				     else
					     {
					        notificationshow("{{ notification.title }}", "{{ notification.message }}");	 
					     }
					{% endif %}
		          {% endfor %}
		       {% endif %}
	}		   
			   
			   

			   

</script>

<style>
	
#modulebox
{
	background:url('/static/images/panel.jpg') repeat-x;
	width: auto;
	min-height: 100px;
	border-radius: 15px;
	margin-top: 10px;
	margin-bottom: 20px;
}
	#moduleboxtext
	{
		color: white;
		padding-top: 10px;
		padding-left: 10px;
		padding-right: 20px;
		padding-bottom: 5px;
		
	}
	#moduleboxtext a
	{
		color: white;
	}
	
	#cookieswapperpopup
	{
		position: absolute;
		top: 50%;
		left: 25%;
		background-color: #d6e0e1;
		font-family:Consolas, monospace;
		min-height: 200px;
		width: auto;
		border-radius: 15px;
		padding: 15px;
	}
	
</style>

<div id = "modulebox">
	<div id = "moduleboxtext">
	   <h3>Credential Harvester<a href = "http://www.kinozoa.com/blog/credential-harvester" target = "_blank">&nbsp;&nbsp;<img width = "15" src = "/static/images/help.png"></a></h3>
	</div>
<div id="credbg">
<table id = "table1" class="credlist">
<tr class = "credbar">
<td>Source</td>
<td>Username</td>
<td>Password</td>
<td>Date</td>
</tr>

{% if credential %}
    {% for cred in credential %}
        <tr class = "{% cycle 'credrowa' 'credrowb' %}">
            <td width = "271">{{ cred.source }}</td>
            <td width = "374">{{ cred.username }}</td>
            <td width = "361">{{ cred.password }}</td>
            <td width = "120">{{ cred.date }}</td>
        </tr>
    {% endfor %}
{% endif %}


<!-- Recheck Arp Poison -->

<script type="text/javascript">
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


</script>

</table>
</div>
</div>


<div id = "modulebox">
	<div id = "moduleboxtext">
	   <h3 style = "float:left;">Session Hijacking <a href = "http://www.kinozoa.com/blog/session-hijacking" target = "_blank">&nbsp;&nbsp;<img width = "15" src = "/static/images/help.png"></a></h3>
	   <a style = "float:right;" href = "#" onclick = "showCookieSwapper()">CookieSwapper</a>
      &nbsp;
	</div>
<div id="credbg">
<table id = "table2" class="credlist">
<tr class = "credbar">
<td>Sessions</td>
<td>Date</td>
</tr>

{% if sessions %}
    {% for session in sessions %}
        <tr class = "{% cycle 'credrowa' 'credrowb' %}">
            <td width = "80%"><a href="#{{ session.session }}" onclick = "sessionhijack('{{ forloop.counter}}')">{{ session.source }}</a></td>
            <td width = "20%">{{ session.date }}</td>
        </tr>
    {% endfor %}
    
<script type="text/javascript">
function sessionhijack(session)
{
	{% for session in sessions %}
	if (session == '{{forloop.counter }}')
	{
		window.prompt ("Copy to clipboard: Ctrl+C, Enter", "{{ session.session }}");
	}
	{% endfor%}
}

function toggleTables(table)
{
var placeholder = "stuff"
	/*
	if (table == "1")
	{
		if ($('#table1').is(':visible')) {
		//Hide it
		$('#table1').hide("slow");
	  }
	  if ($('#table1').is(':hidden')) {
		//Show it
		$('#table1').show("slow");
	  }	
	}
	else if (table == "2")
	{
		if ($('#table2').is(':visible')) {
		//Hide it
		$('#table2').hide("slow");
	  }
	  if ($('#table2').is(':hidden')) {
		//Show it
		$('#table2').show("slow");
	  }	
	}
	*/
}

</script>
	 
{% endif %}



</table>
</div>
</div>
