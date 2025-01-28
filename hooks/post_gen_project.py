#!/usr/bin/env python
import uuid
import secrets
import string


def generate_uplink_key(prefix=''):
    """Generate a unique key using UUID4 (random UUID)"""
    # UUID4 provides 122 bits of randomness
    unique_id = str(uuid.uuid4()).replace('-', '').upper()
    return f"{prefix}{unique_id}"


def generate_secure_password():
    """Generate a secure random password for database"""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(32))


def create_env_file():
    """Create .env file with secure credentials"""
    # Read the template
    with open('env.template', 'r') as f:
        env_content = f.read()

    # Generate secure credentials
    replacements = {
        'POSTGRES_PASSWORD=anvil': f'POSTGRES_PASSWORD={generate_secure_password()}',
        'CLIENT_UPLINK_KEY=client_uplink_key': f'CLIENT_UPLINK_KEY={generate_uplink_key("client_")}',
        'SERVER_UPLINK_KEY=server_uplink_key': f'SERVER_UPLINK_KEY={generate_uplink_key("server_")}'
    }

    # Replace placeholders with secure values
    for old, new in replacements.items():
        env_content = env_content.replace(old, new)

    # Write the .env file
    with open('.env', 'w') as f:
        f.write(env_content)


def main():
    """Post project generation hook"""
    create_env_file()


if __name__ == '__main__':
    main()
