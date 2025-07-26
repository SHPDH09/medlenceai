<?php
session_start();
include 'db.php';         // Database connection
require_once 'table.php'; // Table creation if not exists

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name     = trim($_POST['fullname']);
    $email    = trim($_POST['email']);
    $phone    = trim($_POST['phone']);
    $password = trim($_POST['password']);
    $confirm  = trim($_POST['confirm_password']);

    // Check for empty fields
    if (empty($name) || empty($email) || empty($phone) || empty($password) || empty($confirm)) {
        die("Please fill all fields.");
    }

    // Confirm password match
    if ($password !== $confirm) {
        die("Passwords do not match.");
    }

    // Check if user already exists
    $stmt = $conn->prepare("SELECT id FROM users WHERE email = ? OR phone = ?");
    $stmt->bind_param("ss", $email, $phone);
    $stmt->execute();
    $stmt->store_result();
    if ($stmt->num_rows > 0) {
        die("Email or phone already registered.");
    }

    // Hash the password
    $hashed_password = password_hash($password, PASSWORD_DEFAULT);

    // Insert new user
    $insert = $conn->prepare("INSERT INTO users (name, email, phone, password, role) VALUES (?, ?, ?, ?, ?)");
    $default_role = 'user'; // Default role
    $insert->bind_param("sssss", $name, $email, $phone, $hashed_password, $default_role);

    if ($insert->execute()) {
        header("Location: index.html?register=success");
        exit();
    } else {
        die("Registration failed. Try again.");
    }
}
?>
