from diservice      import DigitallyImportedService
from skyservice     import SkyFmService
from settingsdialog import SettingsDialog

import clementine

class Plugin:
  def __init__(self):
    self.settings_dialog = None

    # Create the services and add them to the Internet tab
    self.di_service = DigitallyImportedService(clementine.radio_model)
    self.sky_service = SkyFmService(clementine.radio_model)
    clementine.radio_model.AddService(self.di_service)
    clementine.radio_model.AddService(self.sky_service)

    # Register for when the user clicks the Settings button
    script.SettingsDialogRequested.connect(self.ShowSettings)

    # Register for the "Configure..." right click menu items
    self.di_service.SettingsDialogRequested.connect(self.ShowSettings)
    self.sky_service.SettingsDialogRequested.connect(self.ShowSettings)

  def ShowSettings(self):
    if not self.settings_dialog:
      # Create the dialog the first time it's shown
      self.settings_dialog = SettingsDialog()
      self.settings_dialog.accepted.connect(self.di_service.ReloadSettings)
      self.settings_dialog.accepted.connect(self.sky_service.ReloadSettings)

    self.settings_dialog.show()

plugin = Plugin()
