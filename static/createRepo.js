$.fn.getRepoName = function()
{
	var nameArr = this.serializeArray();
	return "{ \"name\": \"" + nameArr[0].value + "\" }"
}

$(function() {
    $('#crtRepo').submit(function() {
        var repoName = $("#crtRepo").getRepoName();
        console.log(repoName);
        $.post('', param1: 'value1', function(data, textStatus, xhr) {
        	/*optional stuff to do after success */
        });
        return repoName;
    });
});