<?php
// DB credentials
$host = 'mysql-e8883ac-raunakkumarjob-7886.i.aivencloud.com';
$port = 12637;
$username = 'avnadmin';
$password = 'AVNS_rFSiPQG-ybjDAzwlU6n';
$database = 'defaultdb';

// SSL connection
$conn = mysqli_init();
mysqli_ssl_set($conn, NULL, NULL, NULL, NULL, NULL);
mysqli_real_connect($conn, $host, $username, $password, $database, $port, NULL, MYSQLI_CLIENT_SSL);

// Error check
if (mysqli_connect_errno()) {
    die("Database connection failed: " . mysqli_connect_error());
}

// Fetch form data
$name = $_POST['name'];
$email = $_POST['email'];
$phone = $_POST['phone'];
$pass = password_hash($_POST['password'], PASSWORD_BCRYPT);
$role = 'user';

// Insert into DB
$query = "INSERT INTO users (name, email, phone, password, role) VALUES (?, ?, ?, ?, ?)";
$stmt = mysqli_prepare($conn, $query);
mysqli_stmt_bind_param($stmt, "sssss", $name, $email, $phone, $pass, $role);

if (mysqli_stmt_execute($stmt)) {
    echo "✅ Registration successful!";
} else {
    echo "❌ Error: " . mysqli_error($conn);
}

// Cleanup
mysqli_stmt_close($stmt);
mysqli_close($conn);
?>
