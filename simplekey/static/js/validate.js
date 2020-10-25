	$(document).ready(function(){
		var current = 1;

		widget      = $(".step");
		btnnext     = $(".next");
		btnback     = $(".back");
		btnsubmit   = $(".submit");

		// Init buttons and UI
		widget.not(':eq(0)').hide();
		hideButtons(current);
		setProgress(current);

		// Next button click action
		btnnext.click(function(){
			if(current < widget.length){
				// Check validation
				if($(".form").valid()){
					widget.show();
					widget.not(':eq('+(current++)+')').hide();
					setProgress(current);
				}
			}
			hideButtons(current);
		})

		// Back button click action
		btnback.click(function(){
			if(current > 1){
				current = current - 2;
				if(current < widget.length){
					widget.show();
					widget.not(':eq('+(current++)+')').hide();
					setProgress(current);
				}
			}
			hideButtons(current);
		})

	    $('.form').validate({ // initialize plugin
			ignore:":not(:visible)",
			rules: {
				owner     : "required",
				mobileno  : {required:true,minlength:10,maxlength:10,digits:true},
				pname     : "required",
				area      : {required:true,min:1,digits:true},
				price     : {required:true,min:1,digits:true},
				desc      : "required"
			},
			messages: {
                owner     :"First name is required",
                mobileno  :{ required:   "Phone number is requied",
                            minlength:  "Please enter 10 digit mobile number",
                            maxlength:  "Please enter 10 digit mobile number",
                            digits:   "Only numbers are allowed in this field"},
                pname     :"Property Name shouldn't be blank",
                area      :{required:"Please mention size of area",
                            min: "Area should be minimum 1",
                            digits:   "Only numbers are allowed in this field"},
                price     :{required:"Please insert price",
                            min: "Price should be minimum 1",
                            digits:   "Only numbers are allowed in this field"},
                desc      :"Enter the Description"
			},
	    });

	});

	// Change progress bar action
	setProgress = function(currstep){
		var percent = parseFloat(100 / widget.length) * currstep;
		percent = percent.toFixed();
		$(".progress-bar").css("width",percent+"%").html(percent+"%");
	}

	// Hide buttons according to the current step
	hideButtons = function(current){
		var limit = parseInt(widget.length);

		$(".action").hide();

		if(current < limit) btnnext.show();
		if(current > 1) btnback.show();
		if (current == limit) {
			// Show entered values
			$(".display label:not(.control-label)").each(function(){
				console.log($(this).find("label:not(.control-label)").html($("#"+$(this).data("id")).val()));
			});
			btnnext.hide();
			btnsubmit.show();
		}
	}
