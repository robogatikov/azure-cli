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
    "monitor activity-log alert show",
)
class Show(AAZCommand):
    """Get an activity log alert.
    """

    _aaz_info = {
        "version": "2017-04-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.insights/activitylogalerts/{}", "2017-04-01"],
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
        _args_schema.activity_log_alert_name = AAZStrArg(
            options=["-n", "--name", "--activity-log-alert-name"],
            help="The name of the activity log alert.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ActivityLogAlertsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ActivityLogAlertsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/activityLogAlerts/{activityLogAlertName}",
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
                    "activityLogAlertName", self.ctx.args.activity_log_alert_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2017-04-01",
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
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.actions = AAZObjectType(
                flags={"required": True},
            )
            properties.condition = AAZObjectType(
                flags={"required": True},
            )
            properties.description = AAZStrType()
            properties.enabled = AAZBoolType()
            properties.scopes = AAZListType(
                flags={"required": True},
            )

            actions = cls._schema_on_200.properties.actions
            actions.action_groups = AAZListType(
                serialized_name="actionGroups",
            )

            action_groups = cls._schema_on_200.properties.actions.action_groups
            action_groups.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.actions.action_groups.Element
            _element.action_group_id = AAZStrType(
                serialized_name="actionGroupId",
                flags={"required": True},
            )
            _element.webhook_properties = AAZDictType(
                serialized_name="webhookProperties",
            )

            webhook_properties = cls._schema_on_200.properties.actions.action_groups.Element.webhook_properties
            webhook_properties.Element = AAZStrType()

            condition = cls._schema_on_200.properties.condition
            condition.all_of = AAZListType(
                serialized_name="allOf",
                flags={"required": True},
            )

            all_of = cls._schema_on_200.properties.condition.all_of
            all_of.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.condition.all_of.Element
            _element.equals = AAZStrType(
                flags={"required": True},
            )
            _element.field = AAZStrType(
                flags={"required": True},
            )

            scopes = cls._schema_on_200.properties.scopes
            scopes.Element = AAZStrType()

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""


__all__ = ["Show"]
