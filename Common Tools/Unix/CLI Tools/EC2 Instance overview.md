## To get the AWS EC2 instance id:
    curl http://169.254.169.254/latest/meta-data/instance-id    -> i-1234567890
    curl http://169.254.169.254/latest/meta-data/local-ipv4     -> i-1234567890

## Instance commands:
    aws ec2 start-instances --instance-ids <instance_id>
    aws ec2 describe-instance-status --instance-ids <instance_id>
    aws ec2 stop-instances --instance-ids <instance_id>

    curl http://169.254.169.254/latest/meta-data/instance-id # Get Instance ID
    ->i-0eeca1fa22251bc01

    curl http://169.254.169.254/latest/meta-data/local-ipv4 # Get IP address

## Logging in:
    ssh user@example_address

    ssh -p 3022 connect over specified port

    ssh -L 6006:localhost:6006 user@example_address
        port 6006 on instance is now accessible locally:
        useful for jupyter notebook and tensorboard

        -> jupyter notebook --no-browser --port=6006
            open locally using link and code returned

    ssh -X user@example_address
        allows you to plot something on the instance e.g. plt.imshow(img), ;plt.show()
        and have it display on your local pc*

        * may need to do this before plotting
            import matplotlib
            matplotlib.use('GTKAgg')
            import matplotlib.pyplot as plt

## Carrying Access keys with you:
    1. ssh-agent                        - make sure ssh-agent is running
    2. ssh-add                          - add you local keys to the agent
    3. ssh -A username@example_address  - carry keys with you when signing in
    4. git clone <private repo you can only access on your starting machine>
        This should be able to clone from your private repo as if you are using a pc with
        accepted credentials (such as your laptop)

## Check CUDA and nvidia drivers are present
    nvcc        - should complain about not having input files
    nvidia-smi  - should show you the GPU memory and processing


## Creating a python virtualenv:
```bash
python3.6 -m venv p_3.6_venv # creates a virtualenv by the name p_3.6_venv

source p_3.6_venv/bin/activate
(p_3.6_venv)-> username:~$ pip install -r requirements.txt
(p_3.6_venv)-> username:~$ pip install numpy scipy ....
(p_3.6_venv)-> username:~$ deactivate
```

## Transferring Files:
```bash
scp path_to_local_file user@example_address:path_on_instance    (defaults to home directory)
    -P 1234 to specify port
```
Even better use rsync:

```bash
rsync -hztv --partial --progress path_to_local_file user@example_address:path_on_instance
```
you can transfer from the instance to your pc by flipping the path parameters around.


## Using Screen:
    screen
    screen -list
    screen -r {id}

    ctrl + a:d - detach
             c - create
             n - next
             p - previous
