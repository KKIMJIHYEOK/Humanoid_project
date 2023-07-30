#!/bin/sh

sudo cp /boot/cmdline.txt /boot/cmdline.txt.bak
sudo cp /boot/cmdline.txt.eth0 /boot/cmdline.txt

sudo cp /etc/network/interfaces /etc/network/interfaces.bak
sudo cp /etc/network/interfaces.eth0 /etc/network/interfaces


