


import sublime
import sublime_plugin


class DefaultSyntaxCommand( sublime_plugin.EventListener ):

    def on_new( self, view ):

        settings   = sublime.load_settings("Preferences.sublime-settings")
        new_syntax = settings.get('new_file_syntax', None)

        if new_syntax:
	        view.set_syntax_file( new_syntax )




