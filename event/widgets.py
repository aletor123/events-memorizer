from mapbox_location_field.widgets import MapInput


class MapWidget(MapInput):
    class Media:
        js = ("js/map_input.js",)
        css = {
            "all": ("mapbox_location_field/css/map_input.css",)
        }
