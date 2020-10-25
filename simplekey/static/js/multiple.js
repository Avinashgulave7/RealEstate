    var buy_progress=1, rent_progress=1, land_progress=1
  var current_page='buy'
  var current = 1,current_step,next_step,buy_steps = 1,rent_steps = 1,land_steps = 1;
$(document).ready(function(){
  buy_steps = $(".buy-form").length;
  rent_steps = $(".rent-form").length;
  land_steps = $(".land-form").length;
  $(".next").click(function(){
    current_step = $(this).parent();
    next_step = $(this).parent().next();
    next_step.show();
    current_step.hide();
    if(current_page=='buy'){
        //setProgressBar(++buy_progress);
        console.log(buy_progress)
        console.log(parseInt(buy_progress))
        setProgressBar(++buy_progress,buy_steps)
    }
    if(current_page=='rent'){
        setProgressBar(++rent_progress,rent_steps);
    }
    if(current_page=='land'){
        setProgressBar(++land_progress,land_steps);
    }
  });
  $("#defaultOpen").click(function(){
    console.log("clickedOnBuy")
    setProgressBar(buy_progress,buy_steps)
    current_page='buy'
  })
  $("#rent-tab").click(function(){
    console.log("clickedOnRent")
    setProgressBar(rent_progress,rent_steps)
    current_page='rent'
  })
  $("#land-tab").click(function(){
    console.log("clickedOnLand")
    setProgressBar(land_progress,land_steps)
    current_page='land'
  })
  $(".previous").click(function(){
    current_step = $(this).parent();
    next_step = $(this).parent().prev();
    next_step.show();
    current_step.hide();
    if(current_page=='buy'){
        //setProgressBar(++buy_progress);
        console.log(buy_progress)
        console.log(parseInt(buy_progress))
        setProgressBar(--buy_progress,buy_steps)
    }
    if(current_page=='rent'){
        setProgressBar(--rent_progress,rent_steps);
    }
    if(current_page=='land'){
        setProgressBar(--land_progress,land_steps);
    }
  });
  setProgressBar(current,buy_steps);
  // Change progress bar action
  function setProgressBar(curStep,steps){
    var percent = parseFloat(100 / steps) * curStep;
    percent = percent.toFixed();
    $(".progress-bar")
      .css("width",percent+"%")
      .html(percent+"%");
  }
});