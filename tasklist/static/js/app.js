var BASE_URL = window.location.origin;

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

var csrftoken = getCookie('csrftoken');

$.ajaxSetup({ 
 beforeSend: function(xhr, settings) {
     if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
         // Only send the token to relative URLs i.e. locally.
         xhr.setRequestHeader("X-CSRFToken", csrftoken);
         }
     } 
});

$(document).ready(function() {

	$('#submitTask').on('click', function(){
	    var data = $("#taskForm").serialize();

	    $.ajax({
	       type: "POST",
	       url: BASE_URL + "/mytask/create",
	       data: $("#taskForm").serialize(),
	       success: function(result) {
	       	 // console.log(result);
	         location.reload();
	       }
	    });
	});

	$('#updateTask').on('click', function(){
	    var task_head = $("#edit_task_head").val();
	    var description = $("#edit_description").val();
	    var due_date = $("#edit_due_date").val();
	    var task_id = $("#edit_task_id").val();
	    $.ajax({
	       type: "POST",
	       url: BASE_URL + "/mytask/update",
	       data: {task_id: task_id, task_head: task_head, description: description, due_date: due_date},
	       success: function(result) {
	       	 // console.log(result);
	         location.reload();
	       }
	    });
	});

	$('#search').on('click', function(e){
		var search_term = $('#search_title').val();
		if (search_term == '') {
			e.preventDefault();
		}
	});

});


function deleteTask(task_id) {

	$.ajax({
       type: "POST",
       url: BASE_URL + "/mytask/delete",
       data: {task_id: task_id},
       success: function(result) {
       	 // console.log(result);
         location.reload();
       }
    });
}


function completeTask(task_id) {

	$.ajax({
       type: "POST",
       url: BASE_URL + "/mytask/complete",
       data: {task_id: task_id},
       success: function(result) {
       	 // console.log(result);
         location.reload();
       }
    });
}

function editModel(task_id) {
	var title = $('#task_head' + task_id).text();
	var desc = $('#task_description' + task_id).html();
	var due_date = $('#due_date' + task_id).val();

	$('#edit_description').val(desc);
	$('#edit_task_head').val(title);
	$('#edit_due_date').val(due_date);
	$('#edit_task_id').val(task_id);
	$("#editTaskModel").modal();
}
