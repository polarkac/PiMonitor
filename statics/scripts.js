function render_graph(used_percent, element) {
    var canvas = document.getElementById(element);
    var context = canvas.getContext("2d");
    var used_size = canvas.width / 100 * used_percent;
    context.fillStyle = "#a2ff60";
    context.fillRect(0, 0, used_size, canvas.height);
    context.fillStyle = "#60d4ff";
    context.fillRect(used_size, 0, canvas.width - used_size, canvas.height);
    context.fillStyle = "black";
    context.font = "15px serif";
    context.textAlign = "center";
    context.fillText(used_percent + "%", 100, 15);
}

function get_memory_data() {
    $.ajax({url: '/memory/'})
        .done(function(data) {
            $("#used_memory_percent").html(data.used_memory_percent);
            $("#used_memory").html(data.used_memory);
            $("#total_memory").html(data.total_memory);
            $("#tasks_num").html(data.tasks_num);
            $("#uptime").html(data.uptime);
            render_graph(data.used_memory_percent, "used_memory_graph");
            console.log("Call for new memory data.");
        })
}

function get_swap_data() {
    $.ajax({url: '/swap/'})
        .done(function(data) {
            $("#used_swap_percent").html(data.used_swap_percent);
            $("#used_swap").html(data.used_swap);
            $("#total_swap").html(data.total_swap);
            render_graph(data.used_swap_percent, "used_swap_graph");
            console.log("Call for new swap data.");
        })
}

function get_cpu_data() {
    $.ajax({url: '/cpu/'})
        .done(function(data) {
            $("#cpu_percent").html("");
            for (var i = 0; i < data.cpu_percent.length; i++) {
                var cpu_num = i + 1
                $("#cpu_percent").append(
                        "<tr><td class=\"first_column\">CPU " + cpu_num + "</td><td><canvas id=\"cpu_" + cpu_num + "\" width=\"200\" height=\"18\"></canvas></td><td>" + data.cpu_percent[i] + "%</td></tr>"
                );
                render_graph(data.cpu_percent[i], "cpu_" + cpu_num);
            }
            console.log("Call for new cpu data.");
        })
}

function get_all_data() {
    get_memory_data();
    get_swap_data();
    get_cpu_data();
}

$("body").load(get_all_data());
setInterval(get_all_data, 5000);
