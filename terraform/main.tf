provider "google" {
  credentials = "${file("hitmebaby.json")}"
  project     = "just-advice-242401"
  region      = "asia-southeast1"
  zone        = "asia-southeast1-b"
}
