#!/bin/bash


BASEDIR=$(dirname "$0")
cd "$BASEDIR"


get_routers() {
  ROUTERS=$(ssh admin@172.20.20.1 "sh ip dhcp bind  | inc 01.*\.08" | cut -d' ' -f 1)
  printf "[lab_routers]\n%s" "$ROUTERS" > lab-routers.ini
}
  
prep_git() {	
  if git status | grep lab-routers; then
	git add lab-routers.*
  else
     exit
  fi
}

ship_it() { 
  git commit -m "Updated lab-routers inventory"
  git push origin master
}

main() {
  get_routers
  prep_git
  ship_it
}


main
