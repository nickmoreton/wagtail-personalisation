# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 19:36
from __future__ import unicode_literals

from django.db import migrations

import wagtail.blocks as wagtail_blocks
import wagtail.fields as wagtail_fields

import wagtail_personalisation


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_create_homepage"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="intro",
            field=wagtail_fields.RichTextField(
                default='<p>Thank you for trying <a href="http://wagxperience.io" target="_blank">Wagxperience</a>!</p>'
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="homepage",
            name="body",
            field=wagtail_fields.StreamField(
                (
                    (
                        "personalisable_paragraph",
                        wagtail_blocks.StructBlock(
                            (
                                (
                                    "segment",
                                    wagtail_blocks.ChoiceBlock(
                                        choices=wagtail_personalisation.blocks.list_segment_choices,
                                        help_text="Only show this content block for users in this segment",
                                        label="Personalisation segment",
                                        required=False,
                                    ),
                                ),
                                ("paragraph", wagtail_blocks.RichTextBlock()),
                            ),
                            icon="pilcrow",
                        ),
                    ),
                ),
                default="",
                use_json_field=True,
            ),
            preserve_default=False,
        ),
    ]
