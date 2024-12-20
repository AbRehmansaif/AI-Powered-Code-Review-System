# Generated by Django 5.1.3 on 2024-11-21 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pl', models.CharField(choices=[('PY', 'Python'), ('JAVA', 'Java'), ('JS', 'JavaScript'), ('C', 'C'), ('CPP', 'C++'), ('C#', 'C#'), ('PHP', 'PHP')], default='PY', max_length=10, verbose_name='Programming Language')),
                ('framework', models.CharField(choices=[('REACT', 'React'), ('ANGULAR', 'Angular'), ('VUE', 'Vue'), ('SPRING', 'Spring'), ('DJANGO', 'Django')], default='DJANGO', max_length=10, verbose_name='Programming Language')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='select_language', to='user.user', verbose_name='User')),
            ],
            options={
                'verbose_name': 'Select Language',
                'verbose_name_plural': 'Select Languages',
            },
        ),
        migrations.CreateModel(
            name='CodeReviewSelection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_type', models.CharField(choices=[('SECURITY', 'Security'), ('EFFIENCY', 'Efficiency'), ('STYLING', 'Styling')], default='STYLING', max_length=10, verbose_name='Review Type')),
                ('code_content', models.TextField(verbose_name='Code Content')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Completed', 'Completed'), ('Processing', 'Processing'), ('Failed', 'Failed')], default='Processing', max_length=10, verbose_name='Status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='code_review_selection', to='user.user', verbose_name='User')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='code_review_language_selection', to='user_code.selectlanguage', verbose_name='Language Selection')),
            ],
            options={
                'verbose_name': 'Code Review Selection',
                'verbose_name_plural': 'Code Review Selections',
            },
        ),
    ]
