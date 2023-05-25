# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
import os
import re
from typing import (
    Dict,
    Mapping,
    MutableMapping,
    MutableSequence,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
    cast,
)

from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.exceptions import MutualTLSChannelError  # type: ignore
from google.auth.transport import mtls  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.language_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.cloud.language_v1.types import language_service

from .transports.base import DEFAULT_CLIENT_INFO, LanguageServiceTransport
from .transports.grpc import LanguageServiceGrpcTransport
from .transports.grpc_asyncio import LanguageServiceGrpcAsyncIOTransport
from .transports.rest import LanguageServiceRestTransport


class LanguageServiceClientMeta(type):
    """Metaclass for the LanguageService client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = (
        OrderedDict()
    )  # type: Dict[str, Type[LanguageServiceTransport]]
    _transport_registry["grpc"] = LanguageServiceGrpcTransport
    _transport_registry["grpc_asyncio"] = LanguageServiceGrpcAsyncIOTransport
    _transport_registry["rest"] = LanguageServiceRestTransport

    def get_transport_class(
        cls,
        label: Optional[str] = None,
    ) -> Type[LanguageServiceTransport]:
        """Returns an appropriate transport class.

        Args:
            label: The name of the desired transport. If none is
                provided, then the first transport in the registry is used.

        Returns:
            The transport class to use.
        """
        # If a specific transport is requested, return that one.
        if label:
            return cls._transport_registry[label]

        # No transport is requested; return the default (that is, the first one
        # in the dictionary).
        return next(iter(cls._transport_registry.values()))


class LanguageServiceClient(metaclass=LanguageServiceClientMeta):
    """Provides text analysis operations such as sentiment analysis
    and entity recognition.
    """

    @staticmethod
    def _get_default_mtls_endpoint(api_endpoint):
        """Converts api endpoint to mTLS endpoint.

        Convert "*.sandbox.googleapis.com" and "*.googleapis.com" to
        "*.mtls.sandbox.googleapis.com" and "*.mtls.googleapis.com" respectively.
        Args:
            api_endpoint (Optional[str]): the api endpoint to convert.
        Returns:
            str: converted mTLS api endpoint.
        """
        if not api_endpoint:
            return api_endpoint

        mtls_endpoint_re = re.compile(
            r"(?P<name>[^.]+)(?P<mtls>\.mtls)?(?P<sandbox>\.sandbox)?(?P<googledomain>\.googleapis\.com)?"
        )

        m = mtls_endpoint_re.match(api_endpoint)
        name, mtls, sandbox, googledomain = m.groups()
        if mtls or not googledomain:
            return api_endpoint

        if sandbox:
            return api_endpoint.replace(
                "sandbox.googleapis.com", "mtls.sandbox.googleapis.com"
            )

        return api_endpoint.replace(".googleapis.com", ".mtls.googleapis.com")

    DEFAULT_ENDPOINT = "language.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = _get_default_mtls_endpoint.__func__(  # type: ignore
        DEFAULT_ENDPOINT
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            LanguageServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_info(info)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            LanguageServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> LanguageServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            LanguageServiceTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def common_billing_account_path(
        billing_account: str,
    ) -> str:
        """Returns a fully-qualified billing_account string."""
        return "billingAccounts/{billing_account}".format(
            billing_account=billing_account,
        )

    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str, str]:
        """Parse a billing_account path into its component segments."""
        m = re.match(r"^billingAccounts/(?P<billing_account>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_folder_path(
        folder: str,
    ) -> str:
        """Returns a fully-qualified folder string."""
        return "folders/{folder}".format(
            folder=folder,
        )

    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str, str]:
        """Parse a folder path into its component segments."""
        m = re.match(r"^folders/(?P<folder>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_organization_path(
        organization: str,
    ) -> str:
        """Returns a fully-qualified organization string."""
        return "organizations/{organization}".format(
            organization=organization,
        )

    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str, str]:
        """Parse a organization path into its component segments."""
        m = re.match(r"^organizations/(?P<organization>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_project_path(
        project: str,
    ) -> str:
        """Returns a fully-qualified project string."""
        return "projects/{project}".format(
            project=project,
        )

    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str, str]:
        """Parse a project path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_location_path(
        project: str,
        location: str,
    ) -> str:
        """Returns a fully-qualified location string."""
        return "projects/{project}/locations/{location}".format(
            project=project,
            location=location,
        )

    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str, str]:
        """Parse a location path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)$", path)
        return m.groupdict() if m else {}

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[client_options_lib.ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variable is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        if client_options is None:
            client_options = client_options_lib.ClientOptions()
        use_client_cert = os.getenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false")
        use_mtls_endpoint = os.getenv("GOOGLE_API_USE_MTLS_ENDPOINT", "auto")
        if use_client_cert not in ("true", "false"):
            raise ValueError(
                "Environment variable `GOOGLE_API_USE_CLIENT_CERTIFICATE` must be either `true` or `false`"
            )
        if use_mtls_endpoint not in ("auto", "never", "always"):
            raise MutualTLSChannelError(
                "Environment variable `GOOGLE_API_USE_MTLS_ENDPOINT` must be `never`, `auto` or `always`"
            )

        # Figure out the client cert source to use.
        client_cert_source = None
        if use_client_cert == "true":
            if client_options.client_cert_source:
                client_cert_source = client_options.client_cert_source
            elif mtls.has_default_client_cert_source():
                client_cert_source = mtls.default_client_cert_source()

        # Figure out which api endpoint to use.
        if client_options.api_endpoint is not None:
            api_endpoint = client_options.api_endpoint
        elif use_mtls_endpoint == "always" or (
            use_mtls_endpoint == "auto" and client_cert_source
        ):
            api_endpoint = cls.DEFAULT_MTLS_ENDPOINT
        else:
            api_endpoint = cls.DEFAULT_ENDPOINT

        return api_endpoint, client_cert_source

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[Union[str, LanguageServiceTransport]] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the language service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, LanguageServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]): Custom options for the
                client. It won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        if isinstance(client_options, dict):
            client_options = client_options_lib.from_dict(client_options)
        if client_options is None:
            client_options = client_options_lib.ClientOptions()
        client_options = cast(client_options_lib.ClientOptions, client_options)

        api_endpoint, client_cert_source_func = self.get_mtls_endpoint_and_cert_source(
            client_options
        )

        api_key_value = getattr(client_options, "api_key", None)
        if api_key_value and credentials:
            raise ValueError(
                "client_options.api_key and credentials are mutually exclusive"
            )

        # Save or instantiate the transport.
        # Ordinarily, we provide the transport, but allowing a custom transport
        # instance provides an extensibility point for unusual situations.
        if isinstance(transport, LanguageServiceTransport):
            # transport is a LanguageServiceTransport instance.
            if credentials or client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes "
                    "directly."
                )
            self._transport = transport
        else:
            import google.auth._default  # type: ignore

            if api_key_value and hasattr(
                google.auth._default, "get_api_key_credentials"
            ):
                credentials = google.auth._default.get_api_key_credentials(
                    api_key_value
                )

            Transport = type(self).get_transport_class(transport)
            self._transport = Transport(
                credentials=credentials,
                credentials_file=client_options.credentials_file,
                host=api_endpoint,
                scopes=client_options.scopes,
                client_cert_source_for_mtls=client_cert_source_func,
                quota_project_id=client_options.quota_project_id,
                client_info=client_info,
                always_use_jwt_access=True,
                api_audience=client_options.api_audience,
            )

    def analyze_sentiment(
        self,
        request: Optional[Union[language_service.AnalyzeSentimentRequest, dict]] = None,
        *,
        document: Optional[language_service.Document] = None,
        encoding_type: Optional[language_service.EncodingType] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> language_service.AnalyzeSentimentResponse:
        r"""Analyzes the sentiment of the provided text.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import language_v1

            def sample_analyze_sentiment():
                # Create a client
                client = language_v1.LanguageServiceClient()

                # Initialize request argument(s)
                document = language_v1.Document()
                document.content = "content_value"

                request = language_v1.AnalyzeSentimentRequest(
                    document=document,
                )

                # Make the request
                response = client.analyze_sentiment(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.language_v1.types.AnalyzeSentimentRequest, dict]):
                The request object. The sentiment analysis request
                message.
            document (google.cloud.language_v1.types.Document):
                Required. Input document.
                This corresponds to the ``document`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            encoding_type (google.cloud.language_v1.types.EncodingType):
                The encoding type used by the API to
                calculate sentence offsets.

                This corresponds to the ``encoding_type`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.language_v1.types.AnalyzeSentimentResponse:
                The sentiment analysis response
                message.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([document, encoding_type])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a language_service.AnalyzeSentimentRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, language_service.AnalyzeSentimentRequest):
            request = language_service.AnalyzeSentimentRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if document is not None:
                request.document = document
            if encoding_type is not None:
                request.encoding_type = encoding_type

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.analyze_sentiment]

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def analyze_entities(
        self,
        request: Optional[Union[language_service.AnalyzeEntitiesRequest, dict]] = None,
        *,
        document: Optional[language_service.Document] = None,
        encoding_type: Optional[language_service.EncodingType] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> language_service.AnalyzeEntitiesResponse:
        r"""Finds named entities (currently proper names and
        common nouns) in the text along with entity types,
        salience, mentions for each entity, and other
        properties.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import language_v1

            def sample_analyze_entities():
                # Create a client
                client = language_v1.LanguageServiceClient()

                # Initialize request argument(s)
                document = language_v1.Document()
                document.content = "content_value"

                request = language_v1.AnalyzeEntitiesRequest(
                    document=document,
                )

                # Make the request
                response = client.analyze_entities(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.language_v1.types.AnalyzeEntitiesRequest, dict]):
                The request object. The entity analysis request message.
            document (google.cloud.language_v1.types.Document):
                Required. Input document.
                This corresponds to the ``document`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            encoding_type (google.cloud.language_v1.types.EncodingType):
                The encoding type used by the API to
                calculate offsets.

                This corresponds to the ``encoding_type`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.language_v1.types.AnalyzeEntitiesResponse:
                The entity analysis response message.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([document, encoding_type])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a language_service.AnalyzeEntitiesRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, language_service.AnalyzeEntitiesRequest):
            request = language_service.AnalyzeEntitiesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if document is not None:
                request.document = document
            if encoding_type is not None:
                request.encoding_type = encoding_type

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.analyze_entities]

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def analyze_entity_sentiment(
        self,
        request: Optional[
            Union[language_service.AnalyzeEntitySentimentRequest, dict]
        ] = None,
        *,
        document: Optional[language_service.Document] = None,
        encoding_type: Optional[language_service.EncodingType] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> language_service.AnalyzeEntitySentimentResponse:
        r"""Finds entities, similar to
        [AnalyzeEntities][google.cloud.language.v1.LanguageService.AnalyzeEntities]
        in the text and analyzes sentiment associated with each entity
        and its mentions.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import language_v1

            def sample_analyze_entity_sentiment():
                # Create a client
                client = language_v1.LanguageServiceClient()

                # Initialize request argument(s)
                document = language_v1.Document()
                document.content = "content_value"

                request = language_v1.AnalyzeEntitySentimentRequest(
                    document=document,
                )

                # Make the request
                response = client.analyze_entity_sentiment(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.language_v1.types.AnalyzeEntitySentimentRequest, dict]):
                The request object. The entity-level sentiment analysis
                request message.
            document (google.cloud.language_v1.types.Document):
                Required. Input document.
                This corresponds to the ``document`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            encoding_type (google.cloud.language_v1.types.EncodingType):
                The encoding type used by the API to
                calculate offsets.

                This corresponds to the ``encoding_type`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.language_v1.types.AnalyzeEntitySentimentResponse:
                The entity-level sentiment analysis
                response message.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([document, encoding_type])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a language_service.AnalyzeEntitySentimentRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, language_service.AnalyzeEntitySentimentRequest):
            request = language_service.AnalyzeEntitySentimentRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if document is not None:
                request.document = document
            if encoding_type is not None:
                request.encoding_type = encoding_type

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.analyze_entity_sentiment]

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def analyze_syntax(
        self,
        request: Optional[Union[language_service.AnalyzeSyntaxRequest, dict]] = None,
        *,
        document: Optional[language_service.Document] = None,
        encoding_type: Optional[language_service.EncodingType] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> language_service.AnalyzeSyntaxResponse:
        r"""Analyzes the syntax of the text and provides sentence
        boundaries and tokenization along with part of speech
        tags, dependency trees, and other properties.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import language_v1

            def sample_analyze_syntax():
                # Create a client
                client = language_v1.LanguageServiceClient()

                # Initialize request argument(s)
                document = language_v1.Document()
                document.content = "content_value"

                request = language_v1.AnalyzeSyntaxRequest(
                    document=document,
                )

                # Make the request
                response = client.analyze_syntax(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.language_v1.types.AnalyzeSyntaxRequest, dict]):
                The request object. The syntax analysis request message.
            document (google.cloud.language_v1.types.Document):
                Required. Input document.
                This corresponds to the ``document`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            encoding_type (google.cloud.language_v1.types.EncodingType):
                The encoding type used by the API to
                calculate offsets.

                This corresponds to the ``encoding_type`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.language_v1.types.AnalyzeSyntaxResponse:
                The syntax analysis response message.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([document, encoding_type])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a language_service.AnalyzeSyntaxRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, language_service.AnalyzeSyntaxRequest):
            request = language_service.AnalyzeSyntaxRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if document is not None:
                request.document = document
            if encoding_type is not None:
                request.encoding_type = encoding_type

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.analyze_syntax]

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def classify_text(
        self,
        request: Optional[Union[language_service.ClassifyTextRequest, dict]] = None,
        *,
        document: Optional[language_service.Document] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> language_service.ClassifyTextResponse:
        r"""Classifies a document into categories.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import language_v1

            def sample_classify_text():
                # Create a client
                client = language_v1.LanguageServiceClient()

                # Initialize request argument(s)
                document = language_v1.Document()
                document.content = "content_value"

                request = language_v1.ClassifyTextRequest(
                    document=document,
                )

                # Make the request
                response = client.classify_text(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.language_v1.types.ClassifyTextRequest, dict]):
                The request object. The document classification request
                message.
            document (google.cloud.language_v1.types.Document):
                Required. Input document.
                This corresponds to the ``document`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.language_v1.types.ClassifyTextResponse:
                The document classification response
                message.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([document])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a language_service.ClassifyTextRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, language_service.ClassifyTextRequest):
            request = language_service.ClassifyTextRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if document is not None:
                request.document = document

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.classify_text]

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def moderate_text(
        self,
        request: Optional[Union[language_service.ModerateTextRequest, dict]] = None,
        *,
        document: Optional[language_service.Document] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> language_service.ModerateTextResponse:
        r"""Moderates a document for harmful and sensitive
        categories.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import language_v1

            def sample_moderate_text():
                # Create a client
                client = language_v1.LanguageServiceClient()

                # Initialize request argument(s)
                document = language_v1.Document()
                document.content = "content_value"

                request = language_v1.ModerateTextRequest(
                    document=document,
                )

                # Make the request
                response = client.moderate_text(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.language_v1.types.ModerateTextRequest, dict]):
                The request object. The document moderation request
                message.
            document (google.cloud.language_v1.types.Document):
                Required. Input document.
                This corresponds to the ``document`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.language_v1.types.ModerateTextResponse:
                The document moderation response
                message.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([document])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a language_service.ModerateTextRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, language_service.ModerateTextRequest):
            request = language_service.ModerateTextRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if document is not None:
                request.document = document

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.moderate_text]

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def annotate_text(
        self,
        request: Optional[Union[language_service.AnnotateTextRequest, dict]] = None,
        *,
        document: Optional[language_service.Document] = None,
        features: Optional[language_service.AnnotateTextRequest.Features] = None,
        encoding_type: Optional[language_service.EncodingType] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> language_service.AnnotateTextResponse:
        r"""A convenience method that provides all the features
        that analyzeSentiment, analyzeEntities, and
        analyzeSyntax provide in one call.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import language_v1

            def sample_annotate_text():
                # Create a client
                client = language_v1.LanguageServiceClient()

                # Initialize request argument(s)
                document = language_v1.Document()
                document.content = "content_value"

                request = language_v1.AnnotateTextRequest(
                    document=document,
                )

                # Make the request
                response = client.annotate_text(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.language_v1.types.AnnotateTextRequest, dict]):
                The request object. The request message for the text
                annotation API, which can perform
                multiple analysis types (sentiment,
                entities, and syntax) in one call.
            document (google.cloud.language_v1.types.Document):
                Required. Input document.
                This corresponds to the ``document`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            features (google.cloud.language_v1.types.AnnotateTextRequest.Features):
                Required. The enabled features.
                This corresponds to the ``features`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            encoding_type (google.cloud.language_v1.types.EncodingType):
                The encoding type used by the API to
                calculate offsets.

                This corresponds to the ``encoding_type`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.language_v1.types.AnnotateTextResponse:
                The text annotations response
                message.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([document, features, encoding_type])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a language_service.AnnotateTextRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, language_service.AnnotateTextRequest):
            request = language_service.AnnotateTextRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if document is not None:
                request.document = document
            if features is not None:
                request.features = features
            if encoding_type is not None:
                request.encoding_type = encoding_type

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.annotate_text]

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def __enter__(self) -> "LanguageServiceClient":
        return self

    def __exit__(self, type, value, traceback):
        """Releases underlying transport's resources.

        .. warning::
            ONLY use as a context manager if the transport is NOT shared
            with other clients! Exiting the with block will CLOSE the transport
            and may cause errors in other clients!
        """
        self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)


__all__ = ("LanguageServiceClient",)
