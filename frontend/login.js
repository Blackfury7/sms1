<!DOCTYPE html>
<html>

	<title>login_page</title>

<body>

	<h1>LOGIN PAGE</h1>

	<form action = "" method="POST">
		username:<input type="text" name="user" ><br><br>
		password:<input type ="text" name="pass"><br>
	
	<!-- <input type="submit" name="login" value="LOGIN"> -->
	<div id="demo">
	
	<button type="button" onclick="loadDoc()">submit</button>
	</div>


	</form>

	<script>
function loadDoc(){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("demo").innerHTML =
      this.responseText;
    }
  };
  xhttp.open("GET", "http://127.0.0.1:8000/", true);
 
  var obj = { username: user.value, password: pass.value };
  var myJSON = JSON.stringify(obj);



  xhttp.send(myJSON);
}
</script>


</body>
</html>