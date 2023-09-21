## Installation

1. Download Ubuntu Server ISO
2. Create bootable USB
    - use software like Rufus
3. Install Ubuntu and Boot from USB

## Post-Installation

```run-bash
# 1. Update Packages
sudo apt update && sudo apt upgrade
```

## Samba setup

```run-bash
# 1. Install samba
sudo apt install samba
```

```run-bash
# 2. Configure shares - edit `/etc/samba/smb.conf`
sudo code /etc/samba/smb.conf
```

```run-bash
# 3. Restart samba
sudo systemctl restart smbd

```

## Plex setup

```run-bash
# 1. Download Plex - Get the full URL from Plex's website:
wget https://downloads.plex.tv/plex-media-server/.../plex.deb
```

```run-bash
# 2. Install Plex
sudo dpkg -i plex.deb
```

```run-bash
# 3. Open Plex
# Access from `http://[ServerIP]:32400/web`
```

## Custom Apps with Docker

```run-bash
# 1. Install Docker
sudo apt install docker.io
```

```run-bash
# 2. Run apps - deploy custom apps using Docker
docker run -d --name my-app -p 8080:8080 my-app-image
```

## VPN Setup

```run-bash
# 1. Install WireGuard or OpenVPN
sudo apt install wireguard  # or openvpn
```

## Linux Virtual Machine

```run-bash
# 1. Install `VirtualBox`:
sudo apt install virtualbox
```

```run-bash
# 2. Create Virtual network
# Use the GUI with `VirtualBox` to a new Linux VM (Ubuntu or 
# otherwise)
```

```run-bash
# 3. Configure network
# Set the network adapter to 'Bridged Adapter' for
# external access.
```

```run-bash
# 4. Install Linux
# Install your lightweight Linux distro to the VM
```

