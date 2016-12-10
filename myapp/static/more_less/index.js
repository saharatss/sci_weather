// Grabbing button & content id and assigning to a varaible.

var button=document.getElementById("showMore");
var content=document.getElementById("content");
//Connecting button variable to on click function
button.onclick = function(){
  // If content class name is equal to open
  if(content.className=="open"){
    //removes class name
    content.className="";
    // once removed button shows show more
    button.innerHTML="SHOW MORE"
     }else{
       //other wise if its closed  button will show show less
       content.className="open";
       button.innerHTML="SHOW LESS"
     }
};