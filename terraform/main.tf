// Configure the Google Cloud provider
provider "google" {
 credentials = file("CREDENTIALS_FILE.json")
 project     = "hardy-orb-266609"
 region      = "us-west1"
}

// Terraform plugin for creating random ids
resource "random_id" "instance_id" {
 byte_length = 8
}

// A single Google Cloud Engine instance
resource "google_compute_instance" "default" {
 name         = "proyecto-iv-${random_id.instance_id.hex}"
 machine_type = "f1-micro"
 zone         = "us-west1-a"

 boot_disk {
   initialize_params {
     image = "debian-cloud/debian-9" //usamos una imagen de debian la cual es base para nuestro contenedor de desarrollo garantizando la futura compatibilidad
   }

 }

// Instalamos python y pyramid en la maquina, pyramid lo podemos omitir, a futuro lo instalaremos usando puppet
 metadata_startup_script = "sudo apt-get update; sudo apt-get install -yq build-essential python-pip rsync; pip install pyramid"

 network_interface {
   network = "default"

   access_config {
     // Include this section to give the VM an external ip address
   }
 }

 // anadimos nuestro credencial ssh para poder entrar a la instancia remotamente
 metadata = {
 	  ssh-keys = "rafa:${file("~/.ssh/id_rsa.pub")}"
 }

}

// A variable for extracting the external ip of the instance
output "ip" {
       value = "${google_compute_instance.default.network_interface.0.access_config.0.nat_ip}"
}
