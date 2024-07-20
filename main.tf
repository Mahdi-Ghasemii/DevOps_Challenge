terraform {
    required_providers {
      virtualbox = {
        source = "shekeriev/virtualbox"
        version = "0.0.4"
      }
    }
}

resource "virtualbox_vm" "node"{
    count = 2
    name = "${format("node-%02d")}"
    image = "ubuntu-20.04"
    cpus = 2
    memory = 4096
    status = running

    network_adapter{
        type = "bridged"
        host_interface = "ens0: Wi-Fi-Mahdi "
    }
}