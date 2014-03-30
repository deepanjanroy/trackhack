$(document)
  .ready(function() {


    try_login = function () {
      if(window.facebook_setup_complete && window.github_setup_complete){
        success_data = {
          "facebook_id" : window['fb_user_id'],
          "github_username": window['github_username']
        }
        $.post("/login_success", success_data, function (data, textStatus, jqXHR) {
          alert(success_data);
          window.location.replace("/userhome");
        });
      }

    }

  })
;
