#!/usr/bin/env python
# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for main."""

import re
import zipfile

import main


_TEST_IMAGE_URI = 'gs://{}/language/image8.png'


def test_batch_empty():
    for batch_size in range(1, 10):
        assert len(
            list(main.batch([], batch_size=batch_size))) == 0


def test_batch_single():
    for batch_size in range(1, 10):
        batched = tuple(main.batch([1], batch_size=batch_size))
        assert batched == ((1,),)


def test_single_image_returns_text(cloud_config):
    vision_api_client = main.VisionApi()

    image_path = _TEST_IMAGE_URI.format(cloud_config.storage_bucket)
    texts = vision_api_client.detect_text([image_path])

    assert image_path in texts
    _, document = main.extract_description(texts[image_path])
    assert "daughter" in document
    assert "Bennet" in document
    assert "hat" in document


def test_single_nonimage_returns_error():
    vision_api_client = main.VisionApi()
    texts = vision_api_client.detect_text(['README.md'])
    assert "README.md" not in texts


def test_text_returns_entities():
    text = "Holmes and Watson walked to the cafe."
    text_analyzer = main.TextAnalyzer()
    entities = text_analyzer.nl_detect(text)
    assert entities
    etype, ename, salience, wurl = text_analyzer.extract_entity_info(
        entities[0])
    assert ename == 'holmes'
    assert wurl == 'http://en.wikipedia.org/wiki/Sherlock_Holmes'


def test_entities_list(cloud_config):
    vision_api_client = main.VisionApi()
    image_path = _TEST_IMAGE_URI.format(cloud_config.storage_bucket)
    texts = vision_api_client.detect_text([image_path])
    locale, document = main.extract_description(texts[image_path])
    text_analyzer = main.TextAnalyzer()
    entities = text_analyzer.nl_detect(document)
    assert entities
    etype, ename, salience, wurl = text_analyzer.extract_entity_info(
        entities[0])
    assert ename == 'bennet'
    assert wurl == 'http://en.wikipedia.org/wiki/Mr_Bennet'


def test_main(remote_resource, tmpdir, capsys):
    images_path = str(tmpdir.mkdir('images'))

    # First, pull down some test data
    zip_path = remote_resource('language/ocr_nl-images-small.zip', tmpdir)

    # Extract it to the image directory
    with zipfile.ZipFile(zip_path) as zfile:
        zfile.extractall(images_path)

    main.main(images_path, str(tmpdir.join('ocr_nl.db')))

    stdout, _ = capsys.readouterr()

    assert re.search(r'google was found with count', stdout)
