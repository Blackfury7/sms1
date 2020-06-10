



console.log("js file is opened");

function addStudent(){
  
  var a;


var xhttp = new XMLHttpRequest();



  xhttp.onreadystatechange = function() {
  	console.log(this.readyState);
  	 console.log(this.status);
    if (this.readyState == 4 && this.status == 200) {

      document.getElementById("demo").innerHTML = this.responseText;
    a = JSON.parse(this.responseText);
    // alert(a);
    // redirect_to_new_page(a);
    console.log(a);
    alert(a);
    if(JSON.parse(a)=="Student added successfully")
    {
      window.location = "http://localhost:8080/frontend/teacher.html";
      
    }
    }
  };


var first_name=document.getElementById("first_name").value;
var last_name=document.querySelector('#last_name').value;
var section=document.getElementById("section").value;
var branch=document.getElementById("branch").value;
var email=document.getElementById("email").value;
var phone_no=document.getElementById("phone_no").value;
// console.log(username.value);
// console.log(password.value);

 	
var myJSON = JSON.stringify({ "roll_no":roll_no,  "first_name": first_name, "last_name":last_name ,
  "section": section,"branch":branch,"email":email, "phone_no":phone_no });


console.log(myJSON);
console.log(typeof(myJSON));



  xhttp.open("POST", "http://127.0.0.1:8000/addStudent/", true);
  xhttp.send(myJSON);


}