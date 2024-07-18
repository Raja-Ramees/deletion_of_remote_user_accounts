# User Account Deletion on Remote Servers

Welcome to the **User Account Deletion** repository! This repository provides Python scripts to help you manage user accounts by deleting them on remote servers. Whether you need to clean up user accounts from multiple servers or handle specific user removals, these scripts offer a straightforward solution.

## Repository Contents

1. **`01_del_remote_users.py`**: Script for deleting user accounts on a single remote server.
2. **`02_del_remote_user.py`**: Script for deleting user accounts on a different remote server.
3. **`server.txt`**: Configuration file containing the IP addresses and usernames of remote servers.

## Overview

### `01_del_remote_users.py`

This script is designed to delete user accounts from a specific remote server. It handles up to 5 user accounts for a single server. The server details are specified in the `server.txt` file.

### `02_del_remote_user.py`

This script is intended for use with a different remote server and handles a distinct set of user accounts. Similar to the previous script, it uses the `server.txt` configuration file for server details.

### `server.txt`

The `server.txt` file contains the IP addresses and usernames of the remote servers. It allows the scripts to identify and connect to the correct servers for user account deletion.

## Features

- **Flexible**: Manage user accounts on multiple remote servers.
- **Easy Configuration**: Use a simple `server.txt` file to specify server details.
- **Streamlined Process**: Python scripts automate the user account deletion process, saving you time and effort.

## Prerequisites

Before running the scripts, ensure you have the following:

- Python 3.x installed on your local machine.
- `paramiko` library for SSH communication. Install it using:
  ```bash
  pip install paramiko
Configuration
server.txt Format
The server.txt file should have the following format:
<server_ip1> <username1>
<server_ip2> <username2>
<server_ip3> <username3>
Each line contains the IP address and username of a remote server, separated by a space.

Usage
Deleting Users from a Single Remote Server
Edit server.txt: Ensure it contains the correct IP address and username for the server.
Run the Script: Execute the 01_del_remote_users.py script.
python 01_del_remote_users.py

Certainly! Below is the complete content for the README.md file. This file is designed to be comprehensive and attractive, including all necessary sections for understanding and using the Python scripts for deleting user accounts on remote servers.

markdown
Copy code
# User Account Deletion on Remote Servers

Welcome to the **User Account Deletion** repository! This repository provides Python scripts to help you manage user accounts by deleting them on remote servers. Whether you need to clean up user accounts from multiple servers or handle specific user removals, these scripts offer a straightforward solution.

## Repository Contents

1. **`01_del_remote_users.py`**: Script for deleting user accounts on a single remote server.
2. **`02_del_remote_user.py`**: Script for deleting user accounts on a different remote server.
3. **`server.txt`**: Configuration file containing the IP addresses and usernames of remote servers.

## Overview

### `01_del_remote_users.py`

This script is designed to delete user accounts from a specific remote server. It handles up to 5 user accounts for a single server. The server details are specified in the `server.txt` file.

### `02_del_remote_user.py`

This script is intended for use with a different remote server and handles a distinct set of user accounts. Similar to the previous script, it uses the `server.txt` configuration file for server details.

### `server.txt`

The `server.txt` file contains the IP addresses and usernames of the remote servers. It allows the scripts to identify and connect to the correct servers for user account deletion.

## Features

- **Flexible**: Manage user accounts on multiple remote servers.
- **Easy Configuration**: Use a simple `server.txt` file to specify server details.
- **Streamlined Process**: Python scripts automate the user account deletion process, saving you time and effort.

## Prerequisites

Before running the scripts, ensure you have the following:

- Python 3.x installed on your local machine.
- `paramiko` library for SSH communication. Install it using:
  ```bash
  pip install paramiko
Access credentials for the remote servers (e.g., SSH keys or passwords).
Configuration
server.txt Format
The server.txt file should have the following format:

php
Copy code
<server_ip1> <username1>
<server_ip2> <username2>
<server_ip3> <username3>
Each line contains the IP address and username of a remote server, separated by a space.

Usage
Deleting Users from a Single Remote Server
Edit server.txt: Ensure it contains the correct IP address and username for the server.
Run the Script: Execute the 01_del_remote_users.py script.
bash
Copy code
python 01_del_remote_users.py
Deleting Users from a Different Remote Server
Edit server.txt: Make sure it lists the correct server details.
Run the Script: Execute the 02_del_remote_user.py script.
python 02_del_remote_user.py
Example
Suppose server.txt contains:
192.168.1.100 admin
192.168.1.101 root

Certainly! Below is the complete content for the README.md file. This file is designed to be comprehensive and attractive, including all necessary sections for understanding and using the Python scripts for deleting user accounts on remote servers.

markdown
Copy code
# User Account Deletion on Remote Servers

Welcome to the **User Account Deletion** repository! This repository provides Python scripts to help you manage user accounts by deleting them on remote servers. Whether you need to clean up user accounts from multiple servers or handle specific user removals, these scripts offer a straightforward solution.

## Repository Contents

1. **`01_del_remote_users.py`**: Script for deleting user accounts on a single remote server.
2. **`02_del_remote_user.py`**: Script for deleting user accounts on a different remote server.
3. **`server.txt`**: Configuration file containing the IP addresses and usernames of remote servers.

## Overview

### `01_del_remote_users.py`

This script is designed to delete user accounts from a specific remote server. It handles up to 5 user accounts for a single server. The server details are specified in the `server.txt` file.

### `02_del_remote_user.py`

This script is intended for use with a different remote server and handles a distinct set of user accounts. Similar to the previous script, it uses the `server.txt` configuration file for server details.

### `server.txt`

The `server.txt` file contains the IP addresses and usernames of the remote servers. It allows the scripts to identify and connect to the correct servers for user account deletion.

## Features

- **Flexible**: Manage user accounts on multiple remote servers.
- **Easy Configuration**: Use a simple `server.txt` file to specify server details.
- **Streamlined Process**: Python scripts automate the user account deletion process, saving you time and effort.

## Prerequisites

Before running the scripts, ensure you have the following:

- Python 3.x installed on your local machine.
- `paramiko` library for SSH communication. Install it using:
  ```bash
  pip install paramiko
Access credentials for the remote servers (e.g., SSH keys or passwords).
Configuration
server.txt Format
The server.txt file should have the following format:

php
Copy code
<server_ip1> <username1>
<server_ip2> <username2>
<server_ip3> <username3>
Each line contains the IP address and username of a remote server, separated by a space.

Usage
Deleting Users from a Single Remote Server
Edit server.txt: Ensure it contains the correct IP address and username for the server.
Run the Script: Execute the 01_del_remote_users.py script.
bash
Copy code
python 01_del_remote_users.py
Deleting Users from a Different Remote Server
Edit server.txt: Make sure it lists the correct server details.
Run the Script: Execute the 02_del_remote_user.py script.
bash
Copy code
python 02_del_remote_user.py
Example
Suppose server.txt contains:

Copy code
192.168.1.100 admin
192.168.1.101 root
Running 01_del_remote_users.py will connect to 192.168.1.100 as admin and delete up to 5 users specified in the script.

Similarly, 02_del_remote_user.py will operate on 192.168.1.101 with root access.

Contributing
Feel free to contribute to this repository! If you have improvements or additional features in mind, open an issue or create a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any questions or support, please reach out to your-email@example.com.

Thank you for using the User Account Deletion scripts! We hope these tools make your server management tasks easier and more efficient.

### Key Points:

- **Repository Contents**: Lists the files and their purposes.
- **Overview**: Explains each script and its functionality.
- **Features**: Highlights the benefits of using the scripts.
- **Prerequisites**: Details what you need before running the scripts.
- **Configuration**: Shows how to format the `server.txt` file.
- **Usage**: Instructions for running each script.
- **Example**: Provides a real-world scenario for clarity.
- **Contributing**: Encourages collaboration and contributions.
- **License**: Mentions the licensing details.
- **Contact**: Provides an email for support.

Feel free to customize the contact information and any other details to suit your needs.
