import os


def check_distro():

    global distro

    if os.system("ls /bin | grep pacman "):
        print("Distro derivada de Arch")
        distro = "Arch"

    elif os.system("ls /bin | grep apt "):
        print ("Distro derivada de Debian")
        distro = "Debian"

    else:
        print ("Distro linux no reconocida")
        distro = ""

def check_dependencies():

    if os.system("ls /bin | grep git$ "):
        print("Dependencia GIT satisfecha")

    else:
        print ("Dependencia GIT NO satisfecha")
        print ("Instalando.....")
        os.system("sudo pacman -S git --noconfirm")

def login_manager():

    #Install SDDM
    os.system("sudo pacman -S sddm --noconfirm")

    #Install SDDM-Theme
    os.system("git clone https://github.com/surajmandalcell/Elegant-sddm.git")
    os.system("cd Elegant-sddm")
    os.system("./install.sh")

        #Dependencies Theme
    os.system("sudo pacman -S plasma-framework --noconfirm")