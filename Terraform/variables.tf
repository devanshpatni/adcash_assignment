variable "region" {
  default = "ap-south-1"
}

variable "cluster_name" {

}

variable "vpc_name" {
  
}

variable "vpc_cidr" {
  default = "10.0.0.0/16"
  
}

variable "eks_version" {
  default = "1.33"
  
}

variable "node_instance_type" {
  default = "t3.medium"
  
}

variable "ecr_name" {

  
}

variable "private_subnet_ids" {
  default = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  type        = list(string)
}

variable "public_subnet_ids" {
  default = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]
  type        = list(string)
}
