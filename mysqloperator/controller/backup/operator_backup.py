# Copyright (c) 2020, Oracle and/or its affiliates.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License, version 2.0,
# as published by the Free Software Foundation.
#
# This program is also distributed with certain software (including
# but not limited to OpenSSL) that is licensed under separate terms, as
# designated in a particular file or component or in included license
# documentation.  The authors of MySQL hereby grant you an additional
# permission to link the program and your derivative works with the
# separately licensed software that they have included with MySQL.
# This program is distributed in the hope that it will be useful,  but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See
# the GNU General Public License, version 2.0, for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA


from .. import consts, kubeutils, config, utils
from ..kubeutils import api_core, api_batch
from ..innodbcluster.cluster_api import InnoDBCluster
from .backup_api import MySQLBackup
from . import backup_objects
import kopf
from logging import Logger


@kopf.on.create(consts.GROUP, consts.VERSION, consts.MYSQLBACKUP_PLURAL)
def on_mysqlbackup_create(name: str, namespace: str, spec: dict, body: dict, logger: Logger, **kwargs):
    logger.info(
        f"Initializing MySQL Backup job name={name} namespace={namespace}")

    backup = MySQLBackup(body)

    jobname = name+"-"+utils.timestamp()

    job = backup_objects.prepare_backup_job(jobname, backup.parsed_spec)

    kopf.adopt(job)

    api_batch.create_namespaced_job(namespace, body=job)

    # Copy the backup profile contents to the backup object
    # TODO


# TODO create a job to delete the data when the job is deleted
