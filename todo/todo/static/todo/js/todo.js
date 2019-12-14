var todoItems = [];

var csrftoken = $("input[name=csrfmiddlewaretoken]").val();

$(document).ready(function() {
    $.ajax({
        "url": "http://localhost:8000/get-data",
        "success": function(data) {
            alert(data);
        }
    });
});

showRows();


$("#input-field").keyup(function(e) {
    if(e.keyCode == 13 && $("#input-field").val().trim().length > 0) {
        row = {
            "id": todoItems.length + 1,
            "done": false,
            "job": $("#input-field").val().trim()
        };
        todoItems.push(row);

        showRows();

        $("#input-field").val("");

        $.ajax({
            "method": "POST",
            "datatype": "json",
            "url": "http://localhost:8000/save-data",
            "data": {
                "csrfmiddlewaretoken": csrftoken,
                "todoItems": JSON.stringify(todoItems),
                "action": 'post'
            },
            "success": function(e) {
                console.log(e);
            }
        });
    }
});

$("div#rows").on("click", "div.row input", function(e) {
    doCheck();
});

function doCheck() {

    $("div.row").removeClass("selected");

    for(id in todoItems) {
        todoItems[id].done = false;
    }

    arr = $("div.row input:checked");
    for(i=0; i < arr.length; i++) {
        $par = $(arr[i]).parent();
        $par.addClass("selected");

        rowId = $(arr[i]).data("id");
        for(id in todoItems) {
            if(todoItems[id].id == rowId) {
                todoItems[id].done = true;
            }
        }
    }
}

function showRows() {
    $("div#rows").empty();
    for(id in todoItems) {
        row = todoItems[id];

        rowHtmlText = '<div class="row">'+
            '<input type="checkbox" name="" data-id="'+row.id+'">'+
            '<span>'+ row.job +'</span>'+
        '</div>';
        $("div#rows").append(rowHtmlText);
    }
}