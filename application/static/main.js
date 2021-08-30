var i = 0;
var txt = "Hi, I'm Pranav Rao!"; /* The text */
var speed = 50; /* The speed/duration of the effect in milliseconds */

function typeWriter() {
  if (i < txt.length) {
    document.getElementById("typewriter").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}

var i1 = 0;
var txt1 = 'I love programming, especially using it to make '; /* The text */


function typeWriter1() {
  if (i1 < txt1.length) {
    document.getElementById("typewriter1").innerHTML += txt1.charAt(i1);
    i1++;
    setTimeout(typeWriter1, speed);
  }
}

function addBoldText() {
  $("#typewriter1").after("<strong class='subtitle is-3 has-text-weight-bold' id='typewriter15'></strong>");
}

var i15 = 0;
var txt15 = 'difficult things easier.'; /* The text */

function typeWriter15() {
  if (i15 < txt15.length) {
    document.getElementById("typewriter15").innerHTML += txt15.charAt(i15);
    i15++;
    setTimeout(typeWriter15, speed);
  }
}

function onload() {
  typeWriter();
  speed = 70;
  setTimeout(typeWriter1, 2500);
  setTimeout(addBoldText);
  setTimeout(typeWriter15, 6200);
  setTimeout(function () {
    $('#scroll-prompt').fadeIn(1500);
  }, 8000);
}
