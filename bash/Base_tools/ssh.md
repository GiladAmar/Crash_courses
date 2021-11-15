# Basic use
ssh username@address

    -i <fname> use certificate as authentication
    -X Tunnel graphical displays 
        (i.e. plt.show() on instance shows picture on your desktop)
        If it fails use -Y
    -A Authentication forwarding (make sure ssh-agent is running and ssh-add has been run)
        useful for git clones/pulls etc.
        e.g.
            ssh-agent
            ssh-keygen
            ssh-add
            ssh -A gilad@whatever
    -p Specify port


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
All you need to login now is `ssh webserver` or `ssh dhcp`.

# sshfs
makes remote directory appear in the local folder sshfs-dir
```bash
sudo apt install -y sshfs
sshfs gilad@thisaddress.dp: sshfs-dir
umount sshfs-dir
```