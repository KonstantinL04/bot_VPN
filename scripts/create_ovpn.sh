#!/bin/bash
USERNAME=$1
DAYS=$1
cd /etc/openvpn/server/easy-rsa/
sudo -s ./easyrsa --batch --days=$DAYS build-client-full $USERNAME nopass

{
    sudo -s cat /etc/openvpn/server/client-common.txt
    echo "<ca>"
    sudo -s cat /etc/openvpn/server/easy-rsa/pki/ca.crt
    echo "</ca>"
    echo "<cert>"
    sudo -s sed -ne '/BEGIN CERTIFICATE/,$ p' /etc/openvpn/server/easy-rsa/pki/issued/$USERNAME.crt
    echo "</cert>"
    echo "<key>"
    sudo -s cat /etc/openvpn/server/easy-rsa/pki/private/$USERNAME.key
    echo "</key>"
    echo "<tls-crypt>"
    sudo -s sed -ne '/BEGIN OpenVPN Static key/,$ p' /etc/openvpn/server/tc.key
    echo "</tls-crypt>"
} > /home/konstantin/$USERNAME.ovpn

