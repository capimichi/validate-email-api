# Validate Email API

This project provides an API to validate email addresses using various checks such as format, blacklist, DNS, and SMTP.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/validate-email-api.git
    cd validate-email-api
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file and set the environment variables:
    ```env
    API_URL=http://0.0.0.0:8000
    API_HOST=0.0.0.0
    API_PORT=8000
    ```

## Usage

1. Run the API server:
    ```bash
    uvicorn validateemailapi.api:app --reload
    ```

2. Send a POST request to validate an email address:
    ```bash
    curl -X POST "http://0.0.0.0:8000/validate-email/" -H "Content-Type: application/json" -d '{
        "email_address": "example@example.com",
        "check_format": true,
        "check_blacklist": true,
        "check_dns": true,
        "dns_timeout": 10,
        "check_smtp": true,
        "smtp_timeout": 10,
        "smtp_helo_host": "my.host.name",
        "smtp_from_address": "my@from.addr.ess",
        "smtp_skip_tls": false,
        "smtp_tls_context": null,
        "smtp_debug": false
    }'
    ```

## License

This project is licensed under the MIT License.