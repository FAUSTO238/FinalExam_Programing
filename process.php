<?php
$items = isset($_GET['items']) ? $_GET['items'] : [];
if (empty($items)) {
    echo "<h3>No se seleccionó ningún elemento.</h3>";
    exit;
}
$items_str = implode(" ", $items);
$command = "python3 /var/www/html/party_planner.py " . $items_str;
$output = shell_exec($command);
echo $output;
?>
