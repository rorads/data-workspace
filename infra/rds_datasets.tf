resource "aws_rds_cluster" "datasets" {
  availability_zones            = "${var.aws_availability_zones}"
  backup_retention_period       = "${var.datasets_rds_cluster_backup_retention_period}"
  cluster_identifier            = "${var.datasets_rds_cluster_cluster_identifier}"
  database_name                 = "${var.datasets_rds_cluster_database_name}"
  db_subnet_group_name          = "${aws_db_subnet_group.datasets.name}"
  engine                        = "aurora-postgresql"
  engine_version                = "10.11"
  master_password               = "${random_string.aws_rds_cluster_instance_datasets_password.result}"
  master_username               = "${var.datasets_rds_cluster_master_username}"
  storage_encrypted             = "${var.datasets_rds_cluster_storage_encryption_enabled}"
  vpc_security_group_ids        = ["${aws_security_group.datasets.id}"]
  skip_final_snapshot           = true
  enabled_cloudwatch_logs_exports = ["postgresql"]

  lifecycle {
    ignore_changes = ["master_password", "engine_version"]
  }
}

resource "aws_rds_cluster_instance" "datasets" {
  cluster_identifier            = "${aws_rds_cluster.datasets.cluster_identifier}"
  db_subnet_group_name          = "${aws_db_subnet_group.datasets.name}"
  engine                        = "aurora-postgresql"
  identifier                    = "${var.datasets_rds_cluster_instance_identifier}"
  instance_class                = "${var.datasets_rds_cluster_instance_class}"
  performance_insights_enabled  = "${var.datasets_rds_cluster_instance_performance_insights_enabled}"
  promotion_tier                = 1
  db_parameter_group_name       = "aurora-postgresql-10-pgaudit-db-parameter-group"

  lifecycle {
    ignore_changes = ["engine_version"]
  }
}

resource "aws_db_subnet_group" "datasets" {
  name       = "${var.prefix}-datasets"
  subnet_ids = "${aws_subnet.datasets.*.id}"

  tags = {
    Name = "${var.prefix}-datasets"
  }
}


resource "random_string" "aws_rds_cluster_instance_datasets_password" {
  length = 64
  special = false

  lifecycle {
    ignore_changes = all
  }
}