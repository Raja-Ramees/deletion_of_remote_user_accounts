import paramiko
import time

# File containing server information and user list
SERVER_USER_FILE = "servers.txt"

# Function to delete a user on a server
def delete_user_on_server(server, ssh_user, ssh_password, users):
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

        for user in users:
            # Send the sudo command to delete the user
            shell.send(f"sudo userdel -r {user}\n")

            # Wait for the password prompt
            time.sleep(1)

            # Send the password
            shell.send(f"{ssh_password}\n")

            # Wait for the command to complete
            time.sleep(2)

            # Read the output
            output = shell.recv(65535).decode('utf-8')

            if "password" not in output:
                print(f"User {user} successfully deleted from {server}.")
            else:
                print(f"Failed to delete user {user} from {server}. Error: {output}")

        # Close the connection
        ssh.close()

    except Exception as e:
        print(f"An error occurred while connecting to {server}: {e}")

# Users to delete on both servers
users_to_delete = ["usr1", "usr2", "usr3", "usr4", "usr5"]

# Server details
servers = [
    {"ip": "192.168.29.182", "ssh_user": "test-02", "ssh_password": "Srw1819@20"},
    {"ip": "192.168.29.229", "ssh_user": "test-01", "ssh_password": "Srw1819@20"}
]

# Perform user deletion on all specified servers
for server in servers:
    print(f"Connecting to {server['ip']} as {server['ssh_user']} to delete users...")
    delete_user_on_server(server['ip'], server['ssh_user'], server['ssh_password'], users_to_delete)
