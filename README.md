# meap #

A small tool for interacting with the macOS 802.1x EAPOLClient

## examples ##

List EAP profiles:

        $ meap list
        
        UUID: 83DA876E-A6BD-4588-84B8-82BAFC410140	Name: EAP Profile	EAP Types: PEAP
        
Show EAP profile detail by uuid:

        $ meap show --uuid 83DA876E-A6BD-4588-84B8-82BAFC410140
        
        UUID:	83DA876E-A6BD-4588-84B8-82BAFC410140
        User Defined Name:	EAP Profile
        Accepted EAP Types:	PEAP
        Associated Configuration Profile Payload UUID:	1b504450-a474-0133-1175-44bcc8f31634
        
OR show the same EAP profile associated with BSD interface:

        $ meap show --iface en0
        
Export EAP profile as XML plist:

        $ meap export --uuid 83DA876E-A6BD-4588-84B8-82BAFC410140
        
        ... plist output ...
        
Associate interface with EAP profile (Ethernet only):

        $ meap associate 83DA876E-A6BD-4588-84B8-82BAFC410140 en1
        
        Successfully assigned profile 83DA876E-A6BD-4588-84B8-82BAFC410140 to interface en1
        
