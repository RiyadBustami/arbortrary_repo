from django.urls import path
from . import views

urlpatterns=[
    path('',views.dashboard),
    path('new/tree/',views.plant_new_tree),
    path('new/tree/add_new_plant/',views.add_new_plant),
    path('user/account/',views.manage_trees),
    path('show/<tree_id>/',views.show_tree),
    path('add_visit/<tree_id>/',views.add_visit),
    path('delete/<tree_id>/',views.delete_tree),
    path('edit/<tree_id>/',views.edit_tree),
    path('edit/<tree_id>/update/',views.update_tree),
]