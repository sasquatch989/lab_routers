#!/bin/bash
#Adding comment line

BASEDIR=$(dirname "$0")
cd "$BASEDIR"


get_routers() {
  ROUTERS=$(ssh admin@172.20.20.1 "sh ip dhcp bind  | inc 01.*\.08" | cut -d' ' -f 1)
  printf "[lab_routers]\n%s" "$ROUTERS ansible_network_os=ios" > ../lab-routers.ini
}
  
prep_git() {
  git checkout inventory
  if git status | grep 'lab-routers.ini'; then
	  git add lab-routers.ini
	  ship_it
  else
     exit 0
  fi
}

ship_it() { 
  git commit -m "Updated lab-routers inventory $(date)"
  git pull origin inventory --rebase
  git push origin inventory
}

main() {
  get_routers
  prep_git
}


main
