from django.contrib import admin
from django import forms
from django.utils.html import format_html

from .models import Map, Sections, Layers, Articles, Price, Museums, Route, GeneralMap, Language, Gallery


class ReservationInlineAdmin(admin.TabularInline):
    extra = 0
    model = Gallery
    fields = ('image', 'brief_description',)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Sections)
class SectionsAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Layers)
class LayersAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'map', 'type', 'language')
    inlines = [ReservationInlineAdmin]


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price',)


@admin.register(Museums)
class MuseumsAdmin(admin.ModelAdmin):
    list_display = ('title', 'map', 'type', 'language', 'website', 'start_time', 'end_time', 'tickets', 'price')
    inlines = [ReservationInlineAdmin]


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


class MapForm(forms.ModelForm):

    class Meta:
        model = Map
        fields = '__all__'

    x_coordinates = XRouteField()
    y_coordinates = YRouteField()


class GeneralMapForm(forms.ModelForm):

    class Meta:
        model = GeneralMap
        fields = '__all__'

    x_coordinates = XRouteField()
    y_coordinates = YRouteField()


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('title', )
    exclude = ('route_x', 'route_y',)
    change_form_template = "admin/dashboard/route_form.html"
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


@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    list_display = ('title', 'pin_x', 'pin_y',)
    readonly_fields = ('add_highlight_x', 'add_highlight_y', 'display_highlight_x', 'display_highlight_y',)
    exclude = ('highlight_x', 'highlight_y',)
    change_form_template = "admin/dashboard/map_form.html"
    form = MapForm
    model = Map

    def display_highlight_x(self, obj):  # Button for admin to get to API
        return obj.highlight_x

    display_highlight_x.allow_tags = True
    display_highlight_x.short_description = "Highlight x"

    def display_highlight_y(self, obj):  # Button for admin to get to API
        return obj.highlight_y

    display_highlight_y.allow_tags = True
    display_highlight_y.short_description = "Highlight y"

    def add_highlight_x(self, obj):  # Button for admin to get to API
        return format_html(u'<a href="#" onclick="return false;" class="button" '
                           u'id="add_highlight_x">Add highlight x</a>')

    add_highlight_x.allow_tags = True
    add_highlight_x.short_description = "Highlight x"

    def add_highlight_y(self, obj):  # Button for admin to get to API
        return format_html(u'<a href="#" onclick="return false;" class="button" '
                           u'id="add_highlight_y">Add highlight y</a>')

    add_highlight_y.allow_tags = True
    add_highlight_y.short_description = "Highlight y"

    def save_model(self, request, obj, form, change):
        if 'x_coordinates' in form.changed_data:
            obj.highlight_x = form.cleaned_data.get('x_coordinates').strip().replace(' ', ', ')
        if 'y_coordinates' in form.changed_data:
            obj.highlight_y = form.cleaned_data.get('y_coordinates').strip().replace(' ', ', ')
        super(MapAdmin, self).save_model(request, obj, form, change)


@admin.register(GeneralMap)
class GeneralMapAdmin(admin.ModelAdmin):
    list_display = ('title',)
    exclude = ('map_x', 'map_y',)
    change_form_template = "admin/dashboard/general_map_form.html"
    readonly_fields = ('add_map_x', 'add_map_y', 'display_map_x', 'display_map_y',)
    form = GeneralMapForm
    model = GeneralMap

    def display_map_x(self, obj):  # Button for admin to get to API
        return obj.map_x

    display_map_x.allow_tags = True
    display_map_x.short_description = "Map x"

    def display_map_y(self, obj):  # Button for admin to get to API
        return obj.map_x

    display_map_y.allow_tags = True
    display_map_y.short_description = "Map y"

    def add_map_x(self, obj):  # Button for admin to get to API
        return format_html(u'<a href="#" onclick="return false;" class="button" '
                           u'id="add_map_x">Add map x</a>')

    add_map_x.allow_tags = True
    add_map_x.short_description = "Add map x"

    def add_map_y(self, obj):  # Button for admin to get to API
        return format_html(u'<a href="#" onclick="return false;" class="button" '
                           u'id="add_map_y">Add map y</a>')

    add_map_y.allow_tags = True
    add_map_y.short_description = "Add map y"

    def save_model(self, request, obj, form, change):
        if 'x_coordinates' in form.changed_data:
            obj.map_x = form.cleaned_data.get('x_coordinates').strip().replace(' ', ', ')
        if 'y_coordinates' in form.changed_data:
            obj.map_y = form.cleaned_data.get('y_coordinates').strip().replace(' ', ', ')
        super(GeneralMapAdmin, self).save_model(request, obj, form, change)






