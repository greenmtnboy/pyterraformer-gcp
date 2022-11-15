terraform {
  backend "local" {

  }
  required_providers {
    build = {
      source  = "hashicorp/google"
      version = "3.72.0"
    }
  }
}

