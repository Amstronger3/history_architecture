from django.contrib import admin
from django import forms
from django.utils.html import format_html

from .models import Map, Sections, Layers, Articles, Price, Museums, Route


@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    list_display = ('title', 'highlight_x', 'highlight_y', 'pin_x', 'pin_y',)


@admin.register(Sections)
class SectionsAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Layers)
class LayersAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'map', 'type')


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price',)


@admin.register(Museums)
class MuseumsAdmin(admin.ModelAdmin):
    list_display = ('website', 'start_time', 'end_time', 'tickets', 'price')


class RouteWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = [forms.TextInput(), forms.TextInput(), forms.TextInput(), forms.TextInput(),
                   forms.TextInput(), forms.TextInput(), forms.TextInput(), forms.TextInput(),
                   forms.TextInput(), forms.TextInput(), forms.TextInput(), forms.TextInput(),
                   forms.TextInput(), forms.TextInput(),
                   ]
        super(RouteWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return ' '.join(value)
        else:
            return ['', '', '', '', '', '', '', '', '', '', '', '', '', '']


class XRouteField(forms.MultiValueField):
    def __init__(self, *args, **kwargs):
        list_fields = [forms.CharField(), forms.CharField(), forms.CharField(), forms.CharField(),
                       forms.CharField(), forms.CharField(), forms.CharField(), forms.CharField(),
                       forms.CharField(), forms.CharField(), forms.CharField(), forms.CharField(),
                       forms.CharField(), forms.CharField(),
                       ]
        super(XRouteField, self).__init__(list_fields, widget=RouteWidget(), required=False, *args, **kwargs)

    def compress(self, values):
        return ' '.join(values)


class YRouteField(forms.MultiValueField):
    def __init__(self, *args, **kwargs):
        list_fields = [forms.CharField(), forms.CharField(), forms.CharField(), forms.CharField(),
                       forms.CharField(), forms.CharField(), forms.CharField(), forms.CharField(),
                       forms.CharField(), forms.CharField(), forms.CharField(), forms.CharField(),
                       forms.CharField(), forms.CharField(),
                       ]
        super(YRouteField, self).__init__(list_fields, widget=RouteWidget(), required=False, *args, **kwargs)

    def compress(self, values):
        return ' '.join(values)


class RouteForm(forms.ModelForm):

    class Meta:
        model = Route
        fields = '__all__'

    x_coordinates = XRouteField()
    y_coordinates = YRouteField()


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    change_form_template = "admin/dashboard/change_form.html"
    list_display = ('title', )
    exclude = ('route_x', 'route_y',)
    readonly_fields = ('add_x_coordinate', 'add_y_coordinate', 'display_route_x', 'display_route_y',)
    form = RouteForm
    model = Route

    def display_route_x(self, obj):  # Button for admin to get to API
        return obj.route_x

    display_route_x.allow_tags = True
    display_route_x.short_description = "Route x"

    def display_route_y(self, obj):  # Button for admin to get to API
        return obj.route_y

    display_route_y.allow_tags = True
    display_route_y.short_description = "Route y"

    def add_x_coordinate(self, obj):  # Button for admin to get to API
        return format_html(u'<a href="#" onclick="return false;" class="button" '
                           u'id="add_x_coordinate">Add x coordinate</a>')

    add_x_coordinate.allow_tags = True
    add_x_coordinate.short_description = "Add x coordinate"

    def add_y_coordinate(self, obj):  # Button for admin to get to API
        return format_html(u'<a href="#" onclick="return false;" class="button" '
                           u'id="add_y_coordinate">Add y coordinate</a>')

    add_y_coordinate.allow_tags = True
    add_y_coordinate.short_description = "Add y coordinate"

    def save_model(self, request, obj, form, change):
        if 'x_coordinates' in form.changed_data:
            obj.route_x = form.cleaned_data.get('x_coordinates').strip().replace(' ', ', ')
        if 'y_coordinates' in form.changed_data:
            obj.route_y = form.cleaned_data.get('y_coordinates').strip().replace(' ', ', ')
        super(RouteAdmin, self).save_model(request, obj, form, change)



