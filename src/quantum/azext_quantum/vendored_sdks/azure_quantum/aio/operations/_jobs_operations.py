# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, List, Optional, TypeVar

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
# from azure.core.utils import case_insensitive_dict    <--- Restore this line after Azure CLI version 2.38.0 is released
from ...._utils import case_insensitive_dict

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._jobs_operations import build_cancel_request, build_create_request, build_get_request, build_list_request, build_patch_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class JobsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.quantum._client.aio.QuantumClient`'s
        :attr:`jobs` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")


    @distributed_trace
    def list(
        self,
        **kwargs: Any
    ) -> AsyncIterable[_models.JobDetailsList]:
        """List jobs.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either JobDetailsList or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.quantum._client.models.JobDetailsList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop('cls', None)  # type: ClsType[_models.JobDetailsList]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=self._config.resource_group_name,
                    workspace_name=self._config.workspace_name,
                    template_url=self.list.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=self._config.resource_group_name,
                    workspace_name=self._config.workspace_name,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("JobDetailsList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': "/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Quantum/workspaces/{workspaceName}/jobs"}  # type: ignore

    @distributed_trace_async
    async def get(
        self,
        job_id: str,
        **kwargs: Any
    ) -> _models.JobDetails:
        """Get job by id.

        :param job_id: Id of the job.
        :type job_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JobDetails, or the result of cls(response)
        :rtype: ~azure.quantum._client.models.JobDetails
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop('cls', None)  # type: ClsType[_models.JobDetails]

        
        request = build_get_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=self._config.resource_group_name,
            workspace_name=self._config.workspace_name,
            job_id=job_id,
            template_url=self.get.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.RestError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('JobDetails', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Quantum/workspaces/{workspaceName}/jobs/{jobId}"}  # type: ignore


    @distributed_trace_async
    async def create(
        self,
        job_id: str,
        job: _models.JobDetails,
        **kwargs: Any
    ) -> _models.JobDetails:
        """Create a job.

        :param job_id: Id of the job.
        :type job_id: str
        :param job: The complete metadata of the job to submit.
        :type job: ~azure.quantum._client.models.JobDetails
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JobDetails, or the result of cls(response)
        :rtype: ~azure.quantum._client.models.JobDetails
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', "application/json"))  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.JobDetails]

        _json = self._serialize.body(job, 'JobDetails')

        request = build_create_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=self._config.resource_group_name,
            workspace_name=self._config.workspace_name,
            job_id=job_id,
            content_type=content_type,
            json=_json,
            template_url=self.create.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.RestError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if response.status_code == 200:
            deserialized = self._deserialize('JobDetails', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('JobDetails', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create.metadata = {'url': "/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Quantum/workspaces/{workspaceName}/jobs/{jobId}"}  # type: ignore


    @distributed_trace_async
    async def cancel(  # pylint: disable=inconsistent-return-statements
        self,
        job_id: str,
        **kwargs: Any
    ) -> None:
        """Cancel a job.

        :param job_id: Id of the job.
        :type job_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop('cls', None)  # type: ClsType[None]

        
        request = build_cancel_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=self._config.resource_group_name,
            workspace_name=self._config.workspace_name,
            job_id=job_id,
            template_url=self.cancel.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.RestError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    cancel.metadata = {'url': "/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Quantum/workspaces/{workspaceName}/jobs/{jobId}"}  # type: ignore


    @distributed_trace_async
    async def patch(
        self,
        job_id: str,
        patch_job: List[_models.JsonPatchDocument],
        **kwargs: Any
    ) -> Optional[_models.JobDetails]:
        """Patch a job.

        :param job_id: Id of the job.
        :type job_id: str
        :param patch_job: The json patch document containing the patch operations.
        :type patch_job: list[~azure.quantum._client.models.JsonPatchDocument]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JobDetails, or the result of cls(response)
        :rtype: ~azure.quantum._client.models.JobDetails or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', "application/json"))  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional[_models.JobDetails]]

        _json = self._serialize.body(patch_job, '[JsonPatchDocument]')

        request = build_patch_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=self._config.resource_group_name,
            workspace_name=self._config.workspace_name,
            job_id=job_id,
            content_type=content_type,
            json=_json,
            template_url=self.patch.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.RestError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('JobDetails', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    patch.metadata = {'url': "/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Quantum/workspaces/{workspaceName}/jobs/{jobId}"}  # type: ignore

