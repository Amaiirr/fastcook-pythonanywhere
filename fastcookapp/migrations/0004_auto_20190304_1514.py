# Generated by Django 2.1.5 on 2019-03-04 15:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fastcookapp', '0003_xmlgraph_sharedxmlgraph'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='xmlgraph',
            name='sharedXMLGraph',
        ),
        migrations.AddField(
            model_name='xmlgraph',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='xmlgraph',
            name='XMLGraph',
            field=models.TextField(default='<mxGraphModel><root><mxCell id="0"/><mxCell id="1" parent="0"/></root></mxGraphModel>', null=True),
        ),
    ]
