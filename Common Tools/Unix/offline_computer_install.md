# System Packages
## Online PC
With Synaptic download deb files and requirements
    
    [ sudo dpkg -i <deb files>
    sudo apt install <program names>
        (python3
        python3-magic
        python-lzma
        )

        apt-offline]()

## Using Apt-offline
    files_list = gcc make g++ cmake linux-headers-$(uname -r) dkms linux-image-generic linux-image-extra-virtual linux-source linux-headers-generic gfortran build-essential pkg-config htop libatlas-base-dev libblas-dev liblapack-dev git ffmpeg qtbase5-dev libhdf5-serial-dev python python-dev python-pip

Get signature of offline pc
    
    sudo apt-offline set apt-offline.sig --install-packages <files_list>  --src-build-dep --update --upgrade

Transfer apt-offline.sig to PC with internet connection 
    
    sudo apt-offline get apt-offline.sig --bundle apt-offline_install_files.zip --threads 8

Transfer zip file to Offline PC:
    
    sudo apt-offline install /path/to/aptbundle.zip
    sudo apt install <files_list>

# Python Packages

## Online PC:

    pip3 download  <list of packages> -d target_folder/

or

    pip3 install -r requirements.txt -d target_folder/

## Offline PC:
    pip3 install --no-index --find-links=<target_folder> pip <list of packages> --upgrade
