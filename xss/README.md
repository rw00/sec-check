# RW Demo Labs 🛡️

This project is a simple Python server designed to demonstrate a Stored **Cross-Site Scripting (XSS)** vulnerability.

## Prerequisites

- Python 3.x or Docker

## Run with Docker

From the root directory:

```bash
docker-compose up --build
```

This will start the XSS demo server on [http://localhost:5005](http://localhost:5005).

## Manual Build and Run

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
2. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the server:
   ```bash
   python app.py
   ```
5. Open your browser and navigate to:
   [http://127.0.0.1:5005](http://127.0.0.1:5005)

6. Try this as a comment:

   ```html
   <img src="x" onclick="console.log('XSS: Rekt!')" />
   ```

7. Check the console logs.

## The Vulnerability

This app demonstrates stored **XSS**
(also known as persistent XSS) security issue.

### What is Stored XSS?

Stored XSS occurs when an application receives data from a user
and stores it in a database without proper sanitization.
This data is then rendered on a page for other users to see.
Every time any user views the page, the malicious script executes in their browser.

## How to Fix

To prevent XSS:

1. **Validate** input.
2. **Sanitize** output.
3. **Escape** output.
