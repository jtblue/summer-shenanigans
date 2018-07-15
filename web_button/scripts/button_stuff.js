window.onload = function() {
	// setup the button click
	document.getElementById("theButton").onclick = function() {
		doWork()
	};
}

function doWork() {
	// ajax the JSON to the server
	$.post("receiver", cars, function(){

	});
	// stop link reloading the page
 event.preventDefault();
}