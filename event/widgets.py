from mapbox_location_field.widgets import MapInput


class MapWidget(MapInput):
    """
        This widget overrides media for original MapInput.

        We use the modified js code so that addresses are saved in the database, not coordinates.

        Due to the fact that we are doing this, an error may occur when resubmitting the form from view.
         It expects coordinates in self.center_point, so in get_config_settings we have to set it to False.

    """

    class Media:
        js = ("js/map_input.js",)
        css = {
            "all": ("mapbox_location_field/css/map_input.css",)
        }

    def get_config_settings(self):
        if self.center_point:
            self.center_point = " " + self.center_point
        return super(MapWidget, self).get_config_settings()


class AdminMapWidget(MapWidget):
    class Media:
        js = ("js/map_input_admin.js",)
        css = {
            "all": ("mapbox_location_field/css/map_input.css",)
        }
