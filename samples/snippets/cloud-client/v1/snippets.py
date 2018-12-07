#!/usr/bin/env python

# Copyright 2018 Google, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This application demonstrates how to perform basic operations with the
Google Cloud Natural Language API

For more information, the documentation at
https://cloud.google.com/natural-language/docs.
"""

import argparse
import sys


def sentiment_text():
    # [START language_sentiment_text]
    from google.cloud import language
    from google.cloud.language import enums
    from google.cloud.language import types

    text = 'Hello, world!'

    client = language.LanguageServiceClient()

    try:
        text = text.decode('utf-8')
    except AttributeError:
        pass

    # Instantiates a plain text document.
    # [START language_python_migration_sentiment_text]
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects sentiment in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    sentiment = client.analyze_sentiment(document).document_sentiment

    print('Score: {}'.format(sentiment.score))
    print('Magnitude: {}'.format(sentiment.magnitude))
    # [END language_python_migration_sentiment_text]
    # [END language_sentiment_text]


def sentiment_file():
    # [START language_sentiment_gcs]
    from google.cloud import language
    from google.cloud.language import enums
    from google.cloud.language import types

    gcs_uri = 'gs://cloud-samples-data/language/hello.txt'

    client = language.LanguageServiceClient()

    # Instantiates a plain text document.
    # [START language_python_migration_document_gcs]
    document = types.Document(
        gcs_content_uri=gcs_uri,
        type=enums.Document.Type.PLAIN_TEXT)
    # [END language_python_migration_document_gcs]

    # Detects sentiment in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    sentiment = client.analyze_sentiment(document).document_sentiment

    print('Score: {}'.format(sentiment.score))
    print('Magnitude: {}'.format(sentiment.magnitude))
    # [END language_sentiment_gcs]


def entities_text():
    # [START language_entities_text]
    import six
    from google.cloud import language
    from google.cloud.language import enums
    from google.cloud.language import types

    text = 'President Kennedy spoke at the White House.'

    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Instantiates a plain text document.
    # [START language_python_migration_entities_text]
    # [START language_python_migration_document_text]
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
    # [END language_python_migration_document_text]

    # Detects entities in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    entities = client.analyze_entities(document).entities

    for entity in entities:
        entity_type = enums.Entity.Type(entity.type)
        print('=' * 20)
        print(u'{:<16}: {}'.format('name', entity.name))
        print(u'{:<16}: {}'.format('type', entity_type.name))
        print(u'{:<16}: {}'.format('salience', entity.salience))
        print(u'{:<16}: {}'.format('wikipedia_url',
              entity.metadata.get('wikipedia_url', '-')))
        print(u'{:<16}: {}'.format('mid', entity.metadata.get('mid', '-')))
    # [END language_python_migration_entities_text]
    # [END language_entities_text]


def entities_file():
    # [START language_entities_gcs]
    from google.cloud import language
    from google.cloud.language import enums
    from google.cloud.language import types

    gcs_uri = 'gs://cloud-samples-data/language/president.txt'

    client = language.LanguageServiceClient()

    # Instantiates a plain text document.
    document = types.Document(
        gcs_content_uri=gcs_uri,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects sentiment in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    entities = client.analyze_entities(document).entities

    for entity in entities:
        entity_type = enums.Entity.Type(entity.type)
        print('=' * 20)
        print(u'{:<16}: {}'.format('name', entity.name))
        print(u'{:<16}: {}'.format('type', entity_type.name))
        print(u'{:<16}: {}'.format('salience', entity.salience))
        print(u'{:<16}: {}'.format('wikipedia_url',
              entity.metadata.get('wikipedia_url', '-')))
        print(u'{:<16}: {}'.format('mid', entity.metadata.get('mid', '-')))
    # [END language_entities_gcs]


def syntax_text():
    # [START language_syntax_text]
    import six
    from google.cloud import language
    from google.cloud.language import enums
    from google.cloud.language import types

    text = 'President Kennedy spoke at the White House.'

    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Instantiates a plain text document.
    # [START language_python_migration_syntax_text]
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects syntax in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    tokens = client.analyze_syntax(document).tokens

    for token in tokens:
        part_of_speech_tag = enums.PartOfSpeech.Tag(token.part_of_speech.tag)
        print(u'{}: {}'.format(part_of_speech_tag.name,
                               token.text.content))
    # [END language_python_migration_syntax_text]
    # [END language_syntax_text]


def syntax_file():
    # [START language_syntax_gcs]
    from google.cloud import language
    from google.cloud.language import enums
    from google.cloud.language import types

    gcs_uri = 'gs://cloud-samples-data/language/president.txt'

    client = language.LanguageServiceClient()

    # Instantiates a plain text document.
    document = types.Document(
        gcs_content_uri=gcs_uri,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects syntax in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    tokens = client.analyze_syntax(document).tokens

    for token in tokens:
        part_of_speech_tag = enums.PartOfSpeech.Tag(token.part_of_speech.tag)
        print(u'{}: {}'.format(part_of_speech_tag.name,
                               token.text.content))
    # [END language_syntax_gcs]


def entity_sentiment_text():
    # [START language_entity_sentiment_text]
    import six
    from google.cloud import language
    from google.cloud.language import enums
    from google.cloud.language import types

    text = 'President Kennedy spoke at the White House.'

    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    document = types.Document(
        content=text.encode('utf-8'),
        type=enums.Document.Type.PLAIN_TEXT)

    # Detect and send native Python encoding to receive correct word offsets.
    encoding = enums.EncodingType.UTF32
    if sys.maxunicode == 65535:
        encoding = enums.EncodingType.UTF16

    result = client.analyze_entity_sentiment(document, encoding)

    for entity in result.entities:
        print('Mentions: ')
        print(u'Name: "{}"'.format(entity.name))
        for mention in entity.mentions:
            print(u'  Begin Offset : {}'.format(mention.text.begin_offset))
            print(u'  Content : {}'.format(mention.text.content))
            print(u'  Magnitude : {}'.format(mention.sentiment.magnitude))
            print(u'  Sentiment : {}'.format(mention.sentiment.score))
            print(u'  Type : {}'.format(mention.type))
        print(u'Salience: {}'.format(entity.salience))
        print(u'Sentiment: {}\n'.format(entity.sentiment))
    # [END language_entity_sentiment_text]


def entity_sentiment_file():
    # [START language_entity_sentiment_gcs]
    from google.cloud import language
    from google.cloud.language import enums
    from google.cloud.language import types

    gcs_uri = 'gs://cloud-samples-data/language/president.txt'

    client = language.LanguageServiceClient()

    document = types.Document(
        gcs_content_uri=gcs_uri,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detect and send native Python encoding to receive correct word offsets.
    encoding = enums.EncodingType.UTF32
    if sys.maxunicode == 65535:
        encoding = enums.EncodingType.UTF16

    result = client.analyze_entity_sentiment(document, encoding)

    for entity in result.entities:
        print(u'Name: "{}"'.format(entity.name))
        for mention in entity.mentions:
            print(u'  Begin Offset : {}'.format(mention.text.begin_offset))
            print(u'  Content : {}'.format(mention.text.content))
            print(u'  Magnitude : {}'.format(mention.sentiment.magnitude))
            print(u'  Sentiment : {}'.format(mention.sentiment.score))
            print(u'  Type : {}'.format(mention.type))
        print(u'Salience: {}'.format(entity.salience))
        print(u'Sentiment: {}\n'.format(entity.sentiment))
    # [END language_entity_sentiment_gcs]


def classify_text():
    # [START language_classify_text]
    import six
    from google.cloud import language
    from google.cloud.language import enums
    from google.cloud.language import types

    text = 'Android is a mobile operating system developed by Google, ' \
           'based on the Linux kernel and designed primarily for ' \
           'touchscreen mobile devices such as smartphones and tablets.'

    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    document = types.Document(
        content=text.encode('utf-8'),
        type=enums.Document.Type.PLAIN_TEXT)

    categories = client.classify_text(document).categories

    for category in categories:
        print(u'=' * 20)
        print(u'{:<16}: {}'.format('name', category.name))
        print(u'{:<16}: {}'.format('confidence', category.confidence))
    # [END language_classify_text]


def classify_file():
    # [START language_classify_gcs]
    from google.cloud import language
    from google.cloud.language import enums
    from google.cloud.language import types

    gcs_uri = 'gs://cloud-samples-data/language/android.txt'

    client = language.LanguageServiceClient()

    document = types.Document(
        gcs_content_uri=gcs_uri,
        type=enums.Document.Type.PLAIN_TEXT)

    categories = client.classify_text(document).categories

    for category in categories:
        print(u'=' * 20)
        print(u'{:<16}: {}'.format('name', category.name))
        print(u'{:<16}: {}'.format('confidence', category.confidence))
    # [END language_classify_gcs]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(dest='command')

    classify_text_parser = subparsers.add_parser(
        'classify-text', help=classify_text.__doc__)

    classify_text_parser = subparsers.add_parser(
        'classify-file', help=classify_file.__doc__)

    sentiment_entities_text_parser = subparsers.add_parser(
        'sentiment-entities-text', help=entity_sentiment_text.__doc__)

    sentiment_entities_file_parser = subparsers.add_parser(
        'sentiment-entities-file', help=entity_sentiment_file.__doc__)

    sentiment_text_parser = subparsers.add_parser(
        'sentiment-text', help=sentiment_text.__doc__)

    sentiment_file_parser = subparsers.add_parser(
        'sentiment-file', help=sentiment_file.__doc__)

    entities_text_parser = subparsers.add_parser(
        'entities-text', help=entities_text.__doc__)

    entities_file_parser = subparsers.add_parser(
        'entities-file', help=entities_file.__doc__)

    syntax_text_parser = subparsers.add_parser(
        'syntax-text', help=syntax_text.__doc__)

    syntax_file_parser = subparsers.add_parser(
        'syntax-file', help=syntax_file.__doc__)

    args = parser.parse_args()

    if args.command == 'sentiment-text':
        sentiment_text()
    elif args.command == 'sentiment-file':
        sentiment_file()
    elif args.command == 'entities-text':
        entities_text()
    elif args.command == 'entities-file':
        entities_file()
    elif args.command == 'syntax-text':
        syntax_text()
    elif args.command == 'syntax-file':
        syntax_file()
    elif args.command == 'sentiment-entities-text':
        entity_sentiment_text()
    elif args.command == 'sentiment-entities-file':
        entity_sentiment_file()
    elif args.command == 'classify-text':
        classify_text()
    elif args.command == 'classify-file':
        classify_file()
