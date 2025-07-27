<?php
session_start();
include 'db.php'; // DB connection
require_once 'table.php'; // Table creation if needed

// Fetch and sanitize form input
$emailOrMobile = trim($_POST['email']);
$password = $_POST['password'];

// Check if fields are empty
if (empty($emailOrMobile) || empty($password)) {
    echo "Please fill in all fields.";
    exit();
}

// Prepare statement to prevent SQL injection
$stmt = $conn->prepare("SELECT * FROM users WHERE email = ? OR mobile = ? LIMIT 1");
$stmt->bind_param("ss", $emailOrMobile, $emailOrMobile);
$stmt->execute();
$result = $stmt->get_result();

if ($row = $result->fetch_assoc()) {
    // Verify hashed password
    if (password_verify($password, $row['password'])) {
        // Set session
        $_SESSION['username'] = $row['name'];
        $_SESSION['role'] = $row['role'];

        // Redirect based on role
        if ($row['role'] === 'admin') {
            header("Location: admin_dashboard.php");
        } elseif ($row['role'] === 'user') {
            header("Location: user_dashboard.php");
        } else {
            header("Location: dashboard.php");
        }
        exit();
    } else {
        echo "Incorrect password.";
    }
} else {
    echo "User not found.";
}

$stmt->close();
$conn->close();
?>
