//wait until page has loaded to do something

var showHide = function(div_id){
	document.getElementById(div_id).style.display = "block";
	if (div_id == "div22") {
		document.getElementById("div33").style.display = "none";
		}
	else {
		document.getElementById("div22").style.display = "none";
		}
	
	};


