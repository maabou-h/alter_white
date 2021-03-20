#!/bin/sh

sudo iptables -F
sudo /etc/init.d/networking restart
