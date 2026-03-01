# # Navodaya Prep LMS – Secure Content Delivery Platform

A full-stack learning management system that enables secure digital distribution of coaching materials for JNVST aspirants with user authentication, dynamic watermarking and access audit logging to mitigate unauthorized content sharing.

---

## Features

- Student Registration and Login Authentication
- Protected Access to Study Materials
- View-Only PDF Rendering (No Direct Download)
- Page-Level Dynamic Watermarking using User Email
- Screenshot Traceability
- Right Click and Print Disabled
- Access Log Tracking System
- Admin Panel for Monitoring Student Access
- Session-Based Authentication

---

## System Architecture

- Flask-based backend handles authentication and session management
- SQLite database stores user credentials and material access logs
- PDF.js renders study materials as canvas elements in the browser
- Dynamic watermark overlay embeds authenticated user identity within each rendered page
- Access audit system records user activity for administrative monitoring

---

## Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Flask (Python)
- Database: SQLite
- PDF Rendering: PDF.js
- Version Control: Git & GitHub

---

## Security Features

- Login-Based Content Access
- View-Only Material Rendering
- Dynamic User-Specific Watermark Overlay
- Basic Content Misuse Prevention
- Admin Access Control
- Access Audit Logging

---

## Access Log System

Each time a student opens study materials:

- Email ID
- Material Accessed
- Timestamp

is stored in the database to monitor content usage and detect potential misuse.

---

## Problem Solved

Offline coaching centers face difficulty in securely distributing digital study materials to students without risk of unauthorized sharing.

This platform introduces a secure digital delivery system that embeds user identity within viewed content to discourage redistribution of proprietary resources.

---

## Future Improvements

- Online Test Module
- Performance Tracking Dashboard
- Admin Upload Panel
- Mobile Responsiveness
- Cloud Deployment
- OTP Based Authentication

---

## Developed By

Sheetal sagari. B S
BE CSE, NIE Mysuru
