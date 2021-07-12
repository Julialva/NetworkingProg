from ncclient import manager

IOS_HOST = "INSERT IP ADDRESS"
NETCONF_PORT = "830"
USERNAME = "INSERT USER NAME"
PASSWORD = "INSERT PASSWORD"

def get_capabilities():
    with manager.connect(
        host=IOS_HOST,
        port=NETCONF_PORT,
        username=USERNAME,
        password=PASSWORD,
        hostkey_verify=False
        ) as device:
        print("\n***NETCONF Capabilities for device {}***\n".format(IOS_HOST))
        for cap in device.server_capabilities:
            print(cap)
if __name__=="__main__":
    get_capabilities()