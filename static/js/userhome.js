update_page_content = function () {
  $("#th_content").text("Hey" + window['user_profile']["Name"]);
}

get_current_user_profile = function (facebook_id) {
  $.get("api/user_profile/fb/" + facebook_id, function(data) {
    window['user_profile'] = JSON.parse(data);

    if (window['user_profile']) { // Hack: If there's an error the server returns false.
    update_page_content();
    }
    else {
      alert("You're not logged in :-/");
      window.location.replace("https://localhost:8080");
    }

  });
}
