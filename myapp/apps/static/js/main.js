'use strict';

$(document).ready(function(){
    $('.mdl-button__action').click(function(event){
        event.preventDefault();
        var file, description, link;
        file = $('#file').val()
        description = $('#description').val()
        link = $('#link').val()
        if(file.length >0 && description.length>0 && link.length>0)
            $('#app_form').submit();
    })
})
