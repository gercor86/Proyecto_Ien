from django.urls import path
from .views import Base, Detalle_dulce_v, Dulce_v, Receta3, actualizar_receta, eliminar_receta, figacita_manteca, pan_campo, pan_viena, pionono

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

]
