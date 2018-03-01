function bookInfo(id) {
	var x = document.getElementById("content-".concat("", id));
	var y = document.getElementById("title-".concat("", id));
	if (x.className.indexOf("w3-hide") != -1) {
		x.className = x.className.replace("w3-hide", "");
		y.style.fontWeight = "bold"
		y.style.fontSize = "large"
	} else {
		x.className += "w3-hide";
		y.style.fontWeight = "normal"
		y.style.fontSize = "medium"
	}
}

function orderForm(id) {
	var x = document.getElementById("form-".concat("", id));
	x.style.display = 'block'
}

function closeForm(id) {
	var x = document.getElementById("form-".concat("", id));
	x.style.display = 'none'
}

function navStick() {
	if (window.pageYOffset >= sticky) {
		navbar.classList.add("sticky")
	} else {
		navbar.classList.remove("sticky");
	}
} 

$(function() {
	$("#SCROLL").on("click", function(e) {
		e.preventDefault();
		$("html, body").animate(
			{ scrollTop: $($(this).attr("href")).offset().top },
			500,
			"linear"
		);
	});
});
