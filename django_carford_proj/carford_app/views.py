from carford_app.models import Car, Owner

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView


class OwnerList(ListView):
    model = Owner
    queryset = Owner.objects.all()


class OwnerDetailView(DetailView):
    template_name = './carford_app/owner_detail.html'

    def get_object(self):
        return Car.objects.filter(owner__id=self.kwargs.get('pk'))


class OwnerCreateView(CreateView):
    model = Owner
    fields = '__all__'
    success_url = reverse_lazy('carford_app:owner_list')


class OwnerUpdateView(UpdateView):
    model = Owner
    fields = '__all__'
    success_url = reverse_lazy('carford_app:owner_list')


class OwnerDeleteView(DeleteView):
    model = Owner
    fields = '__all__'
    success_url = reverse_lazy('carford_app:owner_list')

# Cars


class CarCreateView(CreateView):
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('carford_app:owner_list')


class CarUpdateView(UpdateView):
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('carford_app:owner_list')


class CarDeleteView(DeleteView):
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('carford_app:owner_list')
