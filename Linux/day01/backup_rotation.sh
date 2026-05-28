#!/bin/bash


<<readme

Create funtions for system information

readme


function display_usage(){
    echo "Usage: ./backup_rotation.sh <path to your source> <path to backup folder>"
    exit 1
}

if [ $# -eq 0 ]; then
    display_usage
fi


source_dir=$1
time_stamp=$(date "+%Y-%m-%d-%H-%M-%S")
backup_dir=$2

function create_backup(){
    zip -r "${backup_dir}/backup_${time_stamp}.zip" "${source_dir}" 2&>/dev/null
    if [ $? -eq 0 ]; then
     echo "backup generated successfully..."
    fi
}
create_backup

function backup_rotation(){
    backups=($(ls -t "${backup_dir}/backup_"*.zip))
    if [ "${#backups[@]}" -gt 2 ]; then
        echo "Performing roation for 5 days ."
        backups_to_remove=("${backups[@]:2}")
        for backup in "${backups_to_remove[@]}"
        do 
            rm -f "${backup}"
        done
    fi
 
}
backup_rotation