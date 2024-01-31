base_path = ~/Downloads

vpn:
	sudo openvpn $(base_path)/$(file_name)

machine:
	sh scripts/create_machine.sh $(folder_name)