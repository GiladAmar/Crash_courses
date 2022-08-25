# Basic use
ssh username@address

|   Option   | Description                                                                         |
|:----------:|:------------------------------------------------------------------------------------|
| -i <fname> | use certificate as authentication                                                   |
|     -X     | Tunnel graphical displays<br/>(i.e. plt.show() on instance shows picture on your desktop)                         |
|            | If it fails use -Y                                                                  |
|            | You may need to use another matplotlib backend using "matplotlib.use('GTKAgg')"     |
|     -A     | Authentication forwarding (make sure ssh-agent is running and ssh-add has been run) |
|            | useful for git clones/pulls etc.                                                    |
|            | e.g.                                                                                |
|            | ssh-agent                                                                           |
|            | ssh-keygen                                                                          |
|            | ssh-add                                                                             |
|            | ssh -A gilad@whatever                                                               |
|     -p     | Specify port                                                                        |

- ssh-add will add ALL private keys for forwarded
- ssh -i ~/.ssh/id_ed25519 ... will just use the one.

# Port Tunneling
To tunnel a port ie port 3306 on my pc corresponds to what is on port 3306 on instance:
```bash
ssh -L <local-port>:<connect-to-host>:<connect-to-port>
```
e.g. 
```bash 
ssh -L 3306:mysql.suso.org:3306 username@arvo.suso.org
```

# Using a config file
Add to ~/.ssh/config:
```
Host webserver
    HostName 192.168.225.22
    User sk
    Port 2233                               # Optional
    IdentityFIle ~/.ssh/id_rsa_remotesystem # Optional when using ssh keyfile
    ForwardAgent yes                        # If using agent-forwarding (Carrying local keys with you)

Host dhcp
    HostName 192.168.225.25
    User ostechnix
    Port 2233
```
All you need to log in now is `ssh webserver` or `ssh dhcp`.

# sshfs
makes remote directory appear in the local folder sshfs-dir
```bash
sudo apt install -y sshfs
sshfs gilad@thisaddress.dp: sshfs-dir
umount sshfs-dir
```

# Creating an ssh key
```ssh-keygen -a 100 -t ed25519 -f ~/.ssh/id_ed25519 -C "user@email.com"```

|          Option          | Description                                                                                                                                     |
|:------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------|
|         -a  100          | Perform 100 key derivation function rounds.<br/>Larger numbers are harder to brute-force but make verification slower.                          |
|        -t ed25519        | Use the ed25519 algorithm.<br/>The default is rsa which is less secure and a longer string.                                                     |
| -f     ~/.ssh/id_ed25519 | Place in the filepath ~/.ssh/id_ed25519.<br/>This is the default location. \<br/>If the flag is omitted ssh-keygen will prompt for a directory. |
| -C     "user@email.com"  | A comment, could be anything, but convention is to specify a means of contact.                                                                  |