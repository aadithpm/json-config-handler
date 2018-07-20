import datetime
import os
import json

# Config filename
config_file = "config.json"

backup_filename = 'config_' + str(datetime.datetime.today()).replace('-', '')[:8] + '.json'

# Load file in read-only
def load_json_r():
    return open(config_file, 'r')

# Load file to write
def load_json_w():
    return open(config_file, 'w')

# Backup script
def backup_config():

    try:
        backup_f = open(backup_filename, 'w')
        f = load_json_r()
        data = json.load(f)
        json.dump(data, backup_f)


    except FileNotFoundError:
        print("Unable to backup config file")
        return False

    return True

# Get entry if it exists in file
def get_entry(c_key):

    if backup_config():
        print("[{}] Backup successful".format(str(datetime.datetime.today())[:10]))

    else:
        print("WARNING: Backup wasn't made")

    json_file = load_json_r()
    data = json.load(json_file)
    json_file.close()
    try:
        return data[c_key]

    except KeyError:
        print("[ERROR] KeyError: Key does not exist in configuration")
        return None

# Change entry in file
def change_entry(c_key, value):

    if backup_config():
        print("[{}] Backup successful".format(str(datetime.datetime.today())[:10]))

    else:
        print("WARNING: Backup wasn't made")

    json_file = load_json_r()
    data = json.load(json_file)
    json_file.close()
    json_file = load_json_w()
    #
    try:
        print("[CONFIG] Writing {}:{} to config file".format(c_key, value))
        data[c_key] = value
        json.dump(data, json_file)
        return True

    except: # Generic exception
        print("[ERROR] Could not write to config file")
        return False
