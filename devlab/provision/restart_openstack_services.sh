#!/bin/bash
# restart openstack service if it is down after VM provision

cloud_type=$(hostname -s | grep "^grizzly\|^icehouse\|^juno" | awk -F"-" '{print $1}')
if [[ $cloud_type == "grizzly" ]]; then
    network_component="quantum"
else
    network_component="neutron"
fi
for service in cinder glance nova $network_component
do
    sudo initctl list | grep $service | grep stop | awk '{print $1}' | xargs -I {} \
        sudo service {} restart
done
