$(function(){
	var hour =$( "#hours" ).html();
	var min = $("#min").html()
	$("#hm_timer").countdowntimer({
		minutes : min,
		seconds : 00,
		size: "lg",
		timeUp : Up
	});

	function Up(){
	  $("#exampleModalLabel").prepend("Sorry Time Up:  ");
	  $("#exampleModal").modal({ backdrop: 'static',
    						     keyboard: false
    						   });

	}

	$("#add-comment-link").click(function(){
	    $("#comment-form").show();
	});


//SCROL To TOP
	//Check to see if the window is top if not then display button
	$(window).scroll(function(){
		if ($(this).scrollTop() > 100) {
			$('.scrollToTop').fadeIn();
		} else {
			$('.scrollToTop').fadeOut();
		}
	});

	//Click event to scroll to top
	$('.scrollToTop').click(function(){
		$('html, body').animate({scrollTop : 0},800);
		return false;
	});


	$('#btnfull').click(function(){
		if($('input:radio:checked').length == 0){
				alert("Please select answers");
				return false;
		 }
	});

});//dOCUMENT rEADY

