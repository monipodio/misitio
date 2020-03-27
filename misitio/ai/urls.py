from django.urls import path
from django.conf.urls import include, url
from django.conf import settings

from .import views
from misitio.ai.views import EliminaCui,grid_cuidadores,NuevoCui
from misitio.ai.views import EliminaPac,grid_pacientes,NuevoPac
from misitio.ai.views import EliminaApod,grid_apoderados,NuevoApod,grid_anticipos
from misitio.ai.views import ActualizaCui
from misitio.ai.views import ActualizaPac
from misitio.ai.forms import CuidadoresForm
from misitio.ai.forms import PacientesForm
from misitio.ai.forms import ParamForm
from misitio.ai.forms import AnticiposForm

from misitio.ai.views import ficha_cuidadores
#from misitio.ai.views import ficha_pacientes
from misitio.ai.forms import ApoderadosForm
from misitio.ai.views import ActualizaApod
from misitio.ai.views import ficha_apoderados
from misitio.ai.views import Ficha_anticipos
from misitio.ai.views import acsv
from misitio.ai.views import cartolacui
from misitio.ai.views import eliminapauvacias
from misitio.ai.views import consultas
from misitio.ai.views import info_mensual
from misitio.ai.views import info_diario,subefotos
from misitio.ai.views import exceldetalle,excelmensual,ponenombresaldos
from misitio.ai.views import pdfdetalle

from django.contrib.auth.decorators import login_required
#from django.conf import settings

urlpatterns = [
	path('',views.login_ini, name='login_ini'),
	path('log_out/',views.log_out, name="log_out"),
	path('principal/',login_required(views.principal), name="principal"),
	path('grid_cuidadores/',views.grid_cuidadores, name="grid_cuidadores"),
	path('grid_cuidadorBusca/',views.grid_cuidadorBusca, name="grid_cuidadorBusca"),
	path('grid_pacientes/',views.grid_pacientes,name="grid_pacientes"),
	path('grid_apoderados/',views.grid_apoderados, name="grid_apoderados"),
	path('grid_pacienteBusca/',views.grid_pacienteBusca, name="grid_pacienteBusca"),
	path('grid_paramBusca/',views.grid_paramBusca, name="grid_paramBusca"),
	path('grid_pautaBusca/',views.grid_pautaBusca, name="grid_pautaBusca"),	
	path('grid_pauta/',views.grid_pauta, name="grid_pauta"),
	path('ficha_cuidadores/<int:id>',views.ficha_cuidadores, name="ficha_cuidadores"),
	path('ActualizaPauta/<int:id>',views.ActualizaPauta, name="ActualizaPauta"),
	path('ActualizaCui/<int:id>',views.ActualizaCui, name="ActualizaCui"),
	path('ActualizaPac/<int:id>',views.ActualizaPac, name="ActualizaPac"),
	path('ActualizaApod/<int:id>',views.ActualizaApod, name="ActualizaApod"),
	path('EliminaCui/<int:id>',views.EliminaCui, name="EliminaCui"),
	path('EliminaPac/<int:id>',views.EliminaPac, name="EliminaPac"),
	path('Eliminapac_nuevo/<int:id>',views.Eliminapac_nuevo, name="Eliminapac_nuevo"),
	path('EliminaApod/<int:id>',views.EliminaApod, name="EliminaApod"),
	path('NuevoCui/',views.NuevoCui,name="NuevoCui"),
	path('NuevoPac/',views.NuevoPac,name="NuevoPac"),
	path('NuevoApod/',views.NuevoApod,name="NuevoApod"),
	path('MenuParam/',views.MenuParam,name="MenuParam"),
	path('grid_param/',views.grid_param,name="grid_param"),
	path('FichaParam/<int:id>',views.FichaParam,name="FichaParam"),
	path('siexisterut/<rut>/',views.siexisterut,name="siexisterut"),
	path('info/',views.info,name="info"),
	path('liquimeses/',views.liquimeses,name="liquimeses"),
	path('Detapautaview/<rut>/<resu_mes>/<resu_ano>/',views.Detapautaview,name="Detapautaview"),
	path('NuevoParam/',views.NuevoParam,name="NuevoParam"),
	path('Ficha_anticipos/',views.Ficha_anticipos,name="Ficha_anticipos"),
	path('acsv/',views.acsv,name="acsv"),
	path('cartolacui/',views.cartolacui,name="cartolacui"),
	path('repo1/',views.repo1,name="repo1"),
	path('eliminapauvacias/',views.eliminapauvacias,name="eliminapauvacias"),
	path('grid_anticipos/',views.grid_anticipos,name="grid_anticipos"),
	path('consultas/',views.consultas,name="consultas"),
	path('info_mensual/',views.info_mensual,name="info_mensual"),
	path('info_diario/<rut>/<mes>/<ano>/',views.info_diario,name="info_diario"),
	path('exceldetalle/',views.exceldetalle,name="exceldetalle"),
	path('excelmensual/',views.excelmensual,name="excelmensual"),
	path('ponenombresaldos/',views.ponenombresaldos,name="ponenombresaldos"),
	path('subefotos/',views.subefotos,name="subefotos"),
	path('pdfdetalle/',views.pdfdetalle,name="pdfdetalle"),
]

