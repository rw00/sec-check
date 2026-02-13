# Security Check 🛡️

This repository contains interactive demos of common web security vulnerabilities: **XSS** and **XSRF (Cross-Site Request Forgery)**.

## Project Structure

- `/xss`: Cross-Site Scripting demo.
- `/xsrf`: Cross-Site Request Forgery demo (includes a target bank app and a malicious attacker site).

## Quick Start with docker-compose

1. **Start all apps**:

   ```bash
   docker-compose up --build
   ```

2. **Access the apps**:
   - **XSS Demo**: [http://localhost:5005](http://localhost:5005)
   - **XSRF Bank (Target)**: [http://localhost:5001](http://localhost:5001)
   - **XSRF Malicious Site**: [http://localhost:5002](http://localhost:5002)
