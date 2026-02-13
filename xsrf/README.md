# XSRF (Cross-Site Request Forgery) Demo

This lab demonstrates how an attacker can trick a logged-in user
into performing actions they didn't intend to.

## How it works

1. **Insecure Application (`insecure_site.py`)**: A simple bank app running on `http://127.0.0.1:5001`.
   It uses cookies for authentication but lacks CSRF tokens on sensitive actions (like transferring money).
2. **Jackpot Application (`jackpot_site.py`)**: A malicious site running on `http://127.0.0.1:5002`.
   It contains a hidden form that sends a POST request to the bank app.

## Run with Docker

From the root directory:

```bash
docker-compose up --build
```

This will start both the insecure bank app and the malicious jackpot app.

## Local Testing

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

1. **Start the Insecure App**:
   ```bash
   python xsrf/insecure_site.py
   ```
2. From another terminal, **Start the Jackpot App**:
   ```bash
   source venv/bin/activate
   python xsrf/jackpot_site.py
   ```
3. **Login to the Bank**:
   - Go to `http://127.0.0.1:5001`
   - Login with `johndoe` / `securepass`.
   - Take note of your balance.
4. **Visit the Malicious Site**:
   - Go to `http://127.0.0.1:5002` in the **same browser**.
   - Click the "CLAIM PRIZE" button.
   - > **Note:** In some cases, the form could be immediately submitted as soon as the page loads, without you even clicking the button.
5. **Observe the result**:
   - You will be redirected back to the Bank app.
   - Notice that $500 has been transferred to "Attacker" without you ever filling out the bank's form!

## Browser Security Note

Modern browsers have a feature called `SameSite` cookies which defaults to `Lax`.
This prevents POST requests from other sites from including your cookies.

In a real-world scenario, this vulnerability often occurs when:

- The site uses an older browser configuration.
- The action is triggered via a GET request (which `Lax` allows).
- The `SameSite` attribute is explicitly set to `None`.
