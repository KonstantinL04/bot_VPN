#!/bin/bash
USERNAME=$1
DAYS=$2

cd /etc/openvpn/server/easy-rsa/
sudo -s ./easyrsa --batch --days=$DAYS build-client-full $DAYS$USERNAME nopass

{
    sudo -s cat /etc/openvpn/server/client-common.txt
    echo "<ca>"
    sudo -s cat /etc/openvpn/server/easy-rsa/pki/ca.crt
    echo "</ca>"
    echo "<cert>"
    sudo -s sed -ne '/BEGIN CERTIFICATE/,$ p' /etc/openvpn/server/easy-rsa/pki/issued/$DAYS$USERNAME.crt
    echo "</cert>"
    echo "<key>"
    sudo -s cat /etc/openvpn/server/easy-rsa/pki/private/$DAYS$USERNAME.key
    echo "</key>"
    echo "<tls-crypt>"
    sudo -s sed -ne '/BEGIN OpenVPN Static key/,$ p' /etc/openvpn/server/tc.key
    echo "</tls-crypt>"
} > /root/$DAYS$USERNAME.ovpn

