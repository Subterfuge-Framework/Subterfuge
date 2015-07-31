<div id="credbg">
<table class="credlist">
<tr class = "credbar">
<td>ID</td>
<td>Title</td>
<td>Message</td>
<td>Date</td>
</tr>

{% if alerts %}
    {% for notification in alerts %}
        <tr class = "{% cycle 'credrowa' 'credrowb' %}">
            <td width = "71">{{ notification.id }}</td>
            <td width = "174">{{ notification.title }}</td>
            <td width = "561">{{ notification.message }}</td>
            <td width = "120">{{ notification.date }}</td>
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
</script>

</table>
</div>
