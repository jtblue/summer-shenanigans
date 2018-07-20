// Change the URL and refresh page when the switch is toggled.
function switch_toggle() {
	console.log("Toggle called")
	if (document.getElementById("button_switch").checked == true) {
		history.pushState(null, null, "/button/on");
	}
	else {
		history.pushState(null, null, "/button/off");
	}
	location.reload();
}

// Listen for a change in the switch status.
var button = document.getElementById("button_switch");
if (button) {
	button.addEventListener("change", switch_toggle);
	console.log("Event listener added.")
}