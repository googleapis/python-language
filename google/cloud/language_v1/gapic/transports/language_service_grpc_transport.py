# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import google.api_core.grpc_helpers

from google.cloud.language_v1.proto import language_service_pb2_grpc


class LanguageServiceGrpcTransport(object):
    """gRPC transport class providing stubs for
    google.cloud.language.v1 LanguageService API.

    The transport provides access to the raw gRPC stubs,
    which can be used to take advantage of advanced
    features of gRPC.
    """

    # The scopes needed to make gRPC calls to all of the methods defined
    # in this service.
    _OAUTH_SCOPES = (
        "https://www.googleapis.com/auth/cloud-language",
        "https://www.googleapis.com/auth/cloud-platform",
    )

    def __init__(
        self, channel=None, credentials=None, address="language.googleapis.com:443"
    ):
        """Instantiate the transport class.

        Args:
            channel (grpc.Channel): A ``Channel`` instance through
                which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            address (str): The address where the service is hosted.
        """
        # If both `channel` and `credentials` are specified, raise an
        # exception (channels come with credentials baked in already).
        if channel is not None and credentials is not None:
            raise ValueError(
                "The `channel` and `credentials` arguments are mutually " "exclusive."
            )

        # Create the channel.
        if channel is None:
            channel = self.create_channel(
                address=address,
                credentials=credentials,
                options={
                    "grpc.max_send_message_length": -1,
                    "grpc.max_receive_message_length": -1,
                }.items(),
            )

        self._channel = channel

        # gRPC uses objects called "stubs" that are bound to the
        # channel and provide a basic method for each RPC.
        self._stubs = {
            "language_service_stub": language_service_pb2_grpc.LanguageServiceStub(
                channel
            )
        }

    @classmethod
    def create_channel(
        cls, address="language.googleapis.com:443", credentials=None, **kwargs
    ):
        """Create and return a gRPC channel object.

        Args:
            address (str): The host for the channel to use.
            credentials (~.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            kwargs (dict): Keyword arguments, which are passed to the
                channel creation.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return google.api_core.grpc_helpers.create_channel(
            address, credentials=credentials, scopes=cls._OAUTH_SCOPES, **kwargs
        )

    @property
    def channel(self):
        """The gRPC channel used by the transport.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return self._channel

    @property
    def analyze_sentiment(self):
        """Return the gRPC stub for :meth:`LanguageServiceClient.analyze_sentiment`.

        Analyzes the sentiment of the provided text.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["language_service_stub"].AnalyzeSentiment

    @property
    def analyze_entities(self):
        """Return the gRPC stub for :meth:`LanguageServiceClient.analyze_entities`.

        Finds named entities (currently proper names and common nouns) in the text
        along with entity types, salience, mentions for each entity, and
        other properties.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["language_service_stub"].AnalyzeEntities

    @property
    def analyze_entity_sentiment(self):
        """Return the gRPC stub for :meth:`LanguageServiceClient.analyze_entity_sentiment`.

        Address The metadata identifies the street number and locality plus
        whichever additional elements appear in the text:

        .. raw:: html

            <li><code>street_number</code> &ndash; street number</li>
            <li><code>locality</code> &ndash; city or town</li>
            <li><code>street_name</code> &ndash; street/route name, if detected</li>
            <li><code>postal_code</code> &ndash; postal code, if detected</li>
            <li><code>country</code> &ndash; country, if detected</li>
            <li><code>broad_region</code> &ndash; administrative area, such as the
            state, if detected</li> <li><code>narrow_region</code> &ndash; smaller
            administrative area, such as county, if detected</li>
            <li><code>sublocality</code> &ndash; used in Asian addresses to demark a
            district within a city, if detected</li></ul>

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["language_service_stub"].AnalyzeEntitySentiment

    @property
    def analyze_syntax(self):
        """Return the gRPC stub for :meth:`LanguageServiceClient.analyze_syntax`.

        Analyzes the syntax of the text and provides sentence boundaries and
        tokenization along with part of speech tags, dependency trees, and other
        properties.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["language_service_stub"].AnalyzeSyntax

    @property
    def classify_text(self):
        """Return the gRPC stub for :meth:`LanguageServiceClient.classify_text`.

        Classifies a document into categories.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["language_service_stub"].ClassifyText

    @property
    def annotate_text(self):
        """Return the gRPC stub for :meth:`LanguageServiceClient.annotate_text`.

        A convenience method that provides all the features that analyzeSentiment,
        analyzeEntities, and analyzeSyntax provide in one call.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["language_service_stub"].AnnotateText
