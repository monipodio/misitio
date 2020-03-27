# Generated by Django 2.2.5 on 2020-02-16 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anticipos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('fecha', models.DateTimeField(verbose_name='Fecha anticipo')),
                ('mes', models.CharField(blank=True, max_length=2)),
                ('ano', models.CharField(blank=True, max_length=4)),
                ('valor', models.IntegerField(blank=True)),
                ('abon', models.CharField(blank=True, max_length=1)),
                ('notas', models.TextField(blank=True)),
                ('boleta', models.IntegerField(blank=True)),
            ],
            options={
                'verbose_name': 'anticipos',
                'ordering': ['fecha'],
            },
        ),
        migrations.CreateModel(
            name='Apoderados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('nombre', models.CharField(blank=True, max_length=80)),
                ('direccion', models.CharField(blank=True, max_length=60)),
                ('comuna', models.CharField(blank=True, max_length=5)),
                ('region', models.CharField(blank=True, max_length=2)),
                ('fono_apod', models.CharField(blank=True, max_length=12, verbose_name='Fono Cuidador')),
                ('fono2_apod', models.CharField(blank=True, max_length=12, verbose_name='Fono2 Cuidador')),
                ('parentezco', models.CharField(blank=True, max_length=50)),
                ('correo', models.CharField(blank=True, max_length=40)),
                ('notas', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Apoderado',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Cuidadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('nombre', models.CharField(blank=True, max_length=80)),
                ('fe_ini', models.DateTimeField(blank=True, null=True)),
                ('direccion', models.CharField(blank=True, max_length=60)),
                ('comuna', models.CharField(blank=True, max_length=5)),
                ('region', models.CharField(blank=True, max_length=2)),
                ('fono_cuid', models.CharField(blank=True, max_length=12, verbose_name='Fono Cuidador')),
                ('fono2_cuid', models.CharField(blank=True, max_length=12, verbose_name='Fono2 Cuidador')),
                ('fe_nac', models.DateTimeField(blank=True, null=True)),
                ('sexo', models.CharField(blank=True, max_length=1)),
                ('correo', models.CharField(blank=True, max_length=40)),
                ('notas', models.TextField(blank=True)),
                ('tipo', models.CharField(blank=True, max_length=1)),
                ('media', models.FileField(blank=True, null=True, upload_to='misitio/ai/static/img/')),
                ('clasi', models.CharField(blank=True, default='', max_length=1)),
                ('extran', models.CharField(blank=True, default='0', max_length=1)),
                ('estado', models.BooleanField(blank=True, default='')),
                ('instr', models.CharField(blank=True, max_length=1)),
                ('elim_foto', models.CharField(blank=True, max_length=1)),
                ('apago1', models.IntegerField(blank=True)),
                ('apago2', models.IntegerField(blank=True)),
                ('apago3', models.IntegerField(blank=True)),
            ],
            options={
                'verbose_name': 'Cuidadores',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Detapauta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('paciente', models.CharField(max_length=60, null=True, verbose_name='Nombre Paciente')),
                ('fecha', models.DateTimeField(blank=True, verbose_name='Fecha Pauta')),
                ('valor_t1', models.IntegerField(blank=True)),
                ('tipo_turno1', models.CharField(blank=True, max_length=1)),
                ('valor_t2', models.IntegerField(blank=True)),
                ('tipo_turno2', models.CharField(blank=True, max_length=1)),
                ('valor_t3', models.IntegerField(blank=True)),
                ('tipo_turno3', models.CharField(blank=True, max_length=1)),
                ('total', models.IntegerField(blank=True)),
            ],
            options={
                'verbose_name': 'detapauta',
                'ordering': ['fecha'],
            },
        ),
        migrations.CreateModel(
            name='Diario_aux',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(blank=True, max_length=10)),
                ('ndia', models.IntegerField(blank=True, default=0)),
                ('cdia', models.CharField(blank=True, max_length=10)),
                ('paciente', models.CharField(max_length=60, verbose_name='Nombre Paciente')),
                ('turno1', models.IntegerField(blank=True, default=0)),
                ('turno2', models.IntegerField(blank=True, default=0)),
                ('turno3', models.IntegerField(blank=True, default=0)),
                ('valor_t1', models.IntegerField(blank=True, default=0)),
                ('valor_t2', models.IntegerField(blank=True, default=0)),
                ('valor_t3', models.IntegerField(blank=True, default=0)),
                ('val_tot', models.IntegerField(blank=True, default=0)),
                ('acum1', models.IntegerField(blank=True, default=0)),
                ('abonos', models.IntegerField(blank=True, default=0)),
                ('acum2', models.IntegerField(blank=True, default=0)),
                ('notas', models.TextField(blank=True)),
                ('boleta', models.CharField(blank=True, max_length=12)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mensual_aux',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(blank=True, max_length=10)),
                ('paciente', models.CharField(max_length=80, null=True, verbose_name='Nombre Paciente')),
                ('con', models.CharField(blank=True, max_length=12)),
                ('turnos', models.IntegerField(blank=True)),
                ('val_mes', models.IntegerField(blank=True)),
                ('saldoant', models.IntegerField(default=0)),
                ('abonos', models.IntegerField(blank=True, default=0)),
                ('saldo', models.IntegerField(blank=True, default=0)),
                ('celular', models.CharField(blank=True, max_length=12)),
                ('correo', models.CharField(blank=True, max_length=40)),
                ('mes', models.IntegerField(blank=True, default=0)),
                ('ano', models.IntegerField(blank=True, default=0)),
                ('n_apod', models.CharField(blank=True, max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Otrospermisos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'permissions': (('menu_pauta', 'menu_pauta'), ('menu_parametros', 'menu_parametros')),
            },
        ),
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=80, verbose_name='Nombre Paciente')),
                ('fe_ini', models.DateTimeField(verbose_name='Fecha de Inicio')),
                ('direccion', models.CharField(max_length=61)),
                ('comuna', models.CharField(max_length=5, null=True)),
                ('comuna_apod', models.CharField(max_length=5, null=True)),
                ('region', models.CharField(max_length=2)),
                ('fono_pcte', models.CharField(blank=True, max_length=12, verbose_name='Fono del Paciente')),
                ('fono2_pcte', models.CharField(blank=True, max_length=12, verbose_name='Fono alternativo del Paciente')),
                ('fe_nac', models.DateTimeField(blank=True, null=True)),
                ('sexo', models.CharField(default=3, max_length=1)),
                ('correo', models.CharField(blank=True, max_length=40)),
                ('n_apod', models.CharField(max_length=80, verbose_name='Nombre Apoderado')),
                ('rut_apod', models.CharField(max_length=10)),
                ('dir_apod', models.CharField(blank=True, max_length=61, null=True)),
                ('f_apod', models.CharField(blank=True, max_length=12, null=True)),
                ('fono2_apod', models.CharField(blank=True, max_length=12, null=True)),
                ('parentes', models.CharField(blank=True, max_length=30, null=True)),
                ('correo_apod', models.CharField(blank=True, max_length=40, null=True)),
                ('medico', models.CharField(blank=True, max_length=60)),
                ('notas', models.TextField(blank=True)),
                ('cob', models.CharField(max_length=1, null=True)),
                ('estado', models.BooleanField(blank=True, default='')),
                ('clasi', models.CharField(blank=True, default='', max_length=1)),
                ('abon', models.CharField(blank=True, max_length=1)),
                ('yace', models.CharField(blank=True, max_length=1, null=True)),
                ('valor_t1', models.IntegerField(blank=True)),
                ('valor_t2', models.IntegerField(blank=True)),
                ('valor_t3', models.IntegerField(blank=True)),
                ('doc_cobro', models.CharField(blank=True, max_length=1, null=True)),
                ('localizacion', models.CharField(max_length=81, null=True)),
                ('saldoant', models.IntegerField(blank=True, default=0)),
            ],
            options={
                'verbose_name': 'Paciente',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Pacientes_aux',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=80, verbose_name='Nombre Paciente')),
                ('fe_ini', models.DateTimeField(verbose_name='Fecha de Inicio')),
                ('direccion', models.CharField(max_length=61)),
                ('comuna', models.CharField(max_length=5)),
                ('comuna_apod', models.CharField(max_length=5)),
                ('region', models.CharField(max_length=2)),
                ('fono_pcte', models.CharField(blank=True, max_length=12, verbose_name='Fono del Paciente')),
                ('fono2_pcte', models.CharField(blank=True, max_length=12, verbose_name='Fono alternativo del Paciente')),
                ('fe_nac', models.DateTimeField(blank=True, null=True)),
                ('sexo', models.CharField(default=3, max_length=1)),
                ('correo', models.CharField(blank=True, max_length=40)),
                ('n_apod', models.CharField(max_length=80, verbose_name='Nombre Apoderado')),
                ('rut_apod', models.CharField(max_length=10)),
                ('dir_apod', models.CharField(blank=True, max_length=61, null=True)),
                ('f_apod', models.CharField(blank=True, max_length=12, null=True)),
                ('fono2_apod', models.CharField(blank=True, max_length=12, null=True)),
                ('parentes', models.CharField(blank=True, max_length=30, null=True)),
                ('correo_apod', models.CharField(blank=True, max_length=40, null=True)),
                ('medico', models.CharField(blank=True, max_length=60)),
                ('notas', models.TextField(blank=True)),
                ('cob', models.CharField(max_length=1, null=True)),
                ('estado', models.BooleanField(blank=True, default='')),
                ('clasi', models.CharField(blank=True, default='', max_length=1)),
                ('abon', models.CharField(blank=True, max_length=1)),
                ('yace', models.CharField(blank=True, max_length=1, null=True)),
                ('valor_t1', models.IntegerField(blank=True, default=0)),
                ('valor_t2', models.IntegerField(blank=True, default=0)),
                ('valor_t3', models.IntegerField(blank=True, default=0)),
                ('doc_cobro', models.CharField(blank=True, max_length=1, null=True)),
                ('localizacion', models.CharField(max_length=81)),
                ('saldoant', models.IntegerField(blank=True, default=0)),
                ('mes', models.CharField(blank=True, max_length=2)),
                ('ano', models.CharField(blank=True, max_length=4)),
            ],
            options={
                'verbose_name': 'Paciente_aux',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Pagocui_aux',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(blank=True, max_length=10)),
                ('paciente', models.CharField(max_length=80, null=True, verbose_name='Nombre Paciente')),
                ('fecha', models.DateTimeField(blank=True, verbose_name='Fecha Pauta')),
                ('rut_t1', models.CharField(blank=True, max_length=10)),
                ('turno1', models.CharField(blank=True, max_length=80, verbose_name='Nombre turno1')),
                ('tipo_turno', models.CharField(default=0, max_length=1, null=True)),
                ('valor', models.IntegerField(blank=True)),
                ('reca_cui', models.CharField(default=0, max_length=1)),
                ('turno', models.CharField(default=0, max_length=1, null=True)),
            ],
            options={
                'verbose_name': 'Pagocui_aux',
                'ordering': ['paciente'],
            },
        ),
        migrations.CreateModel(
            name='Param',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=5)),
                ('codigo', models.CharField(blank=True, max_length=5)),
                ('descrip', models.CharField(max_length=79, null=True, verbose_name='Desripcion')),
                ('valor1', models.IntegerField(blank=True)),
                ('valor2', models.IntegerField(blank=True)),
                ('valor3', models.IntegerField(blank=True)),
                ('sw_1', models.IntegerField(blank=True)),
                ('sw_2', models.IntegerField(blank=True)),
                ('notas', models.TextField(blank=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('corr', models.IntegerField(blank=True)),
                ('fecha2', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Parametro',
                'ordering': ['tipo', 'descrip'],
            },
        ),
        migrations.CreateModel(
            name='Pauta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(blank=True, max_length=10)),
                ('paciente', models.CharField(max_length=80, null=True, verbose_name='Nombre Paciente')),
                ('fe_ini', models.DateTimeField(blank=True, verbose_name='Fecha de Inicio')),
                ('fecha', models.DateTimeField(blank=True, verbose_name='Fecha Pauta')),
                ('rut_t1', models.CharField(blank=True, max_length=10)),
                ('turno1', models.CharField(blank=True, max_length=80, verbose_name='Nombre turno1')),
                ('rut_t2', models.CharField(blank=True, max_length=10)),
                ('turno2', models.CharField(blank=True, max_length=80, verbose_name='Nombre turno1')),
                ('rut_t3', models.CharField(blank=True, max_length=10)),
                ('turno3', models.CharField(blank=True, max_length=80, verbose_name='Nombre turno1')),
                ('valor_t1', models.IntegerField(blank=True)),
                ('valor_t2', models.IntegerField(blank=True)),
                ('valor_t3', models.IntegerField(blank=True)),
                ('valor_p1', models.IntegerField(blank=True, default=0)),
                ('valor_p2', models.IntegerField(blank=True, default=0)),
                ('valor_p3', models.IntegerField(blank=True, default=0)),
                ('notas', models.TextField(blank=True)),
                ('yace', models.CharField(blank=True, max_length=1, null=True)),
                ('tipo_turno1', models.CharField(default=0, max_length=1, null=True)),
                ('tipo_turno2', models.CharField(default=0, max_length=1, null=True)),
                ('tipo_turno3', models.CharField(default=0, max_length=1, null=True)),
                ('reca_cui', models.CharField(default=0, max_length=1)),
            ],
            options={
                'verbose_name': 'Pauta',
                'ordering': ['paciente'],
            },
        ),
        migrations.CreateModel(
            name='Pauta_aux',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(blank=True, max_length=10)),
                ('paciente', models.CharField(max_length=80, null=True, verbose_name='Nombre Paciente')),
                ('fe_ini', models.DateTimeField(blank=True, verbose_name='Fecha de Inicio')),
                ('fecha', models.DateTimeField(blank=True, verbose_name='Fecha Pauta')),
                ('rut_t1', models.CharField(blank=True, max_length=10)),
                ('turno1', models.CharField(blank=True, max_length=80, verbose_name='Nombre turno1')),
                ('rut_t2', models.CharField(blank=True, max_length=10)),
                ('turno2', models.CharField(blank=True, max_length=80, verbose_name='Nombre turno1')),
                ('rut_t3', models.CharField(blank=True, max_length=10)),
                ('turno3', models.CharField(blank=True, max_length=80, verbose_name='Nombre turno1')),
                ('valor_t1', models.IntegerField(blank=True)),
                ('valor_t2', models.IntegerField(blank=True)),
                ('valor_t3', models.IntegerField(blank=True)),
                ('valor_p1', models.IntegerField(blank=True)),
                ('valor_p2', models.IntegerField(blank=True)),
                ('valor_p3', models.IntegerField(blank=True)),
                ('notas', models.TextField(blank=True)),
                ('yace', models.CharField(blank=True, max_length=1, null=True)),
                ('tipo_turno1', models.CharField(default=0, max_length=1, null=True)),
                ('tipo_turno2', models.CharField(default=0, max_length=1, null=True)),
                ('tipo_turno3', models.CharField(default=0, max_length=1, null=True)),
                ('reca_cui', models.CharField(default=0, max_length=1)),
            ],
            options={
                'verbose_name': 'Pauta_aux',
                'ordering': ['paciente'],
            },
        ),
        migrations.CreateModel(
            name='Resupauta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(blank=True, max_length=10)),
                ('nombre', models.CharField(max_length=80, null=True, verbose_name='Nombre Cuidador')),
                ('mes', models.CharField(blank=True, max_length=2)),
                ('ano', models.CharField(blank=True, max_length=4)),
                ('tot_t1', models.IntegerField(blank=True)),
                ('tot_t2', models.IntegerField(blank=True)),
                ('tot_t3', models.IntegerField(blank=True)),
                ('tot_val', models.IntegerField(blank=True)),
            ],
            options={
                'verbose_name': 'resupauta',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Saldos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(blank=True, max_length=10)),
                ('mes', models.IntegerField(blank=True, default=0)),
                ('ano', models.IntegerField(blank=True, default=0)),
                ('saldo', models.IntegerField(blank=True, default=0)),
                ('saldoant', models.IntegerField(blank=True, default=0)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('nombre', models.CharField(blank=True, max_length=60)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
    ]
