<?php
require_once 'table.php';

$host = 'mysql-e8883ac-raunakkumarjob-7886.i.aivencloud.com';
$port = 12637;
$username = 'avnadmin';
$password = 'AVNS_rFSiPQG-ybjDAzwlU6n';
$database = 'defaultdb';

$conn = mysqli_init();
if (!$conn) {
    die("mysqli_init failed");
}

// Optional: Set path to your SSL certs (if required by Aiven)
// $conn->ssl_set('/path/to/client-key.pem', '/path/to/client-cert.pem', '/path/to/ca.pem', NULL, NULL);

$conn->ssl_set(NULL, NULL, NULL, NULL, NULL);

if (!$conn->real_connect($host, $username, $password, $database, $port, NULL, MYSQLI_CLIENT_SSL)) {
    die("Connection failed: " . mysqli_connect_error());
} else {
    // echo "Connected successfully!";
}
?>
