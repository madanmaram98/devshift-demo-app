terraform {
  required_version = ">= 1.0"
  # VIOLATION: no remote backend configured — local state only
}

provider "aws" {
  region = "eu-central-1"
  # VIOLATION: provider version not pinned (no required_providers block)
}

resource "aws_db_instance" "app_db" {
  identifier          = "appdb"
  engine              = "postgres"
  instance_class      = "db.t3.micro"
  username            = "admin"
  password            = "Passw0rd123!"   # VIOLATION: hardcoded secret
  skip_final_snapshot = true
  # VIOLATION: storage_encrypted not set to true
  # VIOLATION: publicly_accessible not explicitly false
}

resource "aws_security_group" "web" {
  name = "web-sg"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]   # VIOLATION: SSH open to entire internet
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# VIOLATION: variable has no description
variable "environment" {}
