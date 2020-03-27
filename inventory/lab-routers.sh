#!/bin/bash


ROUTERS=$(ssh admin@172.20.20.1 "sh ip dhcp bind  | inc 01.*\.08" | cut -d' ' -f 1)
printf "[lab-routers]\n%s" "$ROUTERS" > lab-routers.ini

git add lab-routers.{ini,sh}
git commit -m "Updated lab-routers inventory"
git push -f origin master
