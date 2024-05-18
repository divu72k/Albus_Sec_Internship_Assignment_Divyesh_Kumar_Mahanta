APPROACH:
1st LAB:
- First, I looked at the status of the interface devices. I got the IP of the server i.e. 10.0.0.1, I tried connecting it but failed.
- I went to the switch this time directly, went to the Config tab and tried seeing the config of fastEthernet 0/1, this gave me access to the CLI and I ran the following commands:
  (config)#exit
  #copy running-config startup-config
- These commands helped me recover the running config which is in the primary memory of the switch making it volatile, further when exporting these files I got a file stating all the commands used for setting up the network. One command in particular caught my attention:
  username net privilege 1 password 0 game
  This gave me the username ‘net’ and the password ‘game'

2nd LAB:
- TO see how changes in the switches and see how the MAC addresses is stored.

3rd LAB:
- We check the status of the VLAN. Try to find the issues and do the needful to set the VLAN properly.
- While checking the communication of packets, we see bob and vicer are configured to 2 different VLANs, hence hindering in their communication. To make them work, we switch the VLAN of fastEthernet 0/3 of admin switch to 1 instead of 2 to make it work.

4th LAB:
- Understood the problem in configuring the hostname of the switches and used appropriate commands to fix it.

5th LAB:
- Checked the line status of all the swtiches and used appropriate commands to fix the down status of the lines.

6th LAB:
- Read the config-files of the switches and re-configured the whole network.

7th LAB:
- Reviewed the config files of the switches and fixed the duplex mismatches in the switches using appropriate commands.

8th LAB:
- Read the running-config files of the switches and debug the SSH configuration.

9th LAB:
- Learnt about SSH timeout through: https://community.cisco.com/t5/network-management/ssh-timeout-for-cisco-devices/td-p/2622872
- SSH timeout are the maximum amount of time that an SSH session can remain idle or inactive before it is closed by either the client or the server.
- Solved the lab using appropirate commands.

10th LAB:
- Read the running-configs and recognised trunking and VLAN problems in the lab based on research and reconfigured the switches in the lab.
