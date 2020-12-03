from mapbox_location_field.widgets import MapInput


class MapWidget(MapInput):
    class Media:
        js = ("js/map_input.js",)
        css = {
            "all": ("mapbox_location_field/css/map_input.css",)
        }

    def get_config_settings(self):
        self.center_point = False
        return super(MapWidget, self).get_config_settings()
