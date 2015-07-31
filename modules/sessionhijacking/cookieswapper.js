var cookieblob = 
"COOKIE DATA GOES HERE!!!"

var cookies = cookieblob.split(";");
for (var i = 0; i < cookies.length; i++)
{
   document.cookie=cookies[i].split("=")[0] + "=" + cookies[i].split("=")[1];
}
alert(document.cookie);
