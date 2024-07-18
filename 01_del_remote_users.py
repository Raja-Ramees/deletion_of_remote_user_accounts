import paramiko
import time

# File containing servers and users
SERVER_USER_FILE = "servers.txt"

# SSH user for connecting to the servers
SSH_USER = "test-02"

# SSH password
SSH_PASSWORD = "pdrw1819@20"

def delete_user_on_server(server, user, ssh_user, ssh_password):
    try:
        # Create an SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the server
        ssh.connect(server, username=ssh_user, password=ssh_password)

        # Create an interactive shell session
        shell = ssh.invoke_shell()

        # Wait for the shell to be ready
        time.sleep(1)

        # Send the sudo command
        shell.send(f"sudo userdel -r {user}\n")

        # Wait for the password prompt
        time.sleep(1)

        # Send the password
        shell.send(f"{ssh_password}\n")

        # Wait for the command to complete
        time.sleep(2)

        # Read the output
        output = shell.recv(65535).decode('utf-8')

        # Close the connection
        ssh.close()

        if "password" not in output:
            print(f"User {user} successfully deleted from {server}.")
        else:
            print(f"Failed to delete user {user} from {server}. Error: {output}")

    except Exception as e:
        print(f"An error occurred while connecting to {server}: {e}")

# Read the file line by line
with open(SERVER_USER_FILE, "r") as file:
    for line in file:
        server, user = line.strip().split(":")
        print(f"Connecting to {server} to delete user {user}...")
        delete_user_on_server(server, user, SSH_USER, SSH_PASSWORD)
