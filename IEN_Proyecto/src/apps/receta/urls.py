from django.urls import path
from .views import Base, Detalle_dulce_v, Dulce_v, Receta3, actualizar_receta, berlinesas_donas, bizcochito_grasa, eliminar_receta, grisines_tradiconales  
from .views import pan_campo, pan_viena, pionono, pan_salvado, figacita_manteca, galletas_marineras, panes_saborizados 

urlpatterns = [
    path('', Base.as_view(), name = 'base'),
    path('receta/dulce/',Dulce_v.as_view(), name = 'receta_dulce'),
    path('receta/bizcochuelo', Detalle_dulce_v.as_view(), name = 'bizcochuelo'),
    path('receta/pionono', pionono.as_view(), name = 'pionono'),
    path('receta/pan_campo', pan_campo.as_view(), name = 'pan_campo'),
    path('receta/crear_receta', Receta3.as_view(), name = 'crear_receta'),
    path('receta/actualizar_receta/<int:pk>', actualizar_receta.as_view(), name = 'actualizar_receta'),
    path('receta/eliminar_receta/<int:pk>', eliminar_receta.as_view(), name = 'eliminar_receta'),
    path('receta/figacita_manteca', figacita_manteca.as_view(), name = 'figacita_manteca'),
    path('receta/pan_viena', pan_viena.as_view(), name = 'pan_viena'),
    path('receta/bizochito_grasa', bizcochito_grasa.as_view(), name = 'bizcochito_grasa'),
    path('receta/pan_salvado', pan_salvado.as_view(), name = 'pan_salvado'),
    path('receta/panes_sabores', panes_saborizados.as_view(), name = 'panes_sabores'),
    path('recetas/galletas_marineras', galletas_marineras.as_view(), name = 'galletas_marineras'),
    path('receta/berlinesas_donas', berlinesas_donas.as_view(), name = 'berlinesas_donas'),
    path('receta/grisines_tradicionales', grisines_tradiconales.as_view(), name = 'grisines_tradicionales')
]
