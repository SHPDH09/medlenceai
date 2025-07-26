<?php
require_once 'table.php';
$host = 'mysql-e8883ac-raunakkumarjob-7886.i.aivencloud.com';
$port = 12637;
$username = 'avnadmin';
$password = 'AVNS_rFSiPQG-ybjDAzwlU6n';
$database = 'defaultdb';

// Enable SSL connection
$ssl = [
    MYSQLI_OPT_SSL_VERIFY_SERVER_CERT => true
];

// Create connection
$conn = mysqli_init();
$conn->ssl_set(NULL, NULL, NULL, NULL, NULL);  // You can add cert paths here if needed
$conn->real_connect($host, $username, $password, $database, $port, NULL, MYSQLI_CLIENT_SSL);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} else {
    // echo "Connected successfully!";
}
?>
