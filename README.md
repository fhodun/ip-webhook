# ip-webhook

Python script that send ip to Discord webhook. You can run it automatically on system startup. Useful for server on Raspberry Pi.

## usage on ubuntu

1. clone repository  
`git clone https://github.com/fhodun/ip-webhook`
2. put your discord webhook token into [main.py](main.py#L4) file  
`sudo nano ip-webhook/main.py`
3. copy [rc.local](rc.local) to /etc/rc.local  
`sudo cp ip-webhook/rc.local /etc/rc.local`

## solving some problems

- [no rc.local file](https://vpsfix.com/community/server-administration/no-etc-rc-local-file-on-ubuntu-18-04-heres-what-to-do/)
