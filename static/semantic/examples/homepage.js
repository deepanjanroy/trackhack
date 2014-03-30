$(document)
  .ready(function() {


    try_login = function () {
      if(window.facebook_setup_complete && window.github_setup_complete){
        success_data = {
          "facebook_id" : window['fb_user_id'],
          "github_username": "foobar" // NEEEEEDS TO BE FIOXED SDFNSDLFJSDLAFKASDLFKSADFLNASDJFL SDAFK
        }
        // jQuery.post( url [, data ] [, success(data, textStatus, jqXHR) ] [, dataType ] )
        $.post("/login_success", success_data, function (data, textStatus, jqXHR) {
          window.location.replace("/userhome");
        });
      }

    }

  })
;
