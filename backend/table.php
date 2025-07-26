<?php
// Aiven MySQL cloud credentials
$host = "mysql-e8883ac-raunakkumarjob-7886.i.aivencloud.com";
$port = 12637;
$username = "avnadmin";
$password = "AVNS_rFSiPQG-ybjDAzwlU6n";
$database = "defaultdb";

// Create connection
$conn = mysqli_init();
mysqli_ssl_set($conn, NULL, NULL, NULL, NULL, NULL); // SSL Required for Aiven
mysqli_real_connect($conn, $host, $username, $password, $database, $port, NULL, MYSQLI_CLIENT_SSL);

// Check connection
if (mysqli_connect_errno()) {
    die("Connection failed: " . mysqli_connect_error());
}

// Create table if not exists
$sql = "
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(15) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
";

if (mysqli_query($conn, $sql)) {
    echo "Table 'users' created successfully or already exists.";
} else {
    echo "Error creating table: " . mysqli_error($conn);
}

// Close connection
mysqli_close($conn);
?>
