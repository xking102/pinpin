/* -------------------- Check Browser --------------------- */

function browser() {

	var isOpera = !!(window.opera && window.opera.version);  // Opera 8.0+
	var isFirefox = testCSS('MozBoxSizing');                 // FF 0.8+
	var isSafari = Object.prototype.toString.call(window.HTMLElement).indexOf('Constructor') > 0;
	    // At least Safari 3+: "[object HTMLElementConstructor]"
	var isChrome = !isSafari && testCSS('WebkitTransform');  // Chrome 1+
	//var isIE = /*@cc_on!@*/false || testCSS('msTransform');  // At least IE6

	function testCSS(prop) {
	    return prop in document.documentElement.style;
	}

	if (isOpera) {

		return false;

	}else if (isSafari || isChrome) {

		return true;

	} else {

		return false;

	}

}


$(document).ready(function(){


	$("#username").focus(function() {

		$(this).parent(".input-prepend").addClass("input-prepend-focus");

	});

	$("#username").focusout(function() {

		$(this).parent(".input-prepend").removeClass("input-prepend-focus");

	});

	$("#email").focus(function() {

		$(this).parent(".input-prepend").addClass("input-prepend-focus");

	});

	$("#email").focusout(function() {

		$(this).parent(".input-prepend").removeClass("input-prepend-focus");

	});

	$("#password").focus(function() {

		$(this).parent(".input-prepend").addClass("input-prepend-focus");

	});

	$("#password").focusout(function() {

		$(this).parent(".input-prepend").removeClass("input-prepend-focus");

	});


	/* ---------- Add class .active to current link  ---------- */
	$('ul.main-menu li a').each(function(){

			if($($(this))[0].href==String(window.location)) {

				$(this).parent().addClass('active');

			}

	});

	$('ul.main-menu li ul li a').each(function(){

			if($($(this))[0].href==String(window.location)) {

				$(this).parent().addClass('active');
				$(this).parent().parent().show();

			}

	});

	/* ---------- Submenu  ---------- */

	$('.dropmenu').click(function(e){

		e.preventDefault();

		$(this).parent().find('ul').slideToggle();

	});

	/* ---------- Acivate Functions ---------- */
	growlLikeNotifications();
	widthFunctions();

	if(jQuery.browser.version.substring(0, 2) == "8.") {

		//disable jQuery Knob

	} else {



	}



});









function growlLikeNotifications() {

	$('#add-sticky').click(function(){

		var unique_id = $.gritter.add({
			// (string | mandatory) the heading of the notification
			title: 'This is a sticky notice!',
			// (string | mandatory) the text inside the notification
			text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eget tincidunt velit. Cum sociis natoque penatibus et <a href="#" style="color:#ccc">magnis dis parturient</a> montes, nascetur ridiculus mus.',
			// (string | optional) the image to display on the left
			image: 'img/avatar.jpg',
			// (bool | optional) if you want it to fade out on its own or just sit there
			sticky: true,
			// (int | optional) the time you want it to be alive for before fading out
			time: '',
			// (string | optional) the class name you want to apply to that specific message
			class_name: 'my-sticky-class'
		});

		// You can have it return a unique id, this can be used to manually remove it later using
		/* ----------
		setTimeout(function(){

			$.gritter.remove(unique_id, {
				fade: true,
				speed: 'slow'
			});

		}, 6000)
		*/

		return false;

	});

	$('#add-regular').click(function(){

		$.gritter.add({
			// (string | mandatory) the heading of the notification
			title: 'This is a regular notice!',
			// (string | mandatory) the text inside the notification
			text: 'This will fade out after a certain amount of time. Vivamus eget tincidunt velit. Cum sociis natoque penatibus et <a href="#" style="color:#ccc">magnis dis parturient</a> montes, nascetur ridiculus mus.',
			// (string | optional) the image to display on the left
			image: 'img/avatar.jpg',
			// (bool | optional) if you want it to fade out on its own or just sit there
			sticky: false,
			// (int | optional) the time you want it to be alive for before fading out
			time: ''
		});

		return false;

	});

    $('#add-max').click(function(){

        $.gritter.add({
            // (string | mandatory) the heading of the notification
            title: 'This is a notice with a max of 3 on screen at one time!',
            // (string | mandatory) the text inside the notification
            text: 'This will fade out after a certain amount of time. Vivamus eget tincidunt velit. Cum sociis natoque penatibus et <a href="#" style="color:#ccc">magnis dis parturient</a> montes, nascetur ridiculus mus.',
            // (string | optional) the image to display on the left
            image: 'img/avatar.jpg',
            // (bool | optional) if you want it to fade out on its own or just sit there
            sticky: false,
            // (function) before the gritter notice is opened
            before_open: function(){
                if($('.gritter-item-wrapper').length == 3)
                {
                    // Returning false prevents a new gritter from opening
                    return false;
                }
            }
        });

        return false;

    });

	$('#add-without-image').click(function(){

		$.gritter.add({
			// (string | mandatory) the heading of the notification
			title: 'This is a notice without an image!',
			// (string | mandatory) the text inside the notification
			text: 'This will fade out after a certain amount of time. Vivamus eget tincidunt velit. Cum sociis natoque penatibus et <a href="#" style="color:#ccc">magnis dis parturient</a> montes, nascetur ridiculus mus.'
		});

		return false;
	});

    $('#add-gritter-light').click(function(){

        $.gritter.add({
            // (string | mandatory) the heading of the notification
            title: 'This is a light notification',
            // (string | mandatory) the text inside the notification
            text: 'Just add a "gritter-light" class_name to your $.gritter.add or globally to $.gritter.options.class_name',
            class_name: 'gritter-light'
        });

        return false;
    });

	$('#add-with-callbacks').click(function(){

		$.gritter.add({
			// (string | mandatory) the heading of the notification
			title: 'This is a notice with callbacks!',
			// (string | mandatory) the text inside the notification
			text: 'The callback is...',
			// (function | optional) function called before it opens
			before_open: function(){
				alert('I am called before it opens');
			},
			// (function | optional) function called after it opens
			after_open: function(e){
				alert("I am called after it opens: \nI am passed the jQuery object for the created Gritter element...\n" + e);
			},
			// (function | optional) function called before it closes
			before_close: function(e, manual_close){
                var manually = (manual_close) ? 'The "X" was clicked to close me!' : '';
				alert("I am called before it closes: I am passed the jQuery object for the Gritter element... \n" + manually);
			},
			// (function | optional) function called after it closes
			after_close: function(e, manual_close){
                var manually = (manual_close) ? 'The "X" was clicked to close me!' : '';
				alert('I am called after it closes. ' + manually);
			}
		});

		return false;
	});

	$('#add-sticky-with-callbacks').click(function(){

		$.gritter.add({
			// (string | mandatory) the heading of the notification
			title: 'This is a sticky notice with callbacks!',
			// (string | mandatory) the text inside the notification
			text: 'Sticky sticky notice.. sticky sticky notice...',
			// Stickeh!
			sticky: true,
			// (function | optional) function called before it opens
			before_open: function(){
				alert('I am a sticky called before it opens');
			},
			// (function | optional) function called after it opens
			after_open: function(e){
				alert("I am a sticky called after it opens: \nI am passed the jQuery object for the created Gritter element...\n" + e);
			},
			// (function | optional) function called before it closes
			before_close: function(e){
				alert("I am a sticky called before it closes: I am passed the jQuery object for the Gritter element... \n" + e);
			},
			// (function | optional) function called after it closes
			after_close: function(){
				alert('I am a sticky called after it closes');
			}
		});

		return false;

	});

	$("#remove-all").click(function(){

		$.gritter.removeAll();
		return false;

	});

	$("#remove-all-with-callbacks").click(function(){

		$.gritter.removeAll({
			before_close: function(e){
				alert("I am called before all notifications are closed.  I am passed the jQuery object containing all  of Gritter notifications.\n" + e);
			},
			after_close: function(){
				alert('I am called after everything has been closed.');
			}
		});
		return false;

	});


}



/* ---------- Page width functions ---------- */

$(window).bind("resize", widthFunctions);

function widthFunctions(e) {

    var winHeight = $(window).height();
    var winWidth = $(window).width();

	var contentHeight = $("#content").height();

	if (winHeight) {

		$("#content").css("min-height",winHeight);

	}

	if (contentHeight) {

		$("#sidebar-left2").css("height",contentHeight);

	}

	if (winWidth < 980 && winWidth > 767) {

		if($("#sidebar-left").hasClass("span2")) {

			$("#sidebar-left").removeClass("span2");
			$("#sidebar-left").addClass("span1");

		}

		if($("#content").hasClass("span10")) {

			$("#content").removeClass("span10");
			$("#content").addClass("span11");

		}


		$("a").each(function(){

			if($(this).hasClass("quick-button-small span1")) {

				$(this).removeClass("quick-button-small span1");
				$(this).addClass("quick-button span2 changed");

			}

		});

		$(".circleStatsItem, .circleStatsItemBox").each(function() {

			var getOnTablet = $(this).parent().attr('onTablet');
			var getOnDesktop = $(this).parent().attr('onDesktop');

			if (getOnTablet) {

				$(this).parent().removeClass(getOnDesktop);
				$(this).parent().addClass(getOnTablet);

			}

		});

		$(".box").each(function(){

			var getOnTablet = $(this).attr('onTablet');
			var getOnDesktop = $(this).attr('onDesktop');

			if (getOnTablet) {

				$(this).removeClass(getOnDesktop);
				$(this).addClass(getOnTablet);

			}

		});

		$(".widget").each(function(){

			var getOnTablet = $(this).attr('onTablet');
			var getOnDesktop = $(this).attr('onDesktop');

			if (getOnTablet) {

				$(this).removeClass(getOnDesktop);
				$(this).addClass(getOnTablet);

			}

		});

		$(".statbox").each(function(){

			var getOnTablet = $(this).attr('onTablet');
			var getOnDesktop = $(this).attr('onDesktop');

			if (getOnTablet) {

				$(this).removeClass(getOnDesktop);
				$(this).addClass(getOnTablet);

			}

		});

	} else {

		if($("#sidebar-left").hasClass("span1")) {

			$("#sidebar-left").removeClass("span1");
			$("#sidebar-left").addClass("span2");

		}

		if($("#content").hasClass("span11")) {

			$("#content").removeClass("span11");
			$("#content").addClass("span11");

		}

		$("a").each(function(){

			if($(this).hasClass("quick-button span2 changed")) {

				$(this).removeClass("quick-button span2 changed");
				$(this).addClass("quick-button-small span1");

			}

		});

		$(".circleStatsItem, .circleStatsItemBox").each(function() {

			var getOnTablet = $(this).parent().attr('onTablet');
			var getOnDesktop = $(this).parent().attr('onDesktop');

			if (getOnTablet) {

				$(this).parent().removeClass(getOnTablet);
				$(this).parent().addClass(getOnDesktop);

			}

		});

		$(".box").each(function(){

			var getOnTablet = $(this).attr('onTablet');
			var getOnDesktop = $(this).attr('onDesktop');

			if (getOnTablet) {

				$(this).removeClass(getOnTablet);
				$(this).addClass(getOnDesktop);

			}

		});

		$(".widget").each(function(){

			var getOnTablet = $(this).attr('onTablet');
			var getOnDesktop = $(this).attr('onDesktop');

			if (getOnTablet) {

				$(this).removeClass(getOnTablet);
				$(this).addClass(getOnDesktop);

			}

		});

		$(".statbox").each(function(){

			var getOnTablet = $(this).attr('onTablet');
			var getOnDesktop = $(this).attr('onDesktop');

			if (getOnTablet) {

				$(this).removeClass(getOnTablet);
				$(this).addClass(getOnDesktop);

			}

		});

	}



}


//<!-- ページトップへスクロールアップ -->
//notes: needs jQuery
jQuery(function($) {
  var isDisplayed = false;
  var pagetop = $('.pagetop');

  $(window).scroll(function () {
    if ( $(window).scrollTop() / $(window).height() > 0.80) {
      //スクロールの位置がwindow上部80%の範囲を超えた場合に表示
      if (isDisplayed === false) {
        isDisplayed = true;
        pagetop.stop().animate({
            'bottom': '45px'
        }, {
          duration: 200
        });
      }
    } else {
      //それ以外のスクロールの位置の場合は非表示
      hidePageTop();
    }
  });

  //windowサイズが変わった場合も非表示
  $(window).resize(function () {
    hidePageTop();
  });

  function hidePageTop () {
    if (isDisplayed) {
      isDisplayed = false;
      pagetop.stop().animate({
          'bottom': '-50px'
      }, {
        duration: 200
      });
    }
  }

  pagetop.click(function () {
    // Scroll 'em to top!
    $('body, html').animate({
      scrollTop: 0
    }, {
      duration: 500
    });
    return false;
  });

});

//feedback

jQuery(function($) {
  var feedback = $('#feedback');
  var feedback_save = $('#feedback_save');




  feedback.click(function () {
   	$('#myModal').modal('show');
   	//$('#feedback_body').append("<textarea class="feedback_textarea" rows="20" cols="10" id="feedback_textarea"></textarea>");
  });

  $('#myModal').on('show.bs.modal', function (e) {
  	$('#feedback_body').append("<textarea class='feedback_textarea' rows='20' cols='10' id='feedback_textarea'></textarea>");
  })

  $('#myModal').on('hide.bs.modal', function (e) {
  	$('#feedback_body').empty();
  })


  feedback_save.click(function () {
   	var fb = $('#feedback_textarea');
   	var url = window.location.href;
   	var $btn = $(this).button('loading')
   	if(fb.val().length>0&&fb.val().length<=2000){
   		var csrftoken = $('meta[name=csrf-token]').attr('content');
    	$.ajaxSetup({
    	  	beforeSend: function(xhr, settings) {
    	      	if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
    	      	    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    	      	}
    		}
    	});
   		$.ajax({
    	  url      : '/feedback',
    	  dataType : 'json',
    	  type     : 'post',
    	  contentType: "application/json",
    	  data:JSON.stringify({
    	            'feedback':fb.val(),
    	            'url':url
    	          }),
    	  success: function(resp) {
    	  	$btn.button('reset')
    	    alert('您的意见已经收到，谢谢反馈！');
    	    fb.val('');
    	    $('#myModal').modal('hide');
    	  }.bind(this),
    	  error: function(xhr, status, err) {
    	  	$btn.button('reset')
    	    console.error(status, err.toString);
    	    alert('发生了奇怪的问题，请再试一次');
    	  }.bind(this)
    	});
   	}else if(fb.val().length>2000){
   		$btn.button('reset');
   		alert('抱歉让您写这么多，不过我们其实只看你前面2000字哦')

   	}else{
   		$btn.button('reset');
   		alert('抱歉您什么都没写啊！')
   	}
  });



});
