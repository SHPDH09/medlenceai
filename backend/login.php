<?php
session_start();
include 'db.php'; // DB connection
require_once 'table.php'; // Create table if not exists

// Fetch form values
$email = $_POST['email'];
$password = $_POST['password'];

// Validate input
if (empty($email) || empty($password)) {
    echo "Please fill in all fields.";
    exit();
}

// Query to match user
$sql = "SELECT * FROM users WHERE email='$email' OR mobile='$email' LIMIT 1";
$result = mysqli_query($conn, $sql);

if ($row = mysqli_fetch_assoc($result)) {
    if ($row['password'] === $password) {
        // Set session values
        $_SESSION['username'] = $row['name'];
        $_SESSION['role'] = $row['role']; // Assume you have a 'role' column in your table

        // Redirect based on role
        if ($row['role'] === 'admin') {
            header("Location: admin_dashboard.php");
        } elseif ($row['role'] === 'user') {
            header("Location: user_dashboard.php");
        } else {
            header("Location: dashboard.php"); // default fallback
        }
        exit();
    } else {
        echo "Incorrect password.";
    }
} else {
    echo "User not found.";
}

mysqli_close($conn);
?>
