# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "sentinel analytics-setting show",
    is_experimental=True,
)
class Show(AAZCommand):
    """Get the Security ML Analytics Settings.
    """

    _aaz_info = {
        "version": "2022-06-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.operationalinsights/workspaces/{}/providers/microsoft.securityinsights/securitymlanalyticssettings/{}", "2022-06-01-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.settings_resource_name = AAZStrArg(
            options=["-n", "--name", "--settings-resource-name"],
            help="Security ML Analytics Settings resource name",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.workspace_name = AAZStrArg(
            options=["-w", "--workspace-name"],
            help="The name of the workspace.",
            required=True,
            is_experimental=True,
            id_part="name",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.SecurityMLAnalyticsSettingsGet(ctx=self.ctx)()

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class SecurityMLAnalyticsSettingsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/providers/Microsoft.SecurityInsights/securityMLAnalyticsSettings/{settingsResourceName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "settingsResourceName", self.ctx.args.settings_resource_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "workspaceName", self.ctx.args.workspace_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-06-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.etag = AAZStrType()
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.kind = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
                flags={"read_only": True},
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
                flags={"read_only": True},
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
                flags={"read_only": True},
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
                flags={"read_only": True},
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
                flags={"read_only": True},
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
                flags={"read_only": True},
            )

            disc_anomaly = cls._schema_on_200.discriminate_by("kind", "Anomaly")
            disc_anomaly.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.discriminate_by("kind", "Anomaly").properties
            properties.anomaly_settings_version = AAZIntType(
                serialized_name="anomalySettingsVersion",
            )
            properties.anomaly_version = AAZStrType(
                serialized_name="anomalyVersion",
                flags={"required": True},
            )
            properties.description = AAZStrType()
            properties.display_name = AAZStrType(
                serialized_name="displayName",
                flags={"required": True},
            )
            properties.enabled = AAZBoolType(
                flags={"required": True},
            )
            properties.frequency = AAZStrType(
                flags={"required": True},
            )
            properties.is_default_settings = AAZBoolType(
                serialized_name="isDefaultSettings",
                flags={"required": True},
            )
            properties.last_modified_utc = AAZStrType(
                serialized_name="lastModifiedUtc",
                flags={"read_only": True},
            )
            properties.required_data_connectors = AAZListType(
                serialized_name="requiredDataConnectors",
            )
            properties.settings_definition_id = AAZStrType(
                serialized_name="settingsDefinitionId",
            )
            properties.settings_status = AAZStrType(
                serialized_name="settingsStatus",
                flags={"required": True},
            )
            properties.tactics = AAZListType()
            properties.techniques = AAZListType()

            required_data_connectors = cls._schema_on_200.discriminate_by("kind", "Anomaly").properties.required_data_connectors
            required_data_connectors.Element = AAZObjectType()

            _element = cls._schema_on_200.discriminate_by("kind", "Anomaly").properties.required_data_connectors.Element
            _element.connector_id = AAZStrType(
                serialized_name="connectorId",
            )
            _element.data_types = AAZListType(
                serialized_name="dataTypes",
            )

            data_types = cls._schema_on_200.discriminate_by("kind", "Anomaly").properties.required_data_connectors.Element.data_types
            data_types.Element = AAZStrType()

            tactics = cls._schema_on_200.discriminate_by("kind", "Anomaly").properties.tactics
            tactics.Element = AAZStrType()

            techniques = cls._schema_on_200.discriminate_by("kind", "Anomaly").properties.techniques
            techniques.Element = AAZStrType()

            return cls._schema_on_200


__all__ = ["Show"]
