

function redirectToUpdate(pk) {
 window.location.href = "http://localhost:8080/frontend/updateStudent.html?pk="+pk;
}


function deleteStudent(pk){
  alert("Are you sure you want to delete this student?");
 var xhttp = new XMLHttpRequest();
  var myObj;

var jsonObj=JSON.stringify({"id":pk})

xhttp.onreadystatechange = function() {
    console.log(this.readyState);
     console.log(this.status);
    if (this.readyState == 4 && this.status == 200) {
     myObj= JSON.parse(this.responseText);
    alert(myObj);
      location.reload();
    }
  };

   xhttp.open("POST", "http://127.0.0.1:8000/deleteStudent/", true);
 xhttp.send(jsonObj);
}





    


  var xhttp = new XMLHttpRequest();
  var myObj;
 xhttp.onreadystatechange = function() {
  	console.log(this.readyState);
  	 console.log(this.status);
    if (this.readyState == 4 && this.status == 200) {
myObj= JSON.parse(this.responseText);
    console.log('hello');
    putdata_intotable(myObj);
    console.log(myObj);
     }
  };
xhttp.open("GET", "http://127.0.0.1:8000/teacherdashboard/", true);
 xhttp.send();





function putdata_intotable(myObj){
var table_data="";

for(var i = 0; i <myObj.length; i++) {
    table_data+='<tr>';
    table_data+=  '<td>'+myObj[i].id+'</td><td>'
    +myObj[i].roll_no+'</td><td>'
    +myObj[i].first_name+' '+myObj[i].last_name+'</td><td>'+
    myObj[i].username+'</td><td>'
    +myObj[i].section+'</td><td>'
    +myObj[i].branch+'</td><td>'
    +myObj[i].email+'</td><td>'
    +myObj[i].phone_no+'</td>';

    table_data+= '<td><button name="updateBtn" class="updateBtn" type="button" onclick="redirectToUpdate('+myObj[i].id+')">Update</button></td>';

    table_data+= '<td><button name="deleteBtn" class="deleteBtn" type="button" onclick="deleteStudent('+myObj[i].id+')">Delete</button> </td></tr>';
    }
    document.getElementById("tbody").innerHTML = table_data;
}
