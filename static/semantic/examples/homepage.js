$(document)
  .ready(function() {

    var
      changeSides = function() {
        $('.ui.shape')
          .eq(0)
            .shape('flip over')
            .end()
          .eq(1)
            .shape('flip over')
            .end()
          .eq(2)
            .shape('flip back')
            .end()
          .eq(3)
            .shape('flip back')
            .end()
        ;
      },
      validationRules = {
        firstName: {
          identifier  : 'email',
          rules: [
            {
              type   : 'empty',
              prompt : 'Please enter an e-mail'
            },
            {
              type   : 'email',
              prompt : 'Please enter a valid e-mail'
            }
          ]
        }
      }
    ;

    $('.ui.dropdown')
      .dropdown({
        on: 'hover'
      })
    ;

    $('.ui.form')
      .form(validationRules, {
        on: 'blur'
      })
    ;

    $('.masthead .information')
      .transition('scale in')
    ;

    setInterval(changeSides, 3000);

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
