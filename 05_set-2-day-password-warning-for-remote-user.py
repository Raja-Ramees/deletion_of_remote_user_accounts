import paramiko

def create_or_update_user_on_remote_server(host, port, username, password, new_user, new_password):
    try:
        # Initialize SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the remote server
        ssh.connect(host, port=port, username=username, password=password)

        # Check if user exists
        check_user_command = f'getent passwd {new_user}'
        stdin, stdout, stderr = ssh.exec_command(check_user_command)
        user_exists = stdout.read().decode().strip()

        if user_exists:
            print(f"User {new_user} already exists.")
        else:
            # Commands to create user and set password expiration
            commands = [
                f'sudo useradd -m {new_user}',  # Create the new user with a home directory
                f'echo "{new_user}:{new_password}" | sudo chpasswd',  # Set the password
                f'sudo chage -M 2 {new_user}'  # Set the password to expire immediately
            ]

            # Execute commands
            for command in commands:
                stdin, stdout, stderr = ssh.exec_command(command)
                print(f"Command: {command}")
                print(f"Output: {stdout.read().decode()}")
                error = stderr.read().decode()
                if error:
                    print(f"Error: {error}")

        # Close the SSH connection
        ssh.close()

    except Exception as e:
        print(f"An error occurred: {e}")

# Configuration
host = '192.168.29.182'
port = 22
username = 'test-02'
password = 'Srw1819@20'
new_user = 'signx4'
new_password = 'Drw1819@45'

create_or_update_user_on_remote_server(host, port, username, password, new_user, new_password)
