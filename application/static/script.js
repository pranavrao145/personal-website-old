var active = "home";


function makeactive(id) {
	document.getElementById(active).classList.toggle("active");
	document.getElementById(id).classList.toggle("active");
	active = id;
}

function wait(ms)
{
    var d = new Date();
    var d2 = null;
    do { d2 = new Date(); }
    while(d2-d < ms);
}

function empty() {

}

function typeWrite(text, elemid) {
  for (i = 0; i < text.length; i++) {
    document.getElementById(elemid).innerHTML += text.charAt(i);
    console.log(text.charAt(i));
    wait(50)
    setTimeout(empty, 50) // alternatively, still doesn't work!!
  }
} // why does this not work

function main() {
  typeWrite("Heyy", "init")
}