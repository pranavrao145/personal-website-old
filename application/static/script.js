var active = "home";


function makeactive(id) {
	document.getElementById(active).classList.toggle("active");
	document.getElementById(id).classList.toggle("active");
	active = id;
}