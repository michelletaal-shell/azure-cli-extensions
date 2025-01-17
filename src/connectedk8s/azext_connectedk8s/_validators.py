# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import azext_connectedk8s._constants as consts


def example_name_or_id_validator(cmd, namespace):
    # Example of a storage account name or ID validator.
    from azure.cli.core.commands.client_factory import get_subscription_id
    from msrestazure.tools import is_valid_resource_id, resource_id
    if namespace.storage_account:
        if not is_valid_resource_id(namespace.RESOURCE):
            namespace.storage_account = resource_id(
                subscription=get_subscription_id(cmd.cli_ctx),
                resource_group=namespace.resource_group_name,
                namespace='Microsoft.Storage',
                type='storageAccounts',
                name=namespace.storage_account
            )


def override_client_request_id_header(cmd, namespace):
    if namespace.correlation_id is not None:
        cmd.cli_ctx.data['headers'][consts.Client_Request_Id_Header] = namespace.correlation_id
    else:
        cmd.cli_ctx.data['headers'][consts.Client_Request_Id_Header] = consts.Default_Onboarding_Source_Tracking_Guid
