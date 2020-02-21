import sublime, sublime_plugin

class ReplaceChar(sublime_plugin.TextCommand):
    def run(self, edit):
      view = self.view
      ctr = view.settings().get("char_to_replace", False)
      rcw = view.settings().get("replace_char_with", False)

      if not ctr:
          return

      if not rcw:
          return

      pat = r"[ \t\f]+$"
      regions = view.find_all(pat)

      if regions:
          for r in regions:
              view.replace(edit, r, rcw)

class ReplaceCharEventListener(sublime_plugin.EventListener):
  def on_pre_save(self, view):
    if view.is_scratch() or view.settings().get('is_widget'):
        return
    if view.settings().get("replace_on_save", False):
        view.run_command("replace_char")
