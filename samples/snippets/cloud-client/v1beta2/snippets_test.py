# -*- coding: utf-8 -*-
# Copyright 2017 Google, Inc.
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

import os

import snippets

BUCKET = os.environ['CLOUD_STORAGE_BUCKET']
TEST_FILE_URL = 'gs://{}/text.txt'.format(BUCKET)
LONG_TEST_FILE_URL = 'gs://{}/android_text.txt'.format(BUCKET)


def test_sentiment_text(capsys):
    snippets.sentiment_text('President Obama is speaking at the White House.')
    out, _ = capsys.readouterr()
    assert 'Score: 0' in out


def test_sentiment_utf(capsys):
    snippets.sentiment_text(
        u'1er site d\'information. Les articles du journal et toute l\'' +
        u'actualité en continu : International, France, Société, Economie, ' +
        u'Culture, Environnement')
    out, _ = capsys.readouterr()
    assert 'Score: 0' in out


def test_sentiment_file(capsys):
    snippets.sentiment_file(TEST_FILE_URL)
    out, _ = capsys.readouterr()
    assert 'Score: 0' in out


def test_entities_text(capsys):
    snippets.entities_text('President Obama is speaking at the White House.')
    out, _ = capsys.readouterr()
    assert 'name' in out
    assert ': Obama' in out


def test_entities_file(capsys):
    snippets.entities_file(TEST_FILE_URL)
    out, _ = capsys.readouterr()
    assert 'name' in out
    assert ': Obama' in out


def test_syntax_text(capsys):
    snippets.syntax_text('President Obama is speaking at the White House.')
    out, _ = capsys.readouterr()
    assert 'NOUN: President' in out


def test_syntax_file(capsys):
    snippets.syntax_file(TEST_FILE_URL)
    out, _ = capsys.readouterr()
    assert 'NOUN: President' in out


def test_sentiment_entities_text(capsys):
    snippets.entity_sentiment_text(
        'President Obama is speaking at the White House.')
    out, _ = capsys.readouterr()
    assert 'Content : White House' in out


def test_sentiment_entities_file(capsys):
    snippets.entity_sentiment_file(TEST_FILE_URL)
    out, _ = capsys.readouterr()
    assert 'Content : White House' in out


def test_sentiment_entities_utf(capsys):
    snippets.entity_sentiment_text(
        'foo→bar')
    out, _ = capsys.readouterr()
    assert 'Begin Offset : 4' in out


def test_classify_text(capsys):
    snippets.classify_text(
        'Android is a mobile operating system developed by Google, '
        'based on the Linux kernel and designed primarily for touchscreen '
        'mobile devices such as smartphones and tablets.')
    out, _ = capsys.readouterr()
    assert 'name' in out
    assert '/Computers & Electronics' in out


def test_classify_file(capsys):
    snippets.classify_file(LONG_TEST_FILE_URL)
    out, _ = capsys.readouterr()
    assert 'name' in out
    assert '/Computers & Electronics' in out
