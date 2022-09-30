# Copyright (c) 2020, 2022, Oracle and/or its affiliates.
#
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl/
#

import os

# version
VERSION_TAG = "8.0.31"

MIN_SUPPORTED_VERSION = "8.0.27"
MAX_SUPPORTED_VERSION = "8.0.32"


# image
IMAGE_REGISTRY = os.getenv(
    "OPERATOR_TEST_REGISTRY", default=None)

IMAGE_REPOSITORY = os.getenv(
    "OPERATOR_TEST_REPOSITORY", default="mysql")


# operator
OPERATOR_IMAGE_NAME = os.getenv(
    "OPERATOR_TEST_IMAGE_NAME", default="mysql-operator")

OPERATOR_EE_IMAGE_NAME = os.getenv(
    "OPERATOR_TEST_EE_IMAGE_NAME", default="enterprise-operator")

OPERATOR_VERSION_TAG = os.getenv(
    "OPERATOR_TEST_VERSION_TAG", default="8.0.32-2.0.8")

OPERATOR_PULL_POLICY = os.getenv(
    "OPERATOR_TEST_PULL_POLICY", default="IfNotPresent")


# server
SERVER_VERSION_TAG = VERSION_TAG
SERVER_IMAGE_NAME = "mysql-server"
SERVER_EE_IMAGE_NAME = "enterprise-server"


# router
ROUTER_VERSION_TAG = VERSION_TAG
ROUTER_IMAGE_NAME = "mysql-router"
ROUTER_EE_IMAGE_NAME = "enterprise-router"


# enterprise
ENTERPRISE_SKIP = os.getenv(
    "OPERATOR_TEST_SKIP_ENTERPRISE", default=False)


# oci
OCI_SKIP = os.getenv(
    "OPERATOR_TEST_SKIP_OCI", default=False)

OCI_CONFIG_PATH = os.getenv(
    "OPERATOR_TEST_OCI_CONFIG_PATH", default=None)

OCI_BUCKET_NAME = os.getenv(
    "OPERATOR_TEST_OCI_BUCKET", default=None)

OCI_VAULT_CONFIG_PATH = os.getenv(
    "OPERATOR_TEST_VAULT_CONFIG_PATH", default=None)


# k8s
K8S_CLUSTER_NAME = os.getenv(
    "OPERATOR_TEST_K8S_CLUSTER_NAME", default="ote-mysql")
