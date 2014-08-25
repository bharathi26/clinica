# Create your views here.

from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import LabTest, Item,Sale,SaleItem,SaleTest
from extra_views import InlineFormSetView,CreateWithInlinesView



class LabTestListView(ListView):
    model = LabTest
    context_object_name = "tests"
    template_name = "clinica/list_test.html"


class ItemListView(ListView):
    model = Item
    context_object_name = "items"
    template_name = "clinica/list_item.html"


class CreateItemView(CreateView):
    model = Item
    template_name = 'clinica/add_item.html'


class CreateLabTestView(CreateView):
    model = LabTest
    template_name = 'clinica/add_lab_test.html'


class UpdateItemView(UpdateView):
    model = Item
    template_name = 'clinica/add_item.html'


class UpdateLabTestView(UpdateView):
    model = LabTest
    template_name = 'clinica/add_lab_test.html'


class ItemInline(InlineFormSetView):
    model = SaleItem


class TestInline(InlineFormSetView):
    model = SaleTest


class CreateSaleInline(CreateWithInlinesView):
    model = Sale
    inlines = [ItemInline,TestInline]
