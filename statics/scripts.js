var timeout = 1;
var last_bytes_sent = 0;
var last_bytes_recv = 0;

function toKB(bytes) {
    return Math.round(bytes / 1024);
}

function toMB(bytes) {
    return Math.round(bytes / 1024 / 1024);
}

function render_graph(used_percent, element) {
    var canvas = document.getElementById(element);
    var context = canvas.getContext("2d");
    var used_size = canvas.width / 100 * used_percent;
    context.fillStyle = "#a2ff60";
    context.fillRect(0, 0, used_size, canvas.height);
    context.fillStyle = "#60d4ff";
    context.fillRect(used_size, 0, canvas.width - used_size, canvas.height);
    context.fillStyle = "black";
    context.font = "15px monospace";
    context.textAlign = "center";
    context.fillText(used_percent + "%", canvas.width / 2, 15);
}

function get_memory_data() {
    $.ajax({url: '/memory/'})
        .done(function(data) {
            $("#used-memory-percent").html(data.used_memory_percent);
            $("#used-memory").html(data.used_memory);
            $("#total-memory").html(data.total_memory);
            $("#tasks-num").html(data.tasks_num);
            $("#uptime").html(data.uptime);
            render_graph(data.used_memory_percent, "used-memory-graph");
            console.log("Call for new memory data.");
        })
}

function get_network_data() {
    $.ajax({ url: '/net/' })
        .done(function (data) {
            $("#mb-sent").html(toMB(data.bytes_sent));
            $("#mb-recv").html(toMB(data.bytes_recv));         
            $("#kb-sending").html(toKB((data.bytes_sent - last_bytes_sent) / timeout));
            $("#kb-receiving").html(toKB((data.bytes_recv - last_bytes_recv) / timeout));

            last_bytes_recv = data.bytes_recv;
            last_bytes_sent = data.bytes_sent;
            
            console.log("Call for new network data.");
        })
}

function get_swap_data() {
    $.ajax({url: '/swap/'})
        .done(function(data) {
            $("#used-swap-percent").html(data.used_swap_percent);
            $("#used-swap").html(data.used_swap);
            $("#total-swap").html(data.total_swap);
            render_graph(data.used_swap_percent, "used-swap-graph");
            console.log("Call for new swap data.");
        })
}

function get_cpu_data() {
    $.ajax({url: '/cpu/'})
        .done(function(data) {
            $("#cpu-percent").html("");
            for (var i = 0; i < data.cpu_percent.length; i++) {
                var cpu_num = i + 1;
                $("#cpu-" + cpu_num).parent().parent().remove();
                $("#info-table").append(
                    "<tr><td class=\"bold\">CPU " + cpu_num + "</td><td colspan=\"2\"><canvas id=\"cpu-" + cpu_num + "\" width=\"400\" height=\"18\"></canvas></td></tr>"
                );
                render_graph(data.cpu_percent[i], "cpu-" + cpu_num);
            }
            console.log("Call for new cpu data.");
        })
}

function get_all_data() {
    get_memory_data();
    get_swap_data();
    get_cpu_data();
    get_network_data();
}

$("body").load(get_all_data());
setInterval(get_all_data, timeout * 1000);
