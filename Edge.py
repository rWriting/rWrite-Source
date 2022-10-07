# rWrite Script 2.0
# Device : Redmi Note 6 Pro
# Author : @XelXen

# Config Script
import rWrite
from ppadb.client import Client as AdbClient
from requests import get as req
from shutil import unpack_archive as unzip, rmtree
from subprocess import check_output, Popen as nullrun, DEVNULL
from sys import path, platform
from time import sleep as wait
from os import remove, path as ospath, chdir as cd, environ, mkdir, system as run

print(" ")
print(" LAUNCHING...")


if platform == "win32" or platform == "win64":
    directory = ospath.join(ospath.join(
        environ['USERPROFILE']), 'rWriteConfig')

    nullrun(
        ['taskkill', "/IM", "adb.exe", "/F"],
        stdout=DEVNULL,
        stderr=DEVNULL,
    )

elif platform == "linux" or platform == "linux2":
    directory = ospath.join(environ['HOME'], '.rWriteConfig')
    from os import popen, kill
    from signal import SIGKILL

    def check_kill_process(pstring):
        for line in popen("ps ax | grep " + pstring + " | grep -v grep"):
            fields = line.split()
            pid = fields[0]
            kill(int(pid), SIGKILL)

    check_kill_process("adb")

elif platform == "darwin":
    directory = ospath.join(environ['HOME'], '.rWriteConfig')
    from os import popen, kill
    from signal import SIGKILL

    def check_kill_process(pstring):
        for line in popen("ps ax | grep " + pstring + " | grep -v grep"):
            fields = line.split()
            pid = fields[0]
            kill(int(pid), SIGKILL)

    check_kill_process("adb")

else:
    print(' ')
    print(" UNKNOWN PLATFORM")
    wait(5)
    exit()

wait(1)

if ospath.exists(directory) is True:
    rmtree(directory)
    mkdir(directory)
    cd(directory)
elif ospath.exists(directory) is False:
    mkdir(directory)
    cd(directory)
else:
    exit()

path.append(directory)

nullrun(
    ['pip3', "install", "requests", "pure-python-adb"],
    stdout=DEVNULL,
    stderr=DEVNULL,
)
wait(1)


file_url = "https://raw.githubusercontent.com/rWriting/rWrite-Source/main/rWrite.py"
r = req(file_url, stream=True)
with open(directory + "/rWrite.py", "wb") as configfile:
    for chunk in r.iter_content(chunk_size=128):
        if chunk:
            configfile.write(chunk)


def rWriteBanner():
    print('         __      __         __  __           ')
    print(' _______/  \    /  \_______|__|/  |_  ____   ')
    print(' \_  __ \   \/\/   /\_  __ \  \   __\/ __ \  ')
    print('  |  | \/\        /  |  | \/  ||  | \  ___/  ')
    print('  |__|    \__/\__/   |__|  |__||__|  \_____> ')
    print(' ')


if platform == "win32" or platform == "win64":
    file_url = "https://gdmbd.sasohan.workers.dev/minimal_adb_fastboot_1.4.3_portable.zip"
    r = req(file_url, stream=True)
    with open(directory + "/minimal.zip", "wb") as zipfile:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                zipfile.write(chunk)

    nullrun(
        ['attrib', "+H", directory],
        stdout=DEVNULL,
        stderr=DEVNULL,
    )

    filename = directory + "/minimal.zip"
    extract_dir = directory + "/minimal"

    unzip(filename, extract_dir)
    remove(filename)
    cd(directory + "/minimal")

    nullrun(
        ['adb.exe', "start-server"],
        stdout=DEVNULL,
        stderr=DEVNULL,
    )
    run('cls')

elif platform == "linux" or platform == "linux2":
    file_url = "https://dl.google.com/android/repository/platform-tools-latest-linux.zip"
    r = req(file_url, stream=True)
    with open(directory + "/minimal.zip", "wb") as zipfile:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                zipfile.write(chunk)

    filename = directory + "/minimal.zip"
    extract_dir = directory + "/minimal"

    unzip(filename, extract_dir)
    remove(filename)
    cd(directory + "/minimal/platform-tools")

    run('chmod 755 *')
    nullrun(
        ['./adb', "start-server"],
        stdout=DEVNULL,
        stderr=DEVNULL,
    )
    run('clear')

elif platform == "darwin":
    file_url = "https://dl.google.com/android/repository/platform-tools-latest-darwin.zip"
    r = req(file_url, stream=True)
    with open(directory + "/minimal.zip", "wb") as zipfile:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                zipfile.write(chunk)

    filename = directory + "/minimal.zip"
    extract_dir = directory + "/minimal"

    unzip(filename, extract_dir)
    remove(filename)
    cd(directory + "/minimal/platform-tools")

    run('chmod 755 *')
    nullrun(
        ['./adb', "start-server"],
        stdout=DEVNULL,
        stderr=DEVNULL,
    )
    run('clear')

else:
    print(" ")
    print(" UNKNOWN PLATFORM")
    wait(5)
    exit()

if platform == "win32" or platform == "win64":
    def midscript():
        run('cls')
        rWriteBanner()
        print(' STARTING THE SCRIPT IN 10 SECONDS.....')
        print(' ')
        print(' PRESS CTRL + C TO EXIT')
        print(' ')
        print(' WARNING! DO NOT USE THIS DEVICE WHILE THE SCRIPT WILL BE RUNNING')
        wait(9)
        print(' ')
        print(' STARTING THE RWRITE SCRIPT...')
        wait(1)
        run('cls')
        rWriteBanner()
        print(' CONNECT YOUR PHONE TO THIS DEVICE')
        print(' ')
        print(' WAITING FOR DEVICE....')
        while True:
            device = 0
            client = AdbClient(host="127.0.0.1", port=5037)
            devices = client.devices()
            if len(devices) != 0:
                wait(1)
                run('adb.exe devices > devices.txt')
                f = open("devices.txt", "r")
                errorcheck = f.read()
                errorcode = "no permission"
                if errorcode in errorcheck:
                    print(' ')
                    print(' ERROR : NO PERMISSION')
                    print(' ')
                    print(' PLEASE ENABLE FILE TRANSFER MODE IN YOUR PHONE')
                    print(' ')
                    while True:
                        wait(1)
                        run('adb devices > devices.txt')
                        f = open("devices.txt", "r")
                        errorcheck = f.read()
                        if errorcode not in errorcheck:
                            print(' OPERATION PERMITTED')
                            break

                wait(1)
                run('adb.exe devices > devices.txt')
                f = open("devices.txt", "r")
                errorcheck = f.read()
                errorcode = "unauthorized"
                if errorcode in errorcheck:
                    print(' ')
                    print(' ERROR : UNAUTHORIZED')
                    print(' ')
                    print(
                        ' PLEASE ENABLE USB DEBUGGING FROM THIS COMPUTER IN YOUR PHONE')
                    print(' ')
                    while True:
                        wait(1)
                        run('adb devices > devices.txt')
                        f = open("devices.txt", "r")
                        errorcheck = f.read()
                        if errorcode not in errorcheck:
                            print(' OPERATION PERMITTED')
                            break

                print(' ')
                print(' REBOOTING....')
                run('adb.exe reboot recovery')
                print(' ')
                wait(1)
                break
            wait(2)

        nullrun(
            ['adb.exe', "kill-server"],
            stdout=DEVNULL,
            stderr=DEVNULL,
        )
        wait(1)

        nullrun(
            ['adb.exe', "start-server"],
            stdout=DEVNULL,
            stderr=DEVNULL,
        )
        wait(1)

        print(' WAITING FOR RECOVERY....')
        while True:
            device = 0
            client = AdbClient(host="127.0.0.1", port=5037)
            devices = client.devices()
            if len(devices) != 0:
                print(' ')
                print(' CONNECTING TO SHELL....')
                wait(1)
                break
            wait(2)

        def connect():
            client = AdbClient(host="127.0.0.1", port=5037)
            devices = client.devices()
            if len(devices) == 0:
                print('No devices')
                quit()
            device = devices[0]
            print(f'Connected to {device}')
            print(' ')
            return device, client

        run('cls')
        rWriteBanner()
        print(' DEVICE CONNECTED SUCCESSFULLY')
        print(' ')
        print(' PARTITIONING....')
        wait(1)
        if __name__ == '__main__':
            device, client = connect()
            device.shell('umount -a')

elif platform == "linux" or platform == "linux2" or platform == "darwin":
    def midscript():
        run('clear')
        rWriteBanner()
        print(' Starting the script in 10 seconds.....')
        print(' ')
        print(' Press CTRL + C to exit')
        print(' ')
        print(' WARNING! DO NOT USE THIS DEVICE WHILE THE SCRIPT WILL BE RUNNING')
        wait(9)
        print(' ')
        print(' STARTING THE RWRITE SCRIPT...')
        wait(1)
        run('clear')
        rWriteBanner()
        print(' CONNECT YOUR PHONE TO THIS DEVICE')
        print(' ')
        print(' WAITING FOR DEVICE....')
        while True:
            device = 0
            client = AdbClient(host="127.0.0.1", port=5037)
            devices = client.devices()
            if len(devices) != 0:
                wait(1)
                run('./adb devices > devices.txt')
                f = open("devices.txt", "r")
                errorcheck = f.read()
                errorcode = "no permission"
                if errorcode in errorcheck:
                    print(' ')
                    print(' ERROR : NO PERMISSION')
                    print(' ')
                    print(' PLEASE ENABLE FILE TRANSFER MODE IN YOUR PHONE')
                    print(' ')
                    while True:
                        wait(1)
                        run('./adb devices > devices.txt')
                        f = open("devices.txt", "r")
                        errorcheck = f.read()
                        if errorcode not in errorcheck:
                            print(' OPERATION PERMITTED')
                            break

                wait(1)
                run('./adb devices > devices.txt')
                f = open("devices.txt", "r")
                errorcheck = f.read()
                errorcode = "unauthorized"
                if errorcode in errorcheck:
                    print(' ')
                    print(' ERROR : UNAUTHORIZED')
                    print(' ')
                    print(
                        ' PLEASE ENABLE USB DEBUGGING FROM THIS COMPUTER IN YOUR PHONE')
                    print(' ')
                    while True:
                        wait(1)
                        run('./adb devices > devices.txt')
                        f = open("devices.txt", "r")
                        errorcheck = f.read()
                        if errorcode not in errorcheck:
                            print(' OPERATION PERMITTED')
                            break

                print(' ')
                print(' REBOOTING....')
                run('./adb reboot recovery')
                print(' ')
                wait(1)
                break
            wait(2)

        nullrun(
            ['./adb', "kill-server"],
            stdout=DEVNULL,
            stderr=DEVNULL,
        )
        wait(1)

        nullrun(
            ['./adb', "start-server"],
            stdout=DEVNULL,
            stderr=DEVNULL,
        )
        wait(1)

        print(' WAITING FOR RECOVERY....')
        while True:
            device = 0
            client = AdbClient(host="127.0.0.1", port=5037)
            devices = client.devices()
            if len(devices) != 0:
                print(' ')
                print(' CONNECTING TO SHELL....')
                wait(1)
                break
            wait(2)

        def connect():
            client = AdbClient(host="127.0.0.1", port=5037)
            devices = client.devices()
            if len(devices) == 0:
                print(' ')
                print(' A CRITICAL ERROR OCCURED')
                wait(5)
                quit()
            device = devices[0]
            return device, client

        run('clear')
        rWriteBanner()
        print(' DEVICE CONNECTED SUCCESSFULLY')
        print(' ')
        print(' PARTITIONING....')
        wait(1)
        if __name__ == '__main__':
            device, client = connect()
            device.shell('umount -a')

# Execute Script

rWriteBanner()

if rWrite.part1 is True or rWrite.part1 == "True":
    part1_size = input(f' {rWrite.part1_name.upper()} SIZE [GB] :')
    if part1_size.isalpha() is False:
        part1_size = int(part1_size) * 1024
        if part1_size < rWrite.min_part1_size or part1_size > rWrite.max_part1_size:
            print(" ")
            print(f" {rWrite.part1_name.upper()} SIZE CAN BE SET BETWEEN {rWrite.min_part1_size} AND {rWrite.max_part1_size} GB ONLY")
            wait(5)
            quit()
        elif part1_size <= rWrite.max_part1_size and part1_size >= rWrite.min_part1_size:
            part1_cmd = f'mkpart {rWrite.part1_name} {rWrite.part1_file_system.lower()} {rWrite.before_part1_size} {rWrite.before_part1_size + part1_size}'
        else:
            print(" ")
            print(" ONLY POSITIVE DECIMAL NUMBERS ARE ACCEPTED")
            wait(5)
            quit()
    else:
        print(" ")
        print(" ONLY NUMBERS ARE ACCEPTED")
        wait(5)
        quit()

if rWrite.part2 is True or rWrite.part2 == "True":
    part2_size = input(f' {rWrite.part2_name.upper()} SIZE [GB] :')
    if part2_size.isalpha() is False:
        part2_size = int(part2_size) * 1024
        if part2_size < rWrite.min_part2_size or part2_size > rWrite.max_part2_size:
            print(" ")
            print(f" {rWrite.part2_name.upper()} SIZE CAN BE SET BETWEEN {rWrite.min_part2_size} AND {rWrite.max_part2_size} GB ONLY")
            wait(5)
            quit()
        elif part2_size <= rWrite.max_part2_size and part2_size >= rWrite.min_part2_size:
            part2_cmd = f'mkpart {rWrite.part2_name} {rWrite.part2_file_system.lower()} {rWrite.before_part2_size} {rWrite.before_part2_size + part2_size}'
        else:
            print(" ")
            print(" ONLY POSITIVE DECIMAL NUMBERS ARE ACCEPTED")
            wait(5)
            quit()
    else:
        print(" ")
        print(" ONLY NUMBERS ARE ACCEPTED")
        wait(5)
        quit()

mobile = input(' DEVICE SIZE [32/64] : ')
if mobile == "64":
    userdata_cmd = f"mkpart userdata ext4 {str(int(system_size + vendor_size + cust_size))} 62.5GB"
    midscript()

elif mobile == "32":
    userdata_cmd = f"mkpart userdata ext4 {str(int(system_size + vendor_size + cust_size))} 31.3GB"
    midscript()

else:
    print(' ')
    print(' INVALID INPUT')
    wait(5)
    exit()

rmtree(directory)
