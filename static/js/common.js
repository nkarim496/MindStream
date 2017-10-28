$(function() {

	//SVG Fallback
	if(!Modernizr.svg) {
		$("img[src*='svg']").attr("src", function() {
			return $(this).attr("src").replace(".svg", ".png");
		});
	};

	// File button attachments
	$("#id_mind_img").on('change', function (e) {
		var fileName = '';
		if(e.target.value)
			fileName = e.target.value.split("\\").pop();
		if(fileName) {
            $("#file-input-label").html('<i class="fa fa-check" aria-hidden="true"></i>');
            $("#filetext").text(fileName).show("slow");
        }
		else {
			$("#file-input-label").html('<i class="fa fa-picture-o" aria-hidden="true"></i>');
			$("#filetext").hide("slow");
		}
    });

	//Chrome Smooth Scroll
	try {
		$.browserSelector();
		if($("html").hasClass("chrome")) {
			$.smoothScroll();
		}
	} catch(err) {

	};

	$("img, a").on("dragstart", function(event) { event.preventDefault(); });
	
});

$(window).load(function() {

	$(".loader_inner").fadeOut();
	$(".loader").delay(400).fadeOut("slow");

});
