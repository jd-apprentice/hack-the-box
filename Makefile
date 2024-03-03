base_path = ~/Downloads
inventory ?= hosts

vpn:
	sudo openvpn $(base_path)/$(file_name)

machine:
	sh scripts/create_machine.sh $(folder_name)

playbook:
	ansible-playbook -i ansible/inventory/$(inventory).conf ansible/playbooks/$(playbook).yml